"""
Routing utilities for AgriPort Optimizer using OSRM
"""
import os
import requests
import pandas as pd
import geopandas as gpd
import numpy as np
from typing import List, Dict, Tuple, Union, Any
import time
import logging

# Set up logging
logger = logging.getLogger(__name__)

class OSRMRouter:
    """
    Router class for interacting with OSRM service
    """
    def __init__(self, osrm_url: str = None):
        """
        Initialize the OSRM router
        
        Args:
            osrm_url: URL to OSRM service (default: env var or localhost:5000)
        """
        self.osrm_url = osrm_url or os.environ.get('OSRM_URL', 'http://localhost:5000')
        logger.info(f"Initialized OSRM router with URL: {self.osrm_url}")
    
    def check_connection(self) -> bool:
        """
        Check if OSRM service is available
        
        Returns:
            True if service is available, False otherwise
        """
        try:
            response = requests.get(f"{self.osrm_url}/health")
            return response.status_code == 200
        except requests.RequestException:
            return False
    
    def get_distance(self, origin: Tuple[float, float], destination: Tuple[float, float]) -> float:
        """
        Get distance between two points
        
        Args:
            origin: (lat, lon) of origin
            destination: (lat, lon) of destination
            
        Returns:
            Distance in kilometers
        """
        # Format coordinates for OSRM (lon,lat format)
        origin_str = f"{origin[1]},{origin[0]}"
        dest_str = f"{destination[1]},{destination[0]}"
        
        # Build URL
        url = f"{self.osrm_url}/route/v1/driving/{origin_str};{dest_str}?overview=false"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data['code'] != 'Ok':
                logger.warning(f"OSRM error: {data['code']} for route {origin} to {destination}")
                return None
            
            # Get distance in kilometers
            distance_km = data['routes'][0]['distance'] / 1000
            return distance_km
        
        except requests.RequestException as e:
            logger.error(f"Error in OSRM request: {str(e)}")
            return None
        except (KeyError, IndexError) as e:
            logger.error(f"Error parsing OSRM response: {str(e)}")
            return None
    
    def get_distance_matrix(self, origins: List[Tuple[float, float]], 
                            destinations: List[Tuple[float, float]], 
                            batch_size: int = 100) -> pd.DataFrame:
        """
        Get distance matrix between multiple origins and destinations using OSRM table service
        
        Args:
            origins: List of (lat, lon) tuples for origins
            destinations: List of (lat, lon) tuples for destinations
            batch_size: Number of locations per batch
            
        Returns:
            DataFrame with distances (km) from each origin to each destination
        """
        # Check inputs
        if not origins or not destinations:
            return pd.DataFrame()
        
        # Initialize results
        results = []
        
        # Process in batches to avoid overloading OSRM
        for i in range(0, len(origins), batch_size):
            batch_origins = origins[i:i+batch_size]
            
            for j in range(0, len(destinations), batch_size):
                batch_destinations = destinations[j:j+batch_size]
                
                # Format coordinates for OSRM (lon,lat format)
                coords = []
                for lat, lon in batch_origins:
                    coords.append(f"{lon},{lat}")
                for lat, lon in batch_destinations:
                    coords.append(f"{lon},{lat}")
                
                # Create sources and destinations indices
                sources = list(range(len(batch_origins)))
                destinations_idx = list(range(len(batch_origins), len(batch_origins) + len(batch_destinations)))
                
                # Build URL
                coords_str = ";".join(coords)
                url = f"{self.osrm_url}/table/v1/driving/{coords_str}"
                params = {
                    "sources": ",".join(map(str, sources)),
                    "destinations": ",".join(map(str, destinations_idx))
                }
                
                try:
                    response = requests.get(url, params=params)
                    response.raise_for_status()
                    data = response.json()
                    
                    if data['code'] != 'Ok':
                        logger.warning(f"OSRM error: {data['code']} for batch table request")
                        continue
                    
                    # Process distances
                    for src_idx, distances in enumerate(data['distances']):
                        origin_idx = i + src_idx
                        if origin_idx >= len(origins):
                            break
                        
                        for dst_idx, distance in enumerate(distances):
                            dest_idx = j + dst_idx
                            if dest_idx >= len(destinations):
                                break
                            
                            # Convert to kilometers
                            distance_km = distance / 1000 if distance >= 0 else None
                            
                            results.append({
                                'origin_idx': origin_idx,
                                'destination_idx': dest_idx,
                                'distance_km': distance_km
                            })
                
                except requests.RequestException as e:
                    logger.error(f"Error in OSRM table request: {str(e)}")
                except (KeyError, IndexError) as e:
                    logger.error(f"Error parsing OSRM table response: {str(e)}")
                
                # Avoid overloading the OSRM server
                time.sleep(0.5)
        
        # Create DataFrame
        df = pd.DataFrame(results)
        
        # Reshape to matrix format
        if not df.empty:
            matrix = df.pivot(index='origin_idx', columns='destination_idx', values='distance_km')
            return matrix
        else:
            return pd.DataFrame()
            
    def compute_grid_to_ports_distances(self, grid_gdf: gpd.GeoDataFrame, 
                                       ports_gdf: gpd.GeoDataFrame) -> pd.DataFrame:
        """
        Compute distances from each grid point to each port
        
        Args:
            grid_gdf: GeoDataFrame with grid points
            ports_gdf: GeoDataFrame with ports
            
        Returns:
            DataFrame with distances from each grid point to each port
        """
        # Extract coordinates
        grid_points = [(row.lat, row.lon) for _, row in grid_gdf.iterrows()]
        port_points = [(row.lat, row.lon) for _, row in ports_gdf.iterrows()]
        
        # Get distance matrix
        distances = self.get_distance_matrix(grid_points, port_points)
        
        # Format results
        results = []
        for i, grid_idx in enumerate(grid_gdf.index):
            for j, port_idx in enumerate(ports_gdf.index):
                try:
                    distance = distances.loc[i, j]
                    results.append({
                        'grid_point_id': grid_idx,
                        'port_id': port_idx,
                        'distance_km': distance
                    })
                except (KeyError, IndexError):
                    # Skip missing values
                    pass
        
        return pd.DataFrame(results)