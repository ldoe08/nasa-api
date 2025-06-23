"""
NASA Image and Video Library API Module

This module provides access to NASA's Image and Video Library API.
"""

from .base import APIModule

class ImageLibraryModule(APIModule):
    """
    Module for accessing NASA's Image and Video Library API.
    
    This module provides methods to search and retrieve NASA's media assets.
    """
    
    def __init__(self, request_handler):
        """
        Initialize the NASA Image and Video Library module.
        
        Args:
            request_handler (RequestHandler): The request handler to use for API requests.
        """
        super().__init__(request_handler)
        self.base_url = "https://images-api.nasa.gov/"
    
    def search(self, q=None, center=None, description=None, keywords=None, 
               location=None, media_type=None, nasa_id=None, page=1, year_start=None, 
               year_end=None):
        """
        Search for NASA images, videos, and audio files.
        
        Args:
            q (str, optional): Free text search terms.
            center (str, optional): NASA center that created the media.
            description (str, optional): Terms to search for in the description field.
            keywords (str, optional): Terms to search for in the keywords field.
            location (str, optional): Terms to search for in the location field.
            media_type (str, optional): Media type to filter results by (image, video, audio).
            nasa_id (str, optional): The NASA ID of the media.
            page (int, optional): Page number of results, starting from 1. Default is 1.
            year_start (int, optional): Starting year for results.
            year_end (int, optional): Ending year for results.
                
        Returns:
            dict: Search results.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "q": q,
            "center": center,
            "description": description,
            "keywords": keywords,
            "location": location,
            "media_type": media_type,
            "nasa_id": nasa_id,
            "page": page,
            "year_start": year_start,
            "year_end": year_end
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("search"), params)
    
    def get_asset(self, nasa_id):
        """
        Retrieve the media asset's manifest.
        
        Args:
            nasa_id (str): The NASA ID of the media asset.
                
        Returns:
            dict: Asset manifest data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        return self.request_handler.get(self._build_url(f"asset/{nasa_id}"))
    
    def get_metadata(self, nasa_id):
        """
        Retrieve detailed metadata for a specific media asset.
        
        Args:
            nasa_id (str): The NASA ID of the media asset.
                
        Returns:
            dict: Metadata for the specified asset.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        return self.request_handler.get(self._build_url(f"metadata/{nasa_id}"))
    
    def get_captions(self, nasa_id):
        """
        Retrieve the location of a video asset's caption file.
        
        Args:
            nasa_id (str): The NASA ID of the video asset.
                
        Returns:
            dict: Caption file location data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        return self.request_handler.get(self._build_url(f"captions/{nasa_id}"))
