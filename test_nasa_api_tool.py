"""
Test script for the NASA Universal API Tool.

This script tests the functionality of the NASA API tool with various NASA APIs.
"""

import os
import sys
import json
from datetime import datetime, timedelta

# Add the parent directory to the path so we can import the nasa_api_tool package
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nasa_api_tool import NASAClient, NASAAPIError

def test_apod():
    """Test the APOD API module."""
    print("\n=== Testing APOD API ===")
    
    try:
        # Initialize client with demo key
        client = NASAClient()
        
        # Get today's APOD
        print("Getting today's APOD...")
        apod = client.apod.get_astronomy_picture()
        print(f"Title: {apod.get('title', 'N/A')}")
        print(f"Date: {apod.get('date', 'N/A')}")
        print(f"Media type: {apod.get('media_type', 'N/A')}")
        
        # Get a specific date's APOD
        specific_date = "2023-01-01"
        print(f"\nGetting APOD for {specific_date}...")
        apod = client.apod.get_astronomy_picture(date=specific_date)
        print(f"Title: {apod.get('title', 'N/A')}")
        print(f"Date: {apod.get('date', 'N/A')}")
        
        # Get multiple APODs
        print("\nGetting 3 random APODs...")
        apods = client.apod.get_astronomy_picture(count=3)
        for i, apod in enumerate(apods):
            print(f"APOD {i+1} - Title: {apod.get('title', 'N/A')}, Date: {apod.get('date', 'N/A')}")
        
        print("\nAPOD API tests passed!")
        return True
    except NASAAPIError as e:
        print(f"Error testing APOD API: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error testing APOD API: {e}")
        return False

def test_asteroids():
    """Test the Asteroids NeoWs API module."""
    print("\n=== Testing Asteroids NeoWs API ===")
    
    try:
        # Initialize client with demo key
        client = NASAClient()
        
        # Get asteroid feed for a short date range (to avoid large responses)
        today = datetime.now().strftime("%Y-%m-%d")
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        
        print(f"Getting asteroid feed from {today} to {tomorrow}...")
        feed = client.asteroids.get_feed(start_date=today, end_date=tomorrow)
        
        element_count = feed.get('element_count', 0)
        print(f"Found {element_count} near-Earth objects")
        
        # If we have results, look up the first one
        if element_count > 0:
            neo_date = list(feed.get('near_earth_objects', {}).keys())[0]
            neo_list = feed['near_earth_objects'][neo_date]
            if neo_list:
                neo_id = neo_list[0]['id']
                neo_name = neo_list[0]['name']
                
                print(f"\nLooking up asteroid {neo_name} (ID: {neo_id})...")
                asteroid = client.asteroids.get_lookup(neo_id)
                print(f"Name: {asteroid.get('name', 'N/A')}")
                print(f"Absolute magnitude: {asteroid.get('absolute_magnitude_h', 'N/A')}")
        
        # Test browse endpoint
        print("\nBrowsing asteroid data (page 1, 5 items)...")
        browse = client.asteroids.get_browse(page=0, size=5)
        print(f"Total elements: {browse.get('page', {}).get('total_elements', 0)}")
        for i, neo in enumerate(browse.get('near_earth_objects', [])[:5]):
            print(f"NEO {i+1}: {neo.get('name', 'N/A')}")
        
        print("\nAsteroids NeoWs API tests passed!")
        return True
    except NASAAPIError as e:
        print(f"Error testing Asteroids NeoWs API: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error testing Asteroids NeoWs API: {e}")
        return False

def test_earth():
    """Test the Earth API module."""
    print("\n=== Testing Earth API ===")
    
    try:
        # Initialize client with demo key
        client = NASAClient()
        
        # Get imagery for a specific location (Grand Canyon)
        lat = 36.098592
        lon = -112.097796
        
        print(f"Getting Earth imagery for lat={lat}, lon={lon}...")
        try:
            imagery = client.earth.get_imagery(lat=lat, lon=lon)
            print(f"Image URL: {imagery.get('url', 'N/A')}")
            print(f"Date: {imagery.get('date', 'N/A')}")
        except NASAAPIError as e:
            print(f"Note: Earth imagery retrieval failed: {e}")
            print("This is often due to cloud coverage or data availability.")
        
        # Get assets for the same location
        print(f"\nGetting Earth assets for lat={lat}, lon={lon}...")
        try:
            assets = client.earth.get_assets(lat=lat, lon=lon)
            print(f"Found {len(assets.get('results', []))} assets")
            if assets.get('results'):
                for i, asset in enumerate(assets['results'][:3]):
                    print(f"Asset {i+1} - Date: {asset.get('date', 'N/A')}")
        except NASAAPIError as e:
            print(f"Note: Earth assets retrieval failed: {e}")
            print("This is often due to data availability.")
        
        print("\nEarth API tests completed!")
        return True
    except NASAAPIError as e:
        print(f"Error testing Earth API: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error testing Earth API: {e}")
        return False

def test_mars_rover():
    """Test the Mars Rover Photos API module."""
    print("\n=== Testing Mars Rover Photos API ===")
    
    try:
        # Initialize client with demo key
        client = NASAClient()
        
        # Get Curiosity rover photos from sol 1000
        print("Getting Curiosity rover photos from sol 1000...")
        photos = client.mars_rover.get_photos(rover="curiosity", sol=1000, page=1)
        
        photo_count = len(photos.get('photos', []))
        print(f"Found {photo_count} photos")
        
        # Display info for the first few photos
        for i, photo in enumerate(photos.get('photos', [])[:3]):
            print(f"Photo {i+1} - ID: {photo.get('id', 'N/A')}, Camera: {photo.get('camera', {}).get('full_name', 'N/A')}")
        
        # Get rover manifest
        print("\nGetting Curiosity rover manifest...")
        manifest = client.mars_rover.get_rover_manifest(rover="curiosity")
        rover_info = manifest.get('photo_manifest', {})
        print(f"Rover name: {rover_info.get('name', 'N/A')}")
        print(f"Launch date: {rover_info.get('launch_date', 'N/A')}")
        print(f"Landing date: {rover_info.get('landing_date', 'N/A')}")
        print(f"Status: {rover_info.get('status', 'N/A')}")
        print(f"Total photos: {rover_info.get('total_photos', 'N/A')}")
        
        print("\nMars Rover Photos API tests passed!")
        return True
    except NASAAPIError as e:
        print(f"Error testing Mars Rover Photos API: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error testing Mars Rover Photos API: {e}")
        return False

def test_image_library():
    """Test the NASA Image and Video Library API module."""
    print("\n=== Testing NASA Image and Video Library API ===")
    
    try:
        # Initialize client with demo key
        client = NASAClient()
        
        # Search for Apollo 11 images
        print("Searching for Apollo 11 images...")
        search_results = client.image_library.search(q="Apollo 11", media_type="image")
        
        items = search_results.get('collection', {}).get('items', [])
        item_count = len(items)
        print(f"Found {item_count} items")
        
        # Display info for the first few items
        for i, item in enumerate(items[:3]):
            data = item.get('data', [{}])[0]
            print(f"Item {i+1} - Title: {data.get('title', 'N/A')}")
            print(f"  NASA ID: {data.get('nasa_id', 'N/A')}")
            print(f"  Date created: {data.get('date_created', 'N/A')}")
        
        # If we have results, get asset and metadata for the first one
        if item_count > 0:
            nasa_id = items[0].get('data', [{}])[0].get('nasa_id')
            if nasa_id:
                print(f"\nGetting asset for NASA ID: {nasa_id}...")
                asset = client.image_library.get_asset(nasa_id)
                asset_items = asset.get('collection', {}).get('items', [])
                if asset_items:
                    print(f"Asset URL: {asset_items[0].get('href', 'N/A')}")
                
                print(f"\nGetting metadata for NASA ID: {nasa_id}...")
                try:
                    metadata = client.image_library.get_metadata(nasa_id)
                    print(f"Metadata retrieved successfully")
                except NASAAPIError as e:
                    print(f"Note: Metadata retrieval failed: {e}")
        
        print("\nNASA Image and Video Library API tests passed!")
        return True
    except NASAAPIError as e:
        print(f"Error testing NASA Image and Video Library API: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error testing NASA Image and Video Library API: {e}")
        return False

def run_all_tests():
    """Run all API tests."""
    print("=== NASA Universal API Tool Tests ===")
    print(f"Starting tests at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    results = {
        "APOD": test_apod(),
        "Asteroids NeoWs": test_asteroids(),
        "Earth": test_earth(),
        "Mars Rover Photos": test_mars_rover(),
        "NASA Image and Video Library": test_image_library()
    }
    
    print("\n=== Test Results Summary ===")
    for api, passed in results.items():
        status = "PASSED" if passed else "FAILED"
        print(f"{api}: {status}")
    
    all_passed = all(results.values())
    print(f"\nOverall result: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    
    return all_passed

if __name__ == "__main__":
    run_all_tests()
