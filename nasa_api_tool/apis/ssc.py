"""
Satellite Situation Center API Module

This module provides access to NASA's Satellite Situation Center API.
"""

from .base import APIModule

class SatelliteSituationCenterModule(APIModule):
    """
    Module for accessing NASA's Satellite Situation Center API.
    
    This module provides methods to retrieve spacecraft location information.
    """
    
    def __init__(self, request_handler):
        """
        Initialize the Satellite Situation Center module.
        
        Args:
            request_handler (RequestHandler): The request handler to use for API requests.
        """
        super().__init__(request_handler)
        self.base_url = "https://sscweb.gsfc.nasa.gov/WS/sscr/2/"
    
    def get_observatories(self):
        """
        Get a list of all available spacecraft (observatories) in the system.
        
        Returns:
            dict: List of available spacecraft.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        return self.request_handler.get(self._build_url("observatories"))
    
    def get_observatory_groups(self):
        """
        Get predefined groups of spacecraft.
        
        Returns:
            dict: List of spacecraft groups.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        return self.request_handler.get(self._build_url("observatoryGroups"))
    
    def get_locations(self, spacecraft, start_time, end_time, resolution):
        """
        Get spacecraft location data.
        
        Args:
            spacecraft (str or list): Comma-separated list of spacecraft IDs or a list.
            start_time (str): Start time in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).
            end_time (str): End time in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).
            resolution (int): Time resolution in seconds.
                
        Returns:
            dict: Spacecraft location data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        if isinstance(spacecraft, list):
            spacecraft = ",".join(spacecraft)
            
        url = f"locations/{spacecraft}/{start_time},{end_time}/{resolution}"
        return self.request_handler.get(self._build_url(url))
    
    def get_coordinate_systems(self):
        """
        Get available coordinate systems for location data.
        
        Returns:
            dict: List of available coordinate systems.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        return self.request_handler.get(self._build_url("coordinateSystems"))
    
    def get_spase_observatories(self):
        """
        Get SPASE (Space Physics Archive Search and Extract) metadata for spacecraft.
        
        Returns:
            dict: SPASE metadata for spacecraft.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        return self.request_handler.get(self._build_url("spaseObservatories"))
