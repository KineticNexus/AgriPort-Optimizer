"""
GIS utilities for AgriPort Optimizer
"""
import os
import geopandas as gpd
import numpy as np
from shapely.geometry import Point, Polygon
import pandas as pd
from typing import List, Tuple, Dict, Any

def load_argentina_boundary(shapefile_path: str = None) -> gpd.GeoDataFrame:
    """
    Load the Argentina boundary shapefile
    
    Args:
        shapefile_path: Path to shapefile (optional)
        
    Returns:
        GeoDataFrame with Argentina boundary
    """
    if shapefile_path is None:
        # Default to data directory
        shapefile_path = os.path.join('data', 'boundaries', 'argentina.shp')
    
    try:
        # Load shapefile
        gdf = gpd.read_file(shapefile_path)
        
        # Ensure CRS is WGS84
        if gdf.crs != 'EPSG:4326':
            gdf = gdf.to_crs('EPSG:4326')
        
        return gdf
    except Exception as e:
        raise FileNotFoundError(f"Could not load Argentina boundary shapefile: {str(e)}")

def create_grid(boundary_gdf: gpd.GeoDataFrame, grid_size: int = 100) -> gpd.GeoDataFrame:
    """
    Create a grid of points covering Argentina
    
    Args:
        boundary_gdf: GeoDataFrame with Argentina boundary
        grid_size: Size of grid (grid_size x grid_size)
        
    Returns:
        GeoDataFrame with grid points
    """
    # Get the bounds of Argentina
    minx, miny, maxx, maxy = boundary_gdf.total_bounds
    
    # Create a grid of points
    x_coords = np.linspace(minx, maxx, grid_size)
    y_coords = np.linspace(miny, maxy, grid_size)
    
    # Create all combinations of x,y coordinates
    grid_points = []
    for y in y_coords:
        for x in x_coords:
            point = Point(x, y)
            grid_points.append(point)
    
    # Create GeoDataFrame
    grid_gdf = gpd.GeoDataFrame(geometry=grid_points, crs='EPSG:4326')
    
    # Only keep points that are within Argentina
    grid_gdf = gpd.sjoin(grid_gdf, boundary_gdf, predicate='within', how='inner')
    
    # Add lat/lon columns
    grid_gdf['lon'] = grid_gdf.geometry.x
    grid_gdf['lat'] = grid_gdf.geometry.y
    
    return grid_gdf

def create_port_regions(grid_gdf: gpd.GeoDataFrame, optimal_ports: pd.DataFrame) -> gpd.GeoDataFrame:
    """
    Create polygons representing regions for each port
    
    Args:
        grid_gdf: GeoDataFrame with grid points
        optimal_ports: DataFrame with optimal port assigned to each grid point
        
    Returns:
        GeoDataFrame with port regions
    """
    # Combine grid points with optimal ports
    grid_with_ports = grid_gdf.copy()
    grid_with_ports['optimal_port_id'] = optimal_ports['optimal_port_id']
    
    # Group by port and create convex hull for each group
    port_regions = []
    for port_id, group in grid_with_ports.groupby('optimal_port_id'):
        if len(group) >= 3:  # Need at least 3 points for a polygon
            # Create convex hull around points
            hull = group.unary_union.convex_hull
            port_regions.append({
                'port_id': port_id,
                'geometry': hull
            })
    
    # Create GeoDataFrame
    regions_gdf = gpd.GeoDataFrame(port_regions, crs='EPSG:4326')
    
    return regions_gdf

def find_boundary_points(grid_gdf: gpd.GeoDataFrame, optimal_ports: pd.DataFrame, threshold: float = 0.05) -> gpd.GeoDataFrame:
    """
    Find grid points at boundaries where port costs are similar
    
    Args:
        grid_gdf: GeoDataFrame with grid points
        optimal_ports: DataFrame with optimal port and costs for each grid point
        threshold: Threshold for cost difference to consider as boundary
        
    Returns:
        GeoDataFrame with boundary points
    """
    # Add cost difference to second-best port
    optimal_ports = optimal_ports.sort_values(['grid_point_id', 'total_cost'])
    
    cost_diffs = []
    for grid_id, group in optimal_ports.groupby('grid_point_id'):
        if len(group) >= 2:
            # Calculate difference between best and second-best
            best_cost = group.iloc[0]['total_cost']
            second_best = group.iloc[1]['total_cost']
            cost_diff = (second_best - best_cost) / best_cost  # Relative difference
            
            cost_diffs.append({
                'grid_point_id': grid_id,
                'cost_diff': cost_diff,
                'is_boundary': cost_diff <= threshold
            })
    
    cost_diff_df = pd.DataFrame(cost_diffs)
    
    # Join with grid points
    boundary_gdf = grid_gdf.merge(cost_diff_df, left_index=True, right_on='grid_point_id')
    boundary_gdf = boundary_gdf[boundary_gdf['is_boundary']]
    
    return boundary_gdf