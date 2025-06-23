"""
InSight: Mars Weather Service API Module

This module provides access to NASA's InSight Mars Weather Service API.
"""

from .base import APIModule

class InsightModule(APIModule):
    """
    Module for accessing NASA's InSight Mars Weather Service API.
    
    This module provides methods to retrieve Mars weather data from the InSight lander.
    """
    
    def __init__(self, request_handler):
        """
        Initialize the InSight module.
        
        Args:
            request_handler (RequestHandler): The request handler to use for API requests.
        """
        super().__init__(request_handler)
        self.base_url = "https://api.nasa.gov/insight_weather/"
    
    def get_weather(self, version="1.0", feedtype="json"):
        """
        Get Mars weather data from the InSight lander.
        
        Note: As of September 2020, the InSight lander is no longer
        returning weather data due to Mars solar conjunction. This API
        may return historical data or may be unavailable.
        
        Args:
            version (str, optional): API version. Default is "1.0".
            feedtype (str, optional): Response format. Default is "json".
                
        Returns:
            dict: Mars weather data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "ver": version,
            "feedtype": feedtype
        }
        
        return self.request_handler.get(self._build_url(""), params)
