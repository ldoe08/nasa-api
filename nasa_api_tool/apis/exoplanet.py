"""
Exoplanet API Module

This module provides access to NASA's Exoplanet Archive API.
"""

from .base import APIModule

class ExoplanetModule(APIModule):
    """
    Module for accessing NASA's Exoplanet Archive API.
    
    This module provides methods to retrieve exoplanet data.
    """
    
    def __init__(self, request_handler):
        """
        Initialize the Exoplanet module.
        
        Args:
            request_handler (RequestHandler): The request handler to use for API requests.
        """
        super().__init__(request_handler)
        self.base_url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?"
    
    def query(self, table="ps", select="*", where=None, order=None, format="json"):
        """
        Query the Exoplanet Archive database.
        
        Args:
            table (str, optional): Table to query. Default is "ps" (Planetary Systems).
                Other options include "pscomppars" (Planetary Systems Composite Parameters).
            select (str, optional): Columns to select. Default is "*" (all columns).
            where (str, optional): WHERE clause for filtering results.
            order (str, optional): ORDER BY clause for sorting results.
            format (str, optional): Response format. Default is "json".
                Other options include "csv", "tsv", "votable".
                
        Returns:
            list or str: Query results in the specified format.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        query_parts = [f"select {select}", f"from {table}"]
        
        if where:
            query_parts.append(f"where {where}")
        
        if order:
            query_parts.append(f"order by {order}")
        
        query = " ".join(query_parts)
        
        params = {
            "query": query,
            "format": format
        }
        
        return self.request_handler.get(self.base_url, params)
    
    def get_confirmed_planets(self, limit=10, format="json"):
        """
        Get a list of confirmed exoplanets.
        
        Args:
            limit (int, optional): Maximum number of results to return. Default is 10.
            format (str, optional): Response format. Default is "json".
                
        Returns:
            list or str: Confirmed exoplanet data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        return self.query(
            table="ps",
            select="pl_name,hostname,discoverymethod,disc_year,pl_orbper,pl_masse,pl_rade,st_dist",
            where="default_flag=1",
            order="disc_year desc",
            format=format
        )
    
    def get_planet_by_name(self, planet_name, format="json"):
        """
        Get data for a specific exoplanet by name.
        
        Args:
            planet_name (str): Name of the exoplanet.
            format (str, optional): Response format. Default is "json".
                
        Returns:
            list or str: Exoplanet data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        return self.query(
            table="ps",
            select="*",
            where=f"pl_name='{planet_name}' and default_flag=1",
            format=format
        )
    
    def get_planets_in_habitable_zone(self, format="json"):
        """
        Get a list of exoplanets in the habitable zone.
        
        Args:
            format (str, optional): Response format. Default is "json".
                
        Returns:
            list or str: Exoplanet data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        return self.query(
            table="ps",
            select="pl_name,hostname,discoverymethod,disc_year,pl_orbper,pl_masse,pl_rade,st_dist",
            where="default_flag=1 and habitable_zone=1",
            format=format
        )
