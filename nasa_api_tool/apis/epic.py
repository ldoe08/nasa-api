"""
EPIC (Earth Polychromatic Imaging Camera) API Module

This module provides access to NASA's EPIC API.
"""

from .base import APIModule

class EPICModule(APIModule):
    """
    Module for accessing NASA's EPIC API.
    
    This module provides methods to retrieve EPIC imagery data.
    """
    
    def __init__(self, request_handler):
        """
        Initialize the EPIC module.
        
        Args:
            request_handler (RequestHandler): The request handler to use for API requests.
        """
        super().__init__(request_handler)
        self.base_url = "https://api.nasa.gov/EPIC/api/"
    
    def get_images(self, collection="natural", date=None):
        """
        Get EPIC imagery for a specific date.
        
        Args:
            collection (str, optional): Image collection type ('natural', 'enhanced').
                Default is 'natural'.
            date (str, optional): Date of the imagery (YYYY-MM-DD).
                Default is most recent date.
                
        Returns:
            list: List of EPIC imagery metadata.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        if date:
            url = f"{collection}/date/{date}"
        else:
            url = f"{collection}"
        
        return self.request_handler.get(self._build_url(url))
    
    def get_available_dates(self, collection="natural"):
        """
        Get a list of dates with available EPIC imagery.
        
        Args:
            collection (str, optional): Image collection type ('natural', 'enhanced').
                Default is 'natural'.
                
        Returns:
            list: List of dates with available imagery.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        url = f"{collection}/available"
        return self.request_handler.get(self._build_url(url))
    
    def get_image_url(self, image, collection="natural"):
        """
        Get the URL for an EPIC image.
        
        Args:
            image (dict): EPIC image metadata from get_images().
            collection (str, optional): Image collection type ('natural', 'enhanced').
                Default is 'natural'.
                
        Returns:
            str: URL to the image.
        """
        date_parts = image["date"].split(" ")[0].split("-")
        year, month, day = date_parts
        image_name = image["image"]
        
        return f"https://api.nasa.gov/EPIC/archive/{collection}/{year}/{month}/{day}/png/{image_name}.png"
