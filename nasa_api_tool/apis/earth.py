"""
Earth API Module

This module provides access to NASA's Earth API.
"""

from .base import APIModule

class EarthModule(APIModule):
    """
    Module for accessing NASA's Earth API.
    
    This module provides methods to retrieve Earth imagery and asset data.
    """
    
    def __init__(self, request_handler):
        """
        Initialize the Earth module.
        
        Args:
            request_handler (RequestHandler): The request handler to use for API requests.
        """
        super().__init__(request_handler)
        self.base_url = "https://api.nasa.gov/planetary/"
    
    def get_imagery(self, lat, lon, date=None, dim=0.025, cloud_score=False):
        """
        Get Landsat 8 imagery for the specified location and date.
        
        Args:
            lat (float): Latitude of the location.
            lon (float): Longitude of the location.
            date (str, optional): Date of the imagery (YYYY-MM-DD).
                Default is most recent date.
            dim (float, optional): Width and height of the image in degrees.
                Default is 0.025.
            cloud_score (bool, optional): Calculate the percentage of the image covered by clouds.
                Default is False.
                
        Returns:
            dict: Earth imagery data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "lat": lat,
            "lon": lon,
            "date": date,
            "dim": dim,
            "cloud_score": cloud_score
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("earth/imagery"), params)
    
    def get_assets(self, lat, lon, date=None, dim=0.025):
        """
        Get a list of available imagery for the specified location and date.
        
        Args:
            lat (float): Latitude of the location.
            lon (float): Longitude of the location.
            date (str, optional): Beginning date for search (YYYY-MM-DD).
                Default is 30 days prior to current date.
            dim (float, optional): Width and height of the image in degrees.
                Default is 0.025.
                
        Returns:
            dict: List of available imagery.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "lat": lat,
            "lon": lon,
            "date": date,
            "dim": dim
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("earth/assets"), params)
