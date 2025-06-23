"""
EONET (Earth Observatory Natural Event Tracker) API Module

This module provides access to NASA's EONET API.
"""

from .base import APIModule

class EONETModule(APIModule):
    """
    Module for accessing NASA's EONET API.
    
    This module provides methods to retrieve natural event data.
    """
    
    def __init__(self, request_handler):
        """
        Initialize the EONET module.
        
        Args:
            request_handler (RequestHandler): The request handler to use for API requests.
        """
        super().__init__(request_handler)
        self.base_url = "https://eonet.gsfc.nasa.gov/api/v3/"
    
    def get_events(self, source=None, status=None, limit=None, days=None, category=None):
        """
        Get natural event data.
        
        Args:
            source (str, optional): Filter events by source.
            status (str, optional): Filter events by status (open, closed, all).
                Default is 'all'.
            limit (int, optional): Limit the number of events returned.
            days (int, optional): Limit the number of days to search.
            category (str or int, optional): Filter events by category ID or title.
                
        Returns:
            dict: Natural event data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "source": source,
            "status": status,
            "limit": limit,
            "days": days,
            "category": category
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("events"), params)
    
    def get_categories(self):
        """
        Get a list of event categories.
        
        Returns:
            dict: Event category data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        return self.request_handler.get(self._build_url("categories"))
    
    def get_sources(self):
        """
        Get a list of event sources.
        
        Returns:
            dict: Event source data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        return self.request_handler.get(self._build_url("sources"))
    
    def get_layers(self):
        """
        Get a list of available web service layers.
        
        Returns:
            dict: Layer data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        return self.request_handler.get(self._build_url("layers"))
