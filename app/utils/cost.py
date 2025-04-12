"""
Cost calculation utilities for AgriPort Optimizer
"""
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Union, Any
import logging

# Set up logging
logger = logging.getLogger(__name__)

def calculate_transportation_cost(distance_km: float, fuel_price: float, 
                                 fuel_efficiency: float = 0.4) -> float:
    """
    Calculate transportation cost based on distance and fuel price
    
    Args:
        distance_km: Distance in kilometers
        fuel_price: Fuel price in dollars per liter
        fuel_efficiency: Fuel consumption in liters per kilometer
                        (default: 0.4 L/km for a typical truck)
        
    Returns:
        Transportation cost in dollars per ton
    """
    if distance_km is None:
        return None
    
    # Basic cost formula: distance * fuel consumption * fuel price
    # We assume a standard truck carrying 25 tons
    truck_capacity_tons = 25.0
    
    # Cost per truck
    cost_per_truck = distance_km * fuel_efficiency * fuel_price
    
    # Cost per ton
    cost_per_ton = cost_per_truck / truck_capacity_tons
    
    return cost_per_ton

def calculate_total_cost(port_charge: float, sea_freight: float, 
                        distance_km: float, fuel_price: float) -> float:
    """
    Calculate total shipping cost
    
    Args:
        port_charge: Port charge in dollars per ton
        sea_freight: Sea freight cost in dollars per ton
        distance_km: Road distance in kilometers
        fuel_price: Fuel price in dollars per liter
        
    Returns:
        Total cost in dollars per ton
    """
    if distance_km is None:
        return None
    
    # Calculate transportation cost
    transport_cost = calculate_transportation_cost(distance_km, fuel_price)
    
    # Total cost = port charge + transportation cost + sea freight
    total_cost = port_charge + transport_cost + sea_freight
    
    return total_cost

def find_optimal_port(grid_distances: pd.DataFrame, ports_data: Dict[int, Dict], 
                     fuel_price: float) -> pd.DataFrame:
    """
    Find the optimal port for each grid point based on total cost
    
    Args:
        grid_distances: DataFrame with distances from each grid point to each port
        ports_data: Dictionary of port data (id -> {port_charge, sea_freight})
        fuel_price: Fuel price in dollars per liter
        
    Returns:
        DataFrame with optimal port and cost for each grid point
    """
    # Create empty results dataframe
    results = []
    
    # Process each grid point
    for grid_point_id in grid_distances['grid_point_id'].unique():
        grid_point_distances = grid_distances[grid_distances['grid_point_id'] == grid_point_id]
        
        # Calculate costs for each port
        for _, row in grid_point_distances.iterrows():
            port_id = row['port_id']
            distance_km = row['distance_km']
            
            # Skip if port not in data or distance is None
            if port_id not in ports_data or distance_km is None:
                continue
            
            port_data = ports_data[port_id]
            port_charge = port_data.get('port_charge', 0)
            sea_freight = port_data.get('sea_freight', 0)
            
            # Calculate total cost
            total_cost = calculate_total_cost(port_charge, sea_freight, distance_km, fuel_price)
            
            if total_cost is not None:
                results.append({
                    'grid_point_id': grid_point_id,
                    'port_id': port_id,
                    'distance_km': distance_km,
                    'port_charge': port_charge,
                    'sea_freight': sea_freight,
                    'fuel_price': fuel_price,
                    'total_cost': total_cost
                })
    
    # Convert to DataFrame
    results_df = pd.DataFrame(results)
    
    # Find optimal (lowest cost) port for each grid point
    if not results_df.empty:
        # Sort by grid_point_id and total_cost
        results_df = results_df.sort_values(['grid_point_id', 'total_cost'])
        
        # Get the lowest cost port for each grid point
        optimal_ports = results_df.groupby('grid_point_id').first().reset_index()
        optimal_ports['optimal_port_id'] = optimal_ports['port_id']
        
        return results_df
    
    return pd.DataFrame()

def generate_cost_gradients(ports_costs: pd.DataFrame, threshold: float = 0.05) -> pd.DataFrame:
    """
    Generate cost gradient data for visualization
    
    Args:
        ports_costs: DataFrame with costs for each grid point and port
        threshold: Threshold for relative cost difference to consider a gradient
        
    Returns:
        DataFrame with gradient information
    """
    # Find points where costs are close between best and second-best port
    gradients = []
    
    for grid_id, group in ports_costs.groupby('grid_point_id'):
        if len(group) < 2:
            continue
            
        # Sort by cost
        group = group.sort_values('total_cost')
        
        # Get costs for best and second-best ports
        best_port = group.iloc[0]
        second_best = group.iloc[1]
        
        # Calculate relative cost difference
        cost_diff = (second_best['total_cost'] - best_port['total_cost']) / best_port['total_cost']
        
        if cost_diff <= threshold:
            # This is a boundary point with gradient
            gradient_value = 1.0 - (cost_diff / threshold)  # 1.0 = equal costs, 0.0 = at threshold
            
            gradients.append({
                'grid_point_id': grid_id,
                'port_id_1': best_port['port_id'],
                'port_id_2': second_best['port_id'],
                'cost_1': best_port['total_cost'],
                'cost_2': second_best['total_cost'],
                'gradient_value': gradient_value
            })
    
    return pd.DataFrame(gradients)

def format_results_for_export(grid_points: pd.DataFrame, optimal_ports: pd.DataFrame) -> pd.DataFrame:
    """
    Format results for CSV export
    
    Args:
        grid_points: DataFrame with grid point coordinates
        optimal_ports: DataFrame with optimal port for each grid point
        
    Returns:
        DataFrame ready for export
    """
    # Merge grid points with optimal ports
    export_df = grid_points.merge(
        optimal_ports[['grid_point_id', 'optimal_port_id', 'distance_km', 'total_cost']],
        left_index=True,
        right_on='grid_point_id'
    )
    
    # Clean up columns for export
    export_df = export_df[['grid_point_id', 'lat', 'lon', 'optimal_port_id', 'distance_km', 'total_cost']]
    
    return export_df