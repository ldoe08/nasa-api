"""
Base API module for NASA APIs.

This module provides a base class for all NASA API modules.
"""

class APIModule:
    """
    Base class for all NASA API modules.
    
    This class provides common functionality for all NASA API modules,
    such as URL building and request handling.
    """
    
    def __init__(self, request_handler):
        """
        Initialize the API module with a request handler.
        
        Args:
            request_handler (RequestHandler): The request handler to use for API requests.
        """
        self.request_handler = request_handler
        self.base_url = "https://api.nasa.gov/"
    
    def _build_url(self, endpoint):
        """
        Build a full URL for the given endpoint.
        
        Args:
            endpoint (str): The API endpoint to access.
            
        Returns:
            str: The full URL.
        """
        return f"{self.base_url}{endpoint}"
