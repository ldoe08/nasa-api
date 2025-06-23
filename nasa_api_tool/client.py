"""
NASA API Client

This module provides the main client class for accessing NASA APIs.
"""

from .request_handler import RequestHandler
from .apis.apod import APODModule
from .apis.asteroids import AsteroidsModule
from .apis.donki import DONKIModule
from .apis.earth import EarthModule
from .apis.eonet import EONETModule
from .apis.epic import EPICModule
from .apis.exoplanet import ExoplanetModule
from .apis.insight import InsightModule
from .apis.mars_rover import MarsRoverModule
from .apis.image_library import ImageLibraryModule
from .apis.tech_transfer import TechTransferModule
from .apis.ssc import SatelliteSituationCenterModule
from .apis.ssd_cneos import SSDCNEOSModule

class NASAClient:
    """
    Main client class for accessing NASA APIs.
    
    This class provides access to all NASA API modules and handles authentication.
    """
    
    def __init__(self, api_key=None):
        """
        Initialize the NASA API client.
        
        Args:
            api_key (str, optional): NASA API key. If None, uses "DEMO_KEY".
        """
        self.api_key = api_key or "DEMO_KEY"
        self.request_handler = RequestHandler(self.api_key)
        
        # Initialize API modules
        self.apod = APODModule(self.request_handler)
        self.asteroids = AsteroidsModule(self.request_handler)
        self.donki = DONKIModule(self.request_handler)
        self.earth = EarthModule(self.request_handler)
        self.eonet = EONETModule(self.request_handler)
        self.epic = EPICModule(self.request_handler)
        self.exoplanet = ExoplanetModule(self.request_handler)
        self.insight = InsightModule(self.request_handler)
        self.mars_rover = MarsRoverModule(self.request_handler)
        self.image_library = ImageLibraryModule(self.request_handler)
        self.tech_transfer = TechTransferModule(self.request_handler)
        self.ssc = SatelliteSituationCenterModule(self.request_handler)
        self.ssd_cneos = SSDCNEOSModule(self.request_handler)
    
    def set_api_key(self, api_key):
        """
        Set a new API key.
        
        Args:
            api_key (str): The new NASA API key to use.
        """
        self.api_key = api_key
        self.request_handler.api_key = api_key
