# NASA Universal API Tool - User Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [API Modules](#api-modules)
   - [APOD (Astronomy Picture of the Day)](#apod-astronomy-picture-of-the-day)
   - [Asteroids NeoWs (Near Earth Object Web Service)](#asteroids-neows-near-earth-object-web-service)
   - [DONKI (Space Weather Database)](#donki-space-weather-database)
   - [Earth](#earth)
   - [EONET (Earth Observatory Natural Event Tracker)](#eonet-earth-observatory-natural-event-tracker)
   - [EPIC (Earth Polychromatic Imaging Camera)](#epic-earth-polychromatic-imaging-camera)
   - [Exoplanet Archive](#exoplanet-archive)
   - [InSight: Mars Weather Service](#insight-mars-weather-service)
   - [Mars Rover Photos](#mars-rover-photos)
   - [NASA Image and Video Library](#nasa-image-and-video-library)
   - [TechTransfer](#techtransfer)
   - [Satellite Situation Center](#satellite-situation-center)
   - [SSD/CNEOS (Solar System Dynamics)](#ssdcneos-solar-system-dynamics)
5. [Error Handling](#error-handling)
6. [Best Practices](#best-practices)
7. [Troubleshooting](#troubleshooting)
8. [API Key Management](#api-key-management)
9. [Examples](#examples)

## Introduction

The NASA Universal API Tool is a comprehensive Python library that provides a unified interface to access NASA's various APIs. This tool simplifies the process of retrieving data from NASA's rich collection of space and Earth science datasets, allowing researchers, developers, and space enthusiasts to easily incorporate NASA data into their projects.

This user guide provides detailed instructions on how to use the NASA Universal API Tool, including installation, basic usage, and examples for each supported API.

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation Steps

1. Clone the repository or download the package:
```bash
git clone https://github.com/yourusername/nasa-api-tool.git
cd nasa-api-tool
```

2. Install the package:
```bash
pip install -e .
```

Alternatively, you can install directly from the directory:
```bash
cd /path/to/nasa_api_project
pip install -e .
```

## Getting Started

### Obtaining a NASA API Key

While many NASA APIs can be accessed using a demo key with limited rate restrictions, it's recommended to obtain your own API key for production use:

1. Visit [https://api.nasa.gov/](https://api.nasa.gov/)
2. Fill out the form to sign up for an API key
3. Your API key will be emailed to you

### Basic Usage

Here's a simple example to get started with the NASA Universal API Tool:

```python
from nasa_api_tool import NASAClient

# Initialize the client with your API key
client = NASAClient(api_key="YOUR_API_KEY")

# Get today's Astronomy Picture of the Day
apod = client.apod.get_astronomy_picture()
print(f"Title: {apod['title']}")
print(f"URL: {apod['url']}")
print(f"Explanation: {apod['explanation']}")
```

If you don't provide an API key, the tool will use "DEMO_KEY" by default, which has stricter rate limits.

## API Modules

The NASA Universal API Tool provides access to the following NASA APIs:

### APOD (Astronomy Picture of the Day)

The APOD API provides the Astronomy Picture of the Day, along with a brief explanation written by a professional astronomer.

#### Methods

- `get_astronomy_picture(date=None, start_date=None, end_date=None, count=None, thumbs=False)`

#### Examples

```python
# Get today's APOD
apod = client.apod.get_astronomy_picture()

# Get APOD for a specific date
apod = client.apod.get_astronomy_picture(date="2023-01-01")

# Get APODs for a date range
apods = client.apod.get_astronomy_picture(start_date="2023-01-01", end_date="2023-01-07")

# Get a random selection of APODs
apods = client.apod.get_astronomy_picture(count=5)

# Include thumbnail URLs for video content
apod = client.apod.get_astronomy_picture(thumbs=True)
```

### Asteroids NeoWs (Near Earth Object Web Service)

The Asteroids NeoWs API provides access to NASA's asteroid data, including close approaches to Earth.

#### Methods

- `get_feed(start_date=None, end_date=None)`
- `get_lookup(asteroid_id)`
- `get_browse(page=None, size=None)`

#### Examples

```python
# Get asteroids approaching Earth in the next 7 days (default)
asteroids = client.asteroids.get_feed()

# Get asteroids for a specific date range
asteroids = client.asteroids.get_feed(start_date="2023-01-01", end_date="2023-01-07")

# Look up a specific asteroid by ID
asteroid = client.asteroids.get_lookup("3542519")

# Browse the asteroid dataset
asteroids = client.asteroids.get_browse(page=0, size=20)
```

### DONKI (Space Weather Database)

The DONKI API provides access to space weather events such as solar flares, coronal mass ejections, and more.

#### Methods

- `get_coronal_mass_ejection(start_date=None, end_date=None)`
- `get_coronal_mass_ejection_analysis(start_date=None, end_date=None, most_accurate_only=None, speed=None, half_angle=None, catalog=None)`
- `get_geomagnetic_storm(start_date=None, end_date=None)`
- `get_interplanetary_shock(start_date=None, end_date=None, location=None, catalog=None)`
- `get_solar_flare(start_date=None, end_date=None)`
- `get_solar_energetic_particle(start_date=None, end_date=None)`
- `get_magnetopause_crossing(start_date=None, end_date=None)`
- `get_radiation_belt_enhancement(start_date=None, end_date=None)`
- `get_hss(start_date=None, end_date=None)`
- `get_wsa_enlil_simulation(start_date=None, end_date=None)`
- `get_notifications(start_date=None, end_date=None, type=None)`

#### Examples

```python
# Get coronal mass ejection data for the last 30 days (default)
cmes = client.donki.get_coronal_mass_ejection()

# Get solar flare data for a specific date range
flares = client.donki.get_solar_flare(start_date="2023-01-01", end_date="2023-01-31")

# Get geomagnetic storm data
storms = client.donki.get_geomagnetic_storm()

# Get notifications of various types
notifications = client.donki.get_notifications(type="all")
```

### Earth

The Earth API provides satellite imagery and asset metadata from NASA's Earth observation datasets.

#### Methods

- `get_imagery(lat, lon, date=None, dim=0.025, cloud_score=False)`
- `get_assets(lat, lon, date=None, dim=0.025)`

#### Examples

```python
# Get Landsat 8 imagery for a specific location (Grand Canyon)
imagery = client.earth.get_imagery(lat=36.098592, lon=-112.097796)
print(f"Image URL: {imagery['url']}")

# Get imagery for a specific date with cloud score
imagery = client.earth.get_imagery(
    lat=36.098592, 
    lon=-112.097796, 
    date="2020-01-01", 
    cloud_score=True
)

# Get a list of available imagery for a location
assets = client.earth.get_assets(lat=36.098592, lon=-112.097796)
```

### EONET (Earth Observatory Natural Event Tracker)

The EONET API provides information about natural events occurring around the world, such as wildfires, storms, and volcanic activity.

#### Methods

- `get_events(source=None, status=None, limit=None, days=None, category=None)`
- `get_categories()`
- `get_sources()`
- `get_layers()`

#### Examples

```python
# Get recent natural events
events = client.eonet.get_events()

# Get events with specific parameters
events = client.eonet.get_events(
    status="open",
    limit=10,
    days=30,
    category="wildfires"
)

# Get event categories
categories = client.eonet.get_categories()

# Get event sources
sources = client.eonet.get_sources()

# Get available web service layers
layers = client.eonet.get_layers()
```

### EPIC (Earth Polychromatic Imaging Camera)

The EPIC API provides imagery of Earth taken by the EPIC instrument aboard NOAA's DSCOVR spacecraft.

#### Methods

- `get_images(collection="natural", date=None)`
- `get_available_dates(collection="natural")`
- `get_image_url(image, collection="natural")`

#### Examples

```python
# Get the most recent EPIC images
images = client.epic.get_images()

# Get EPIC images for a specific date
images = client.epic.get_images(date="2023-01-01")

# Get enhanced color images
images = client.epic.get_images(collection="enhanced")

# Get available dates with EPIC imagery
dates = client.epic.get_available_dates()

# Get the URL for a specific image
if images:
    image_url = client.epic.get_image_url(images[0])
    print(f"Image URL: {image_url}")
```

### Exoplanet Archive

The Exoplanet Archive API provides access to NASA's database of confirmed exoplanets.

#### Methods

- `query(table="ps", select="*", where=None, order=None, format="json")`
- `get_confirmed_planets(limit=10, format="json")`
- `get_planet_by_name(planet_name, format="json")`
- `get_planets_in_habitable_zone(format="json")`

#### Examples

```python
# Get a list of confirmed exoplanets
planets = client.exoplanet.get_confirmed_planets(limit=20)

# Get data for a specific exoplanet
planet = client.exoplanet.get_planet_by_name("Kepler-186 f")

# Get exoplanets in the habitable zone
habitable_planets = client.exoplanet.get_planets_in_habitable_zone()

# Custom query
custom_query = client.exoplanet.query(
    table="ps",
    select="pl_name,hostname,discoverymethod,disc_year",
    where="disc_year>2020",
    order="disc_year desc"
)
```

### InSight: Mars Weather Service

The InSight API provides weather data from NASA's InSight Mars lander.

#### Methods

- `get_weather(version="1.0", feedtype="json")`

#### Examples

```python
# Get Mars weather data
try:
    weather = client.insight.get_weather()
    print(f"Mars weather data: {weather}")
except Exception as e:
    print(f"Note: InSight weather data may be unavailable: {e}")
```

Note: As of September 2020, the InSight lander is no longer returning weather data due to Mars solar conjunction. This API may return historical data or may be unavailable.

### Mars Rover Photos

The Mars Rover Photos API provides access to images taken by NASA's Mars rovers (Curiosity, Opportunity, Spirit, and Perseverance).

#### Methods

- `get_photos(rover, sol=None, earth_date=None, camera=None, page=1)`
- `get_rover_manifest(rover)`

#### Examples

```python
# Get photos from the Curiosity rover on sol 1000
photos = client.mars_rover.get_photos(rover="curiosity", sol=1000)

# Get photos from a specific date and camera
photos = client.mars_rover.get_photos(
    rover="perseverance",
    earth_date="2023-01-01",
    camera="NAVCAM"
)

# Get rover mission manifest
manifest = client.mars_rover.get_rover_manifest(rover="curiosity")
```

### NASA Image and Video Library

The NASA Image and Video Library API provides access to NASA's media assets, including images, videos, and audio files.

#### Methods

- `search(q=None, center=None, description=None, keywords=None, location=None, media_type=None, nasa_id=None, page=1, year_start=None, year_end=None)`
- `get_asset(nasa_id)`
- `get_metadata(nasa_id)`
- `get_captions(nasa_id)`

#### Examples

```python
# Search for Apollo 11 images
search_results = client.image_library.search(
    q="Apollo 11",
    media_type="image"
)

# Get asset information for a specific media item
if search_results.get('collection', {}).get('items'):
    nasa_id = search_results['collection']['items'][0]['data'][0]['nasa_id']
    asset = client.image_library.get_asset(nasa_id)
    
    # Get metadata for the media item
    metadata = client.image_library.get_metadata(nasa_id)
    
    # Get captions for a video
    try:
        captions = client.image_library.get_captions(nasa_id)
    except Exception as e:
        print(f"Captions not available: {e}")
```

### TechTransfer

The TechTransfer API provides access to NASA's patents, software, and technology spinoff descriptions.

#### Methods

- `get_patents(query=None)`
- `get_patent_issued(query=None)`
- `get_software(query=None)`
- `get_spinoff(query=None)`

#### Examples

```python
# Get NASA patent data
patents = client.tech_transfer.get_patents()

# Search for specific patents
patents = client.tech_transfer.get_patents(query="satellite")

# Get issued patents
issued_patents = client.tech_transfer.get_patent_issued()

# Get software data
software = client.tech_transfer.get_software()

# Get spinoff data
spinoffs = client.tech_transfer.get_spinoff()
```

### Satellite Situation Center

The Satellite Situation Center API provides spacecraft location information.

#### Methods

- `get_observatories()`
- `get_observatory_groups()`
- `get_locations(spacecraft, start_time, end_time, resolution)`
- `get_coordinate_systems()`
- `get_spase_observatories()`

#### Examples

```python
# Get a list of available spacecraft
observatories = client.ssc.get_observatories()

# Get predefined groups of spacecraft
groups = client.ssc.get_observatory_groups()

# Get spacecraft location data
locations = client.ssc.get_locations(
    spacecraft="ace",
    start_time="2023-01-01T00:00:00Z",
    end_time="2023-01-02T00:00:00Z",
    resolution=3600
)

# Get available coordinate systems
coordinate_systems = client.ssc.get_coordinate_systems()
```

### SSD/CNEOS (Solar System Dynamics)

The SSD/CNEOS API provides data about asteroids, comets, and near-Earth objects.

#### Methods

- `get_cad(date_min=None, date_max=None, dist_min=None, dist_max=None, h_min=None, h_max=None, v_inf_min=None, v_inf_max=None, v_rel_min=None, v_rel_max=None, class_filter=None, pha=None, nea=None, comet=None, neo=None, kind=None, spk=None, des=None, body=None, sort="date", limit=50, fullname=False, format="json")`
- `get_fireball(date_min=None, date_max=None, energy_min=None, energy_max=None, impact_e_min=None, impact_e_max=None, vel_min=None, vel_max=None, alt_min=None, alt_max=None, req_loc=None, limit=50, sort="date", format="json")`
- `get_sentry(spk=None, des=None, h_min=None, h_max=None, ps_min=None, ps_max=None, ip_min=None, ip_max=None, limit=50, format="json")`
- `get_sbdb(spk=None, des=None, name=None, neo=None, pha=None, nea=None, comet=None, kind=None, mb=None, tro=None, cen=None, tno=None, fullname=False, format="json")`

#### Examples

```python
# Get close-approach data for asteroids and comets
cad = client.ssd_cneos.get_cad()

# Get fireball event data
fireballs = client.ssd_cneos.get_fireball()

# Get NEO Earth impact risk assessment data
sentry = client.ssd_cneos.get_sentry()

# Get Small-Body Database data
sbdb = client.ssd_cneos.get_sbdb(neo=True, limit=10)
```

## Error Handling

The NASA Universal API Tool provides a custom exception class, `NASAAPIError`, for handling API-related errors. It's recommended to use try-except blocks to handle potential errors:

```python
from nasa_api_tool import NASAClient, NASAAPIError

client = NASAClient(api_key="YOUR_API_KEY")

try:
    apod = client.apod.get_astronomy_picture()
    print(f"Title: {apod['title']}")
except NASAAPIError as e:
    print(f"API Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

Common error types include:
- Bad request (400): Check your parameters
- Unauthorized (401): Check your API key
- Forbidden (403): You don't have access to this resource
- Not found (404): The requested resource doesn't exist
- Too many requests (429): You've exceeded your rate limit
- Server error (500+): NASA API is experiencing issues

## Best Practices

### API Key Management

1. **Store your API key securely**: Don't hardcode your API key in your source code. Use environment variables or a configuration file that's not committed to version control.

```python
import os
from nasa_api_tool import NASAClient

api_key = os.environ.get("NASA_API_KEY")
client = NASAClient(api_key=api_key)
```

2. **Use the demo key for testing**: During development, you can use the demo key by not providing an API key.

```python
client = NASAClient()  # Uses "DEMO_KEY" by default
```

### Rate Limiting

NASA APIs have rate limits. For the demo key:
- Hourly Limit: 30 requests per IP address per hour
- Daily Limit: 50 requests per IP address per day

For a registered API key:
- Hourly Limit: 1,000 requests per hour
- Daily Limit: 10,000 requests per day

To avoid hitting rate limits:
- Cache responses when appropriate
- Implement exponential backoff for retries
- Monitor your usage

### Data Processing

- Always check if the response contains the expected data before accessing it
- Handle empty results gracefully
- Consider using a data processing library like Pandas for large datasets

## Troubleshooting

### Common Issues

1. **API Key Issues**
   - Error: "Unauthorized: Check your API key"
   - Solution: Verify your API key is correct and has not expired

2. **Rate Limiting**
   - Error: "Too many requests: You've exceeded your rate limit"
   - Solution: Implement caching and rate limiting in your application

3. **Parameter Errors**
   - Error: "Bad request: Check your parameters"
   - Solution: Verify the parameters you're sending match the API requirements

4. **Data Availability**
   - Issue: Some APIs may not have data for certain dates or parameters
   - Solution: Implement proper error handling and provide fallbacks

### NASA Image and Video Library API Issues

The NASA Image and Video Library API may return a "Bad request" error when using certain search parameters. To resolve this:

- Ensure your search query is not empty
- Try using simpler search terms
- Avoid special characters in search queries
- Use only one or two search parameters at a time

## API Key Management

### Obtaining an API Key

1. Visit [https://api.nasa.gov/](https://api.nasa.gov/)
2. Fill out the form to sign up for an API key
3. Your API key will be emailed to you

### Using Your API Key

```python
from nasa_api_tool import NASAClient

# Initialize with your API key
client = NASAClient(api_key="YOUR_API_KEY")

# Change the API key later if needed
client.set_api_key("NEW_API_KEY")
```

### Securing Your API Key

To keep your API key secure:

1. Store it in an environment variable:
```python
import os
api_key = os.environ.get("NASA_API_KEY")
```

2. Use a configuration file that's not committed to version control:
```python
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['NASA']['API_KEY']
```

3. Use a secrets management service for production applications

## Examples

### Complete Example: Creating a Daily APOD Viewer

```python
import os
import requests
from datetime import datetime, timedelta
from nasa_api_tool import NASAClient, NASAAPIError

def download_image(url, save_path):
    """Download an image from a URL and save it to disk."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        return True
    return False

def get_apod_for_last_week():
    """Get and save APODs for the last 7 days."""
    # Get API key from environment variable or use demo key
    api_key = os.environ.get("NASA_API_KEY")
    client = NASAClient(api_key=api_key)
    
    # Calculate date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    
    try:
        # Get APODs for the last 7 days
        apods = client.apod.get_astronomy_picture(
            start_date=start_date.strftime("%Y-%m-%d"),
            end_date=end_date.strftime("%Y-%m-%d")
        )
        
        # Create directory for images if it doesn't exist
        os.makedirs("apod_images", exist_ok=True)
        
        # Process each APOD
        for apod in apods:
            date = apod.get('date')
            title = apod.get('title')
            explanation = apod.get('explanation')
            media_type = apod.get('media_type')
            
            print(f"Date: {date}")
            print(f"Title: {title}")
            print(f"Media Type: {media_type}")
            
            # Download image if it's an image
            if media_type == 'image':
                image_url = apod.get('url')
                save_path = f"apod_images/apod_{date}.jpg"
                
                if download_image(image_url, save_path):
                    print(f"Image saved to {save_path}")
                else:
                    print("Failed to download image")
            
            print("-" * 50)
        
        return True
    
    except NASAAPIError as e:
        print(f"API Error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    get_apod_for_last_week()
```

### Example: Tracking Near-Earth Objects

```python
from nasa_api_tool import NASAClient
from datetime import datetime, timedelta

def track_close_approaches():
    """Track asteroids that will make close approaches to Earth in the next 7 days."""
    client = NASAClient()
    
    # Get current date and date 7 days from now
    start_date = datetime.now().strftime("%Y-%m-%d")
    end_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    
    print(f"Tracking near-Earth objects from {start_date} to {end_date}")
    
    try:
        # Get asteroid feed
        neo_feed = client.asteroids.get_feed(start_date=start_date, end_date=end_date)
        
        # Print summary
        element_count = neo_feed.get('element_count', 0)
        print(f"Found {element_count} near-Earth objects")
        
        # Process each day
        for date, asteroids in neo_feed.get('near_earth_objects', {}).items():
            print(f"\nDate: {date}")
            print(f"Number of asteroids: {len(asteroids)}")
            
            # Find potentially hazardous asteroids
            hazardous = [a for a in asteroids if a.get('is_potentially_hazardous_asteroid')]
            print(f"Potentially hazardous: {len(hazardous)}")
            
            if hazardous:
                print("\nPotentially hazardous asteroids:")
                for asteroid in hazardous:
                    name = asteroid.get('name')
                    diameter_min = asteroid.get('estimated_diameter', {}).get('kilometers', {}).get('estimated_diameter_min')
                    diameter_max = asteroid.get('estimated_diameter', {}).get('kilometers', {}).get('estimated_diameter_max')
                    close_approach = asteroid.get('close_approach_data', [{}])[0]
                    miss_distance_km = close_approach.get('miss_distance', {}).get('kilometers')
                    relative_velocity = close_approach.get('relative_velocity', {}).get('kilometers_per_hour')
                    
                    print(f"  - {name}")
                    print(f"    Diameter: {diameter_min:.2f} to {diameter_max:.2f} km")
                    print(f"    Miss distance: {float(miss_distance_km):,.0f} km")
                    print(f"    Relative velocity: {float(relative_velocity):,.0f} km/h")
        
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    track_close_approaches()
```

### Example: Exploring Mars Rover Photos

```python
from nasa_api_tool import NASAClient
import os
import requests

def explore_mars_rover_photos():
    """Explore and download photos from Mars rovers."""
    client = NASAClient()
    
    # Get Curiosity rover manifest
    manifest = client.mars_rover.get_rover_manifest(rover="curiosity")
    rover_info = manifest.get('photo_manifest', {})
    
    print(f"Rover: {rover_info.get('name')}")
    print(f"Launch date: {rover_info.get('launch_date')}")
    print(f"Landing date: {rover_info.get('landing_date')}")
    print(f"Status: {rover_info.get('status')}")
    print(f"Total photos: {rover_info.get('total_photos')}")
    print(f"Most recent sol: {rover_info.get('max_sol')}")
    
    # Get photos from a specific sol
    sol = 1000
    print(f"\nGetting photos from sol {sol}...")
    
    photos = client.mars_rover.get_photos(rover="curiosity", sol=sol)
    photo_list = photos.get('photos', [])
    
    print(f"Found {len(photo_list)} photos")
    
    # Group photos by camera
    cameras = {}
    for photo in photo_list:
        camera = photo.get('camera', {}).get('name')
        if camera not in cameras:
            cameras[camera] = []
        cameras[camera].append(photo)
    
    print("\nPhotos by camera:")
    for camera, photos in cameras.items():
        print(f"  - {camera}: {len(photos)} photos")
    
    # Download a sample photo from each camera
    os.makedirs("mars_photos", exist_ok=True)
    
    for camera, photos in cameras.items():
        if photos:
            photo = photos[0]
            photo_id = photo.get('id')
            img_src = photo.get('img_src')
            
            print(f"\nDownloading sample photo from {camera} (ID: {photo_id})...")
            
            response = requests.get(img_src, stream=True)
            if response.status_code == 200:
                file_path = f"mars_photos/curiosity_sol{sol}_{camera}.jpg"
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                print(f"Saved to {file_path}")
            else:
                print("Failed to download image")
    
    return True

if __name__ == "__main__":
    explore_mars_rover_photos()
```

These examples demonstrate how to use the NASA Universal API Tool for various applications. You can adapt and extend them to suit your specific needs.
