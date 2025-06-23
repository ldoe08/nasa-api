"""
APOD (Astronomy Picture of the Day) API Module

This module provides access to NASA's APOD API.
"""

from .base import APIModule

class APODModule(APIModule):
    """
    Module for accessing NASA's Astronomy Picture of the Day API.
    
    This module provides methods to retrieve the astronomy picture of the day
    and related metadata.
    """
    
    def __init__(self, request_handler):
        """
        Initialize the APOD module.
        
        Args:
            request_handler (RequestHandler): The request handler to use for API requests.
        """
        super().__init__(request_handler)
        self.base_url = "https://api.nasa.gov/planetary/"
    
    def get_astronomy_picture(self, date=None, start_date=None, end_date=None, count=None, thumbs=False):
        """
        Get the Astronomy Picture of the Day.
        
        Args:
            date (str, optional): The date of the APOD image to retrieve (YYYY-MM-DD).
                Cannot be used with start_date, end_date, or count.
            start_date (str, optional): The start date of a date range (YYYY-MM-DD).
                Must be used with end_date. Cannot be used with date or count.
            end_date (str, optional): The end date of a date range (YYYY-MM-DD).
                Must be used with start_date. Cannot be used with date or count.
            count (int, optional): The number of random images to retrieve.
                Cannot be used with date, start_date, or end_date.
            thumbs (bool, optional): Whether to include thumbnail URLs for video content.
                Default is False.
                
        Returns:
            dict or list: The APOD data. If a date range or count is specified,
                returns a list of dictionaries.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "date": date,
            "start_date": start_date,
            "end_date": end_date,
            "count": count,
            "thumbs": thumbs
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("apod"), params)
