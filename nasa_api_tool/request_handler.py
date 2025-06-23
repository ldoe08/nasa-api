"""
Request handler for NASA API requests.

This module handles HTTP requests to NASA APIs, including formatting,
sending, and receiving responses.
"""

import requests
from .exceptions import NASAAPIError

class RequestHandler:
    """
    Handles HTTP requests to NASA APIs.
    
    This class is responsible for making HTTP requests to NASA APIs,
    handling authentication, and processing responses.
    """
    
    def __init__(self, api_key):
        """
        Initialize the RequestHandler with an API key.
        
        Args:
            api_key (str): NASA API key. If None, uses "DEMO_KEY".
        """
        self.api_key = api_key or "DEMO_KEY"
        self.session = requests.Session()
    
    def get(self, url, params=None):
        """
        Make a GET request to the specified URL.
        
        Args:
            url (str): The URL to request.
            params (dict, optional): Query parameters to include in the request.
            
        Returns:
            dict: The JSON response from the API.
            
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        if params is None:
            params = {}
        
        # Add API key to parameters
        params["api_key"] = self.api_key
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            # Handle HTTP errors
            self._handle_error(e, response)
        except requests.exceptions.RequestException as e:
            # Handle connection errors
            raise NASAAPIError(f"Request failed: {str(e)}")
        except ValueError:
            # Handle JSON parsing errors
            raise NASAAPIError("Invalid response format")
    
    def _handle_error(self, error, response):
        """
        Handle HTTP errors from the API.
        
        Args:
            error (Exception): The original error.
            response (Response): The response object.
            
        Raises:
            NASAAPIError: With a descriptive message based on the status code.
        """
        status_code = response.status_code
        
        if status_code == 400:
            raise NASAAPIError("Bad request: Check your parameters")
        elif status_code == 401:
            raise NASAAPIError("Unauthorized: Check your API key")
        elif status_code == 403:
            raise NASAAPIError("Forbidden: You don't have access to this resource")
        elif status_code == 404:
            raise NASAAPIError("Not found: The requested resource doesn't exist")
        elif status_code == 429:
            raise NASAAPIError("Too many requests: You've exceeded your rate limit")
        elif status_code >= 500:
            raise NASAAPIError("Server error: NASA API is experiencing issues")
        else:
            raise NASAAPIError(f"HTTP error {status_code}: {response.text}")
