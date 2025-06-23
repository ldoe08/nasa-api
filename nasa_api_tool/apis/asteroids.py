"""
Asteroids NeoWs (Near Earth Object Web Service) API Module

This module provides access to NASA's Asteroids NeoWs API.
"""

from .base import APIModule

class AsteroidsModule(APIModule):
    """
    Module for accessing NASA's Asteroids NeoWs API.
    
    This module provides methods to retrieve data about near-Earth objects.
    """
    
    def __init__(self, request_handler):
        """
        Initialize the Asteroids NeoWs module.
        
        Args:
            request_handler (RequestHandler): The request handler to use for API requests.
        """
        super().__init__(request_handler)
        self.base_url = "https://api.nasa.gov/neo/rest/v1/"
    
    def get_feed(self, start_date=None, end_date=None):
        """
        Get a list of asteroids based on their closest approach date to Earth.
        
        Args:
            start_date (str, optional): Starting date for asteroid search (YYYY-MM-DD).
                Default is today.
            end_date (str, optional): Ending date for asteroid search (YYYY-MM-DD).
                Default is 7 days after start_date. Maximum range is 7 days.
                
        Returns:
            dict: Near-Earth object data for the specified date range.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "start_date": start_date,
            "end_date": end_date
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("feed"), params)
    
    def get_lookup(self, asteroid_id):
        """
        Look up an asteroid by its NASA JPL small body ID.
        
        Args:
            asteroid_id (str): Asteroid SPK-ID.
                
        Returns:
            dict: Detailed information about the specified asteroid.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        return self.request_handler.get(self._build_url(f"neo/{asteroid_id}"))
    
    def get_browse(self, page=None, size=None):
        """
        Browse the overall asteroid data-set.
        
        Args:
            page (int, optional): Page number (zero-based).
            size (int, optional): Number of elements per page.
                
        Returns:
            dict: Paginated list of near-Earth objects.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "page": page,
            "size": size
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("neo/browse"), params)
