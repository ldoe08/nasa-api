"""
TechTransfer API Module

This module provides access to NASA's TechTransfer API.
"""

from .base import APIModule

class TechTransferModule(APIModule):
    """
    Module for accessing NASA's TechTransfer API.
    
    This module provides methods to retrieve NASA's patents, software, and technology spinoff descriptions.
    """
    
    def __init__(self, request_handler):
        """
        Initialize the TechTransfer module.
        
        Args:
            request_handler (RequestHandler): The request handler to use for API requests.
        """
        super().__init__(request_handler)
        self.base_url = "https://api.nasa.gov/techtransfer/"
    
    def get_patents(self, query=None):
        """
        Get NASA patent data.
        
        Args:
            query (str, optional): Search term to filter patents.
                
        Returns:
            dict: Patent data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {}
        if query:
            params["patent"] = query
        
        return self.request_handler.get(self._build_url("patent"), params)
    
    def get_patent_issued(self, query=None):
        """
        Get NASA issued patent data.
        
        Args:
            query (str, optional): Search term to filter issued patents.
                
        Returns:
            dict: Issued patent data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {}
        if query:
            params["patent_issued"] = query
        
        return self.request_handler.get(self._build_url("patent"), params)
    
    def get_software(self, query=None):
        """
        Get NASA software data.
        
        Args:
            query (str, optional): Search term to filter software.
                
        Returns:
            dict: Software data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {}
        if query:
            params["software"] = query
        
        return self.request_handler.get(self._build_url("software"), params)
    
    def get_spinoff(self, query=None):
        """
        Get NASA spinoff data.
        
        Args:
            query (str, optional): Search term to filter spinoff examples.
                
        Returns:
            dict: Spinoff data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {}
        if query:
            params["spinoff"] = query
        
        return self.request_handler.get(self._build_url("spinoff"), params)
