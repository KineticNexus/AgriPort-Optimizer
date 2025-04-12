"""
Database models for AgriPort Optimizer
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from geoalchemy2 import Geometry
from . import db

class Port(db.Model):
    """
    Port model representing shipping ports in Argentina
    """
    __tablename__ = 'ports'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    location = Column(Geometry('POINT', srid=4326), nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<Port {self.name} ({self.lat}, {self.lon})>"
    
    def to_dict(self):
        """
        Convert port to dictionary for API responses
        """
        return {
            'id': self.id,
            'name': self.name,
            'lat': self.lat,
            'lon': self.lon,
            'active': self.active
        }

class GridPoint(db.Model):
    """
    GridPoint model representing points in the 100x100 grid over Argentina
    This can be populated once at setup time
    """
    __tablename__ = 'grid_points'
    
    id = Column(Integer, primary_key=True)
    location = Column(Geometry('POINT', srid=4326), nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    
    def __repr__(self):
        return f"<GridPoint {self.id} ({self.lat}, {self.lon})>"
    
    def to_dict(self):
        """
        Convert grid point to dictionary for API responses
        """
        return {
            'id': self.id,
            'lat': self.lat,
            'lon': self.lon
        }

class Distance(db.Model):
    """
    Distance model for storing precomputed distances between grid points and ports
    """
    __tablename__ = 'distances'
    
    id = Column(Integer, primary_key=True)
    grid_point_id = Column(Integer, db.ForeignKey('grid_points.id'), nullable=False)
    port_id = Column(Integer, db.ForeignKey('ports.id'), nullable=False)
    distance_km = Column(Float, nullable=False)
    
    # Define relationships
    grid_point = db.relationship('GridPoint', backref=db.backref('distances', lazy=True))
    port = db.relationship('Port', backref=db.backref('distances', lazy=True))
    
    def __repr__(self):
        return f"<Distance Grid:{self.grid_point_id} to Port:{self.port_id} = {self.distance_km}km>"