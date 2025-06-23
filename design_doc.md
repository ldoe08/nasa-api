# NASA Universal API Tool - Design Document

## Overview
The NASA Universal API Tool is a comprehensive Python library designed to provide a unified interface to all NASA APIs. This tool will allow users to access NASA's diverse data sources through a consistent, easy-to-use interface while handling authentication, request formatting, and response parsing.

## Design Goals
1. **Unified Interface**: Provide a consistent interface across all NASA APIs
2. **Modularity**: Each API should be encapsulated in its own module
3. **Extensibility**: Easy to add new APIs or endpoints as NASA expands their offerings
4. **Authentication**: Simple API key management
5. **Error Handling**: Comprehensive error handling and informative messages
6. **Documentation**: Clear documentation and examples for each API
7. **Cross-platform**: Work on all major operating systems

## Architecture

### Core Components

#### 1. Client Class
The main entry point for the library, handling authentication and providing access to all API modules.

```
NASAClient
├── API Key Management
├── Rate Limiting
├── Error Handling
└── API Module Access
```

#### 2. API Modules
Individual modules for each NASA API, encapsulating the specific endpoints and functionality.

```
APIModule (Base Class)
├── APOD Module
├── Asteroids NeoWs Module
├── DONKI Module
├── Earth Module
├── EONET Module
├── EPIC Module
├── Exoplanet Module
├── Open Science Data Repository Module
├── InSight Module
├── Mars Rover Photos Module
├── NASA Image and Video Library Module
├── TechTransfer Module
├── Satellite Situation Center Module
└── SSD/CNEOS Module
```

#### 3. Request Handler
Handles HTTP requests, including formatting, sending, and receiving responses.

```
RequestHandler
├── Request Formatting
├── HTTP Methods (GET, POST, etc.)
├── Response Parsing
└── Error Handling
```

#### 4. Response Models
Data models for structured API responses.

```
ResponseModel (Base Class)
├── APOD Response
├── Asteroids Response
└── ... (other API-specific responses)
```

### Class Diagram

```
+----------------+       +----------------+       +----------------+
|   NASAClient   |------>|   APIModule    |------>| RequestHandler |
+----------------+       +----------------+       +----------------+
        |                        |                        |
        |                        |                        |
        v                        v                        v
+----------------+       +----------------+       +----------------+
| Authentication |       | Specific APIs  |       | ResponseModel  |
+----------------+       +----------------+       +----------------+
```

## Implementation Details

### NASAClient Class
```python
class NASAClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or "DEMO_KEY"
        self.request_handler = RequestHandler(self.api_key)
        
        # Initialize API modules
        self.apod = APODModule(self.request_handler)
        self.asteroids = AsteroidsModule(self.request_handler)
        # ... other modules
    
    def set_api_key(self, api_key):
        self.api_key = api_key
        self.request_handler.api_key = api_key
```

### APIModule Base Class
```python
class APIModule:
    def __init__(self, request_handler):
        self.request_handler = request_handler
        self.base_url = "https://api.nasa.gov/"
    
    def _build_url(self, endpoint):
        return f"{self.base_url}{endpoint}"
```

### Example Specific API Module
```python
class APODModule(APIModule):
    def __init__(self, request_handler):
        super().__init__(request_handler)
        self.base_url = "https://api.nasa.gov/planetary/"
    
    def get_astronomy_picture(self, date=None, start_date=None, end_date=None, count=None, thumbs=False):
        params = {
            "date": date,
            "start_date": start_date,
            "end_date": end_date,
            "count": count,
            "thumbs": thumbs
        }
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self.request_handler.get(self._build_url("apod"), params)
```

### RequestHandler Class
```python
class RequestHandler:
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()
    
    def get(self, url, params=None):
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
```

### Custom Exception Class
```python
class NASAAPIError(Exception):
    """Exception raised for NASA API errors."""
    pass
```

## File Structure
```
nasa_api_tool/
├── __init__.py
├── client.py           # NASAClient class
├── exceptions.py       # Custom exceptions
├── request_handler.py  # RequestHandler class
├── models/             # Response models
│   ├── __init__.py
│   ├── apod.py
│   ├── asteroids.py
│   └── ...
└── apis/               # API modules
    ├── __init__.py
    ├── apod.py
    ├── asteroids.py
    └── ...
```

## Usage Examples

### Basic Usage
```python
from nasa_api_tool import NASAClient

# Initialize with demo key
client = NASAClient()

# Or with your own API key
client = NASAClient(api_key="YOUR_API_KEY")

# Get today's astronomy picture
apod = client.apod.get_astronomy_picture()
print(f"Title: {apod['title']}")
print(f"URL: {apod['url']}")

# Get Mars Rover photos
photos = client.mars_rover.get_photos(rover="curiosity", sol=1000)
for photo in photos['photos'][:5]:
    print(f"Photo ID: {photo['id']}, Camera: {photo['camera']['full_name']}")
```

### Advanced Usage
```python
# Search for near-Earth objects
neo_data = client.asteroids.get_feed(start_date="2023-01-01", end_date="2023-01-07")
print(f"Found {neo_data['element_count']} near-Earth objects")

# Get Earth imagery
earth_image = client.earth.get_imagery(lat=36.098592, lon=-112.097796, date="2018-01-01")
print(f"Earth image URL: {earth_image['url']}")

# Get EPIC imagery
epic_images = client.epic.get_images(date="2021-06-15")
for image in epic_images[:3]:
    print(f"Image name: {image['image']}, Date: {image['date']}")
```

## Error Handling
```python
from nasa_api_tool import NASAClient, NASAAPIError

client = NASAClient()

try:
    # Try with invalid parameters
    apod = client.apod.get_astronomy_picture(date="invalid-date")
except NASAAPIError as e:
    print(f"Error: {e}")
```

## Next Steps
1. Implement the core client class
2. Develop the request handler with error handling
3. Create base API module class
4. Implement individual API modules
5. Add comprehensive documentation and examples
6. Create unit tests for all components
7. Package the library for distribution
