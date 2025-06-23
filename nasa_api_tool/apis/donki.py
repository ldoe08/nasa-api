"""
DONKI (Space Weather Database Of Notifications, Knowledge, Information) API Module

This module provides access to NASA's DONKI API.
"""

from .base import APIModule

class DONKIModule(APIModule):
    """
    Module for accessing NASA's DONKI API.
    
    This module provides methods to retrieve space weather data.
    """
    
    def __init__(self, request_handler):
        """
        Initialize the DONKI module.
        
        Args:
            request_handler (RequestHandler): The request handler to use for API requests.
        """
        super().__init__(request_handler)
        self.base_url = "https://api.nasa.gov/DONKI/"
    
    def get_coronal_mass_ejection(self, start_date=None, end_date=None):
        """
        Get coronal mass ejection (CME) data.
        
        Args:
            start_date (str, optional): Start date for search (YYYY-MM-DD).
                Default is 30 days prior to current UTC date.
            end_date (str, optional): End date for search (YYYY-MM-DD).
                Default is current UTC date.
                
        Returns:
            list: List of CME events.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "startDate": start_date,
            "endDate": end_date
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("CME"), params)
    
    def get_coronal_mass_ejection_analysis(self, start_date=None, end_date=None, most_accurate_only=None, speed=None, half_angle=None, catalog=None):
        """
        Get coronal mass ejection (CME) analysis data.
        
        Args:
            start_date (str, optional): Start date for search (YYYY-MM-DD).
                Default is 30 days prior to current UTC date.
            end_date (str, optional): End date for search (YYYY-MM-DD).
                Default is current UTC date.
            most_accurate_only (bool, optional): If True, get most accurate results only.
            speed (int, optional): Speed filter (km/s).
            half_angle (int, optional): Half angle filter (degrees).
            catalog (str, optional): Catalog filter (SWRC_CATALOG, JANG_ET_AL_CATALOG).
                
        Returns:
            list: List of CME analysis events.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "startDate": start_date,
            "endDate": end_date,
            "mostAccurateOnly": most_accurate_only,
            "speed": speed,
            "halfAngle": half_angle,
            "catalog": catalog
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("CMEAnalysis"), params)
    
    def get_geomagnetic_storm(self, start_date=None, end_date=None):
        """
        Get geomagnetic storm data.
        
        Args:
            start_date (str, optional): Start date for search (YYYY-MM-DD).
                Default is 30 days prior to current UTC date.
            end_date (str, optional): End date for search (YYYY-MM-DD).
                Default is current UTC date.
                
        Returns:
            list: List of geomagnetic storm events.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "startDate": start_date,
            "endDate": end_date
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("GST"), params)
    
    def get_interplanetary_shock(self, start_date=None, end_date=None, location=None, catalog=None):
        """
        Get interplanetary shock data.
        
        Args:
            start_date (str, optional): Start date for search (YYYY-MM-DD).
                Default is 30 days prior to current UTC date.
            end_date (str, optional): End date for search (YYYY-MM-DD).
                Default is current UTC date.
            location (str, optional): Location filter (Earth, MESSENGER, STEREO A, STEREO B).
            catalog (str, optional): Catalog filter (SWRC_CATALOG, WINSLOW_MESSENGER_CATALOG).
                
        Returns:
            list: List of interplanetary shock events.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "startDate": start_date,
            "endDate": end_date,
            "location": location,
            "catalog": catalog
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("IPS"), params)
    
    def get_solar_flare(self, start_date=None, end_date=None):
        """
        Get solar flare data.
        
        Args:
            start_date (str, optional): Start date for search (YYYY-MM-DD).
                Default is 30 days prior to current UTC date.
            end_date (str, optional): End date for search (YYYY-MM-DD).
                Default is current UTC date.
                
        Returns:
            list: List of solar flare events.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "startDate": start_date,
            "endDate": end_date
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("FLR"), params)
    
    def get_solar_energetic_particle(self, start_date=None, end_date=None):
        """
        Get solar energetic particle (SEP) data.
        
        Args:
            start_date (str, optional): Start date for search (YYYY-MM-DD).
                Default is 30 days prior to current UTC date.
            end_date (str, optional): End date for search (YYYY-MM-DD).
                Default is current UTC date.
                
        Returns:
            list: List of SEP events.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "startDate": start_date,
            "endDate": end_date
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("SEP"), params)
    
    def get_magnetopause_crossing(self, start_date=None, end_date=None):
        """
        Get magnetopause crossing data.
        
        Args:
            start_date (str, optional): Start date for search (YYYY-MM-DD).
                Default is 30 days prior to current UTC date.
            end_date (str, optional): End date for search (YYYY-MM-DD).
                Default is current UTC date.
                
        Returns:
            list: List of magnetopause crossing events.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "startDate": start_date,
            "endDate": end_date
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("MPC"), params)
    
    def get_radiation_belt_enhancement(self, start_date=None, end_date=None):
        """
        Get radiation belt enhancement data.
        
        Args:
            start_date (str, optional): Start date for search (YYYY-MM-DD).
                Default is 30 days prior to current UTC date.
            end_date (str, optional): End date for search (YYYY-MM-DD).
                Default is current UTC date.
                
        Returns:
            list: List of radiation belt enhancement events.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "startDate": start_date,
            "endDate": end_date
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("RBE"), params)
    
    def get_hss(self, start_date=None, end_date=None):
        """
        Get high-speed stream (HSS) data.
        
        Args:
            start_date (str, optional): Start date for search (YYYY-MM-DD).
                Default is 30 days prior to current UTC date.
            end_date (str, optional): End date for search (YYYY-MM-DD).
                Default is current UTC date.
                
        Returns:
            list: List of HSS events.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "startDate": start_date,
            "endDate": end_date
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("HSS"), params)
    
    def get_wsa_enlil_simulation(self, start_date=None, end_date=None):
        """
        Get WSA+ENLIL simulation data.
        
        Args:
            start_date (str, optional): Start date for search (YYYY-MM-DD).
                Default is 30 days prior to current UTC date.
            end_date (str, optional): End date for search (YYYY-MM-DD).
                Default is current UTC date.
                
        Returns:
            list: List of WSA+ENLIL simulation runs.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "startDate": start_date,
            "endDate": end_date
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("WSAEnlilSimulations"), params)
    
    def get_notifications(self, start_date=None, end_date=None, type=None):
        """
        Get notifications data.
        
        Args:
            start_date (str, optional): Start date for search (YYYY-MM-DD).
                Default is 30 days prior to current UTC date.
            end_date (str, optional): End date for search (YYYY-MM-DD).
                Default is current UTC date.
            type (str, optional): Notification type filter (all, FLR, SEP, CME, IPS, MPC, GST, RBE, report).
                
        Returns:
            list: List of notifications.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "startDate": start_date,
            "endDate": end_date,
            "type": type
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("notifications"), params)
