"""
Main routes for AgriPort Optimizer
"""
from flask import Blueprint, render_template, request, jsonify, current_app
import json
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@main_bp.route('/calculate', methods=['POST'])
def calculate():
    """
    Calculate optimal ports for grid points based on input costs
    
    Expected input JSON:
    {
        "fuel_price": float,
        "ports": [
            {
                "id": int,
                "name": string,
                "port_charge": float,
                "sea_freight": float
            },
            ...
        ]
    }
    """
    try:
        # Validate input
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
        
        data = request.get_json()
        
        # Basic validation
        if "fuel_price" not in data or not isinstance(data["fuel_price"], (int, float)):
            return jsonify({"error": "Valid fuel price required"}), 400
        
        if "ports" not in data or not isinstance(data["ports"], list) or len(data["ports"]) == 0:
            return jsonify({"error": "At least one port is required"}), 400
        
        # Log the request (for development)
        if current_app.debug:
            current_app.logger.debug(f"Calculation request: {data}")
        
        # TODO: This is where actual calculation logic will go
        # For now, return placeholder data
        
        return jsonify({
            "status": "success",
            "message": "Calculation endpoint ready. Implementation pending.",
            "received_data": data
        })
    
    except Exception as e:
        current_app.logger.error(f"Error in calculate: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@main_bp.route('/export', methods=['GET'])
def export():
    """
    Export grid assignments as CSV
    
    Query parameters:
    - format: 'csv' (default) or 'json'
    """
    try:
        # TODO: Implement export logic when grid calculation is ready
        return jsonify({
            "status": "success",
            "message": "Export endpoint ready. Implementation pending."
        })
    
    except Exception as e:
        current_app.logger.error(f"Error in export: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500