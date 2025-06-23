"""
Mars Rover Photos API Module

This module provides access to NASA's Mars Rover Photos API.
"""

from .base import APIModule

class MarsRoverModule(APIModule):
    """
    Module for accessing NASA's Mars Rover Photos API.
    
    This module provides methods to retrieve photos taken by Mars rovers.
    """
    
    def __init__(self, request_handler):
        """
        Initialize the Mars Rover Photos module.
        
        Args:
            request_handler (RequestHandler): The request handler to use for API requests.
        """
        super().__init__(request_handler)
        self.base_url = "https://api.nasa.gov/mars-photos/api/v1/"
    
    def get_photos(self, rover, sol=None, earth_date=None, camera=None, page=1):
        """
        Get photos from a Mars rover.
        
        Args:
            rover (str): Rover name (curiosity, opportunity, spirit, perseverance).
            sol (int, optional): Martian sol (day) of the rover's mission.
                Either sol or earth_date must be specified.
            earth_date (str, optional): Earth date in YYYY-MM-DD format.
                Either sol or earth_date must be specified.
            camera (str, optional): Filter by camera type.
                Valid cameras depend on the rover.
            page (int, optional): Page number for pagination. Default is 1.
                
        Returns:
            dict: Mars rover photos data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        if not sol and not earth_date:
            raise ValueError("Either sol or earth_date must be specified")
        
        params = {
            "sol": sol,
            "earth_date": earth_date,
            "camera": camera,
            "page": page
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url(f"rovers/{rover}/photos"), params)
    
    def get_rover_manifest(self, rover):
        """
        Get mission manifest for a Mars rover.
        
        Args:
            rover (str): Rover name (curiosity, opportunity, spirit, perseverance).
                
        Returns:
            dict: Rover mission manifest data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        return self.request_handler.get(self._build_url(f"manifests/{rover}"))
