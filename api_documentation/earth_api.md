# Earth API

## Overview
The Earth API provides access to NASA's vast collection of Earth observation imagery data. This API allows developers to tap into the significant public investment in earth observation data, particularly Landsat satellite imagery. According to industry reports, Landsat satellite imagery data provides an estimated $2.19 billion in annual economic value, far exceeding the cost of building, launching, and managing the satellites and sensors.

## Data Sources
The Earth API connects to multiple data sources and services:

1. **Landsat Imagery**: Joint project between NASA and USGS
2. **NASA's Earth Science Division**: Various Earth imagery APIs for developers
3. **GIBS** (Global Imagery Browse Services): API for accessing satellite imagery
4. **Google Earth Engine API**: Provides access to pan-sharpened Landsat 8 imagery

## Endpoints

### 1. Earth Imagery

#### Endpoint
`GET https://api.nasa.gov/planetary/earth/imagery`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `lat` | float | None | Latitude of the imagery location (required) |
| `lon` | float | None | Longitude of the imagery location (required) |
| `date` | YYYY-MM-DD | today | Date of the imagery (optional) |
| `dim` | float | 0.025 | Width and height of image in degrees (optional) |
| `cloud_score` | boolean | false | Calculate the percentage of the image covered by clouds (optional) |
| `api_key` | string | DEMO_KEY | api.nasa.gov key for expanded usage |

#### Example Request
```
GET https://api.nasa.gov/planetary/earth/imagery?lon=100.75&lat=1.5&date=2014-02-01&dim=0.15&api_key=DEMO_KEY
```

### 2. Earth Assets

#### Endpoint
`GET https://api.nasa.gov/planetary/earth/assets`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `lat` | float | None | Latitude of the imagery location (required) |
| `lon` | float | None | Longitude of the imagery location (required) |
| `begin` | YYYY-MM-DD | None | Beginning of date range (optional) |
| `end` | YYYY-MM-DD | today | End of date range (optional) |
| `api_key` | string | DEMO_KEY | api.nasa.gov key for expanded usage |

#### Example Request
```
GET https://api.nasa.gov/planetary/earth/assets?lon=100.75&lat=1.5&begin=2014-02-01&end=2014-02-05&api_key=DEMO_KEY
```

## Response Format

### Earth Imagery Response
The response is an image file (typically JPEG or PNG) of the requested location. If `cloud_score=true` is specified, the API also returns a JSON object with the calculated cloud score.

### Earth Assets Response
```json
{
  "count": 5,
  "results": [
    {
      "date": "2014-02-04T03:30:01",
      "id": "LC8_L1T_TOA/LC81270592014035LGN00",
      "resource": {
        "dataset": "LC8_L1T_TOA",
        "planet": "earth"
      },
      "service_version": "v1",
      "url": "https://earthengine.googleapis.com/api/thumb?thumbid=..."
    },
    ...
  ]
}
```

## Usage Notes
- The Earth API provides a simple way to access Landsat imagery data
- For more complex applications, consider using the Earthdata Developer Portal or GIBS
- The Google Earth Engine API integration currently only supports pan-sharpened Landsat 8 imagery
- Cloud score calculation can be useful for filtering out heavily clouded images
- The API is subject to the standard rate limits of api.nasa.gov (1,000 requests per hour for registered API keys)
- For building more sophisticated models with satellite imagery, apply machine learning techniques or use the more advanced APIs available through NASA's Earth Science Division

## Additional Resources
- [Earthdata Developer Portal](https://developer.earthdata.nasa.gov/)
- [GIBS (Global Imagery Browse Services)](https://earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/gibs)
- [Google Earth Engine API](https://developers.google.com/earth-engine/)
