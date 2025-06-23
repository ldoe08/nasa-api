"""
NASA Universal API Tool

A comprehensive Python library for accessing NASA's APIs through a unified interface.
"""

from .exceptions import NASAAPIError
from .client import NASAClient

__version__ = "0.1.0"
__all__ = ["NASAClient", "NASAAPIError"]
