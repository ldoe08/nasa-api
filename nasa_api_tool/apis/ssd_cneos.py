"""
SSD/CNEOS (Solar System Dynamics and Center for Near-Earth Object Studies) API Module

This module provides access to NASA's SSD/CNEOS API.
"""

from .base import APIModule

class SSDCNEOSModule(APIModule):
    """
    Module for accessing NASA's SSD/CNEOS API.
    
    This module provides methods to retrieve data about asteroids, comets, and near-Earth objects.
    """
    
    def __init__(self, request_handler):
        """
        Initialize the SSD/CNEOS module.
        
        Args:
            request_handler (RequestHandler): The request handler to use for API requests.
        """
        super().__init__(request_handler)
        self.base_url = "https://ssd-api.jpl.nasa.gov/"
    
    def get_cad(self, date_min=None, date_max=None, dist_min=None, dist_max=None, 
                h_min=None, h_max=None, v_inf_min=None, v_inf_max=None, v_rel_min=None, 
                v_rel_max=None, class_filter=None, pha=None, nea=None, comet=None, 
                neo=None, kind=None, spk=None, des=None, body=None, sort="date", 
                limit=50, fullname=False, format="json"):
        """
        Get close-approach data for asteroids and comets.
        
        Args:
            date_min (str, optional): Start date for search (days from now or YYYY-MM-DD).
                Default is -30 (30 days ago).
            date_max (str, optional): End date for search (days from now or YYYY-MM-DD).
                Default is +60 (60 days from now).
            dist_min (float, optional): Minimum approach distance (au or LD).
            dist_max (float, optional): Maximum approach distance (au or LD).
                Default is 0.05 au.
            h_min (float, optional): Minimum absolute magnitude.
            h_max (float, optional): Maximum absolute magnitude.
            v_inf_min (float, optional): Minimum approach velocity (km/s).
            v_inf_max (float, optional): Maximum approach velocity (km/s).
            v_rel_min (float, optional): Minimum relative velocity (km/s).
            v_rel_max (float, optional): Maximum relative velocity (km/s).
            class_filter (str, optional): Object class/type filter.
            pha (bool, optional): Potentially Hazardous Asteroid filter.
            nea (bool, optional): Near-Earth Asteroid filter.
            comet (bool, optional): Comet filter.
            neo (bool, optional): Near-Earth Object filter.
            kind (str, optional): Object kind filter (a=asteroid, c=comet).
            spk (int or str, optional): Object SPK-ID filter.
            des (str, optional): Object designation filter.
            body (str, optional): Body filter (Earth, Moon, etc.).
            sort (str, optional): Sort key. Default is "date".
            limit (int, optional): Maximum number of results. Default is 50.
            fullname (bool, optional): Show full object names. Default is False.
            format (str, optional): Output format. Default is "json".
                
        Returns:
            dict: Close-approach data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "date-min": date_min,
            "date-max": date_max,
            "dist-min": dist_min,
            "dist-max": dist_max,
            "h-min": h_min,
            "h-max": h_max,
            "v-inf-min": v_inf_min,
            "v-inf-max": v_inf_max,
            "v-rel-min": v_rel_min,
            "v-rel-max": v_rel_max,
            "class": class_filter,
            "pha": pha,
            "nea": nea,
            "comet": comet,
            "neo": neo,
            "kind": kind,
            "spk": spk,
            "des": des,
            "body": body,
            "sort": sort,
            "limit": limit,
            "fullname": fullname,
            "format": format
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("cad.api"), params)
    
    def get_fireball(self, date_min=None, date_max=None, energy_min=None, energy_max=None,
                    impact_e_min=None, impact_e_max=None, vel_min=None, vel_max=None,
                    alt_min=None, alt_max=None, req_loc=None, limit=50, sort="date",
                    format="json"):
        """
        Get fireball atmospheric impact event data.
        
        Args:
            date_min (str, optional): Start date (YYYY-MM-DD).
            date_max (str, optional): End date (YYYY-MM-DD).
            energy_min (float, optional): Minimum energy (kt).
            energy_max (float, optional): Maximum energy (kt).
            impact_e_min (float, optional): Minimum impact energy (kt).
            impact_e_max (float, optional): Maximum impact energy (kt).
            vel_min (float, optional): Minimum velocity (km/s).
            vel_max (float, optional): Maximum velocity (km/s).
            alt_min (float, optional): Minimum altitude (km).
            alt_max (float, optional): Maximum altitude (km).
            req_loc (bool, optional): Require location data.
            limit (int, optional): Maximum number of results. Default is 50.
            sort (str, optional): Sort key. Default is "date".
            format (str, optional): Output format. Default is "json".
                
        Returns:
            dict: Fireball event data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "date-min": date_min,
            "date-max": date_max,
            "energy-min": energy_min,
            "energy-max": energy_max,
            "impact-e-min": impact_e_min,
            "impact-e-max": impact_e_max,
            "vel-min": vel_min,
            "vel-max": vel_max,
            "alt-min": alt_min,
            "alt-max": alt_max,
            "req-loc": req_loc,
            "limit": limit,
            "sort": sort,
            "format": format
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("fireball.api"), params)
    
    def get_sentry(self, spk=None, des=None, h_min=None, h_max=None, ps_min=None,
                  ps_max=None, ip_min=None, ip_max=None, limit=50, format="json"):
        """
        Get NEO Earth impact risk assessment data.
        
        Args:
            spk (int or str, optional): Object SPK-ID.
            des (str, optional): Object designation.
            h_min (float, optional): Minimum absolute magnitude.
            h_max (float, optional): Maximum absolute magnitude.
            ps_min (float, optional): Minimum Palermo Scale.
            ps_max (float, optional): Maximum Palermo Scale.
            ip_min (float, optional): Minimum impact probability.
            ip_max (float, optional): Maximum impact probability.
            limit (int, optional): Maximum number of results. Default is 50.
            format (str, optional): Output format. Default is "json".
                
        Returns:
            dict: Impact risk assessment data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "spk": spk,
            "des": des,
            "h-min": h_min,
            "h-max": h_max,
            "ps-min": ps_min,
            "ps-max": ps_max,
            "ip-min": ip_min,
            "ip-max": ip_max,
            "limit": limit,
            "format": format
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("sentry.api"), params)
    
    def get_sbdb(self, spk=None, des=None, name=None, neo=None, pha=None, nea=None,
                comet=None, kind=None, mb=None, tro=None, cen=None, tno=None,
                fullname=False, format="json"):
        """
        Get Small-Body Database data.
        
        Args:
            spk (int or str, optional): Object SPK-ID.
            des (str, optional): Object designation.
            name (str, optional): Object name.
            neo (bool, optional): Near-Earth Object filter.
            pha (bool, optional): Potentially Hazardous Asteroid filter.
            nea (bool, optional): Near-Earth Asteroid filter.
            comet (bool, optional): Comet filter.
            kind (str, optional): Object kind filter (a=asteroid, c=comet).
            mb (bool, optional): Main-belt Asteroid filter.
            tro (bool, optional): Trojan Asteroid filter.
            cen (bool, optional): Centaur filter.
            tno (bool, optional): Trans-Neptunian Object filter.
            fullname (bool, optional): Show full object names. Default is False.
            format (str, optional): Output format. Default is "json".
                
        Returns:
            dict: Small-Body Database data.
                
        Raises:
            NASAAPIError: If the request fails or returns an error.
        """
        params = {
            "spk": spk,
            "des": des,
            "name": name,
            "neo": neo,
            "pha": pha,
            "nea": nea,
            "comet": comet,
            "kind": kind,
            "mb": mb,
            "tro": tro,
            "cen": cen,
            "tno": tno,
            "fullname": fullname,
            "format": format
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("sbdb.api"), params)
