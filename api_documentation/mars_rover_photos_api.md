# Mars Rover Photos API

## Overview
The Mars Rover Photos API is designed to collect image data gathered by NASA's Curiosity, Opportunity, and Spirit rovers on Mars and make it more easily available to developers, educators, and citizen scientists. This API provides access to the raw and processed images captured by various cameras on these Mars rovers.

## Data Organization
- Each rover has its own set of photos stored in the database, which can be queried separately
- Photos are organized by the sol (Martian rotation or day) on which they were taken, counting up from the rover's landing date
- Photos can also be searched by Earth date

## Endpoint

### Get Photos
`GET https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `rover` | string | required | Rover name (curiosity, opportunity, spirit) |
| `sol` | integer | none | Martian sol (day) of the rover's mission |
| `earth_date` | YYYY-MM-DD | none | Earth date in format YYYY-MM-DD |
| `camera` | string | all | Filter by camera type (see camera list below) |
| `page` | integer | 1 | Page number (25 photos per page) |
| `api_key` | string | DEMO_KEY | Your API key |

**Note**: Either `sol` or `earth_date` must be provided, but not both.

#### Example Requests
```
GET https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY
GET https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?earth_date=2015-6-3&api_key=DEMO_KEY
GET https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY
```

### Get Rover Information
`GET https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `rover` | string | required | Rover name (curiosity, opportunity, spirit) |
| `api_key` | string | DEMO_KEY | Your API key |

#### Example Request
```
GET https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity?api_key=DEMO_KEY
```

### Get All Rovers
`GET https://api.nasa.gov/mars-photos/api/v1/rovers`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `api_key` | string | DEMO_KEY | Your API key |

#### Example Request
```
GET https://api.nasa.gov/mars-photos/api/v1/rovers?api_key=DEMO_KEY
```

## Rover Cameras

Each rover has a unique set of cameras with different perspectives and functions:

| Abbreviation | Camera | Curiosity | Opportunity | Spirit |
|--------------|--------|-----------|-------------|--------|
| FHAZ | Front Hazard Avoidance Camera | ✓ | ✓ | ✓ |
| RHAZ | Rear Hazard Avoidance Camera | ✓ | ✓ | ✓ |
| MAST | Mast Camera | ✓ | | |
| CHEMCAM | Chemistry and Camera Complex | ✓ | | |
| MAHLI | Mars Hand Lens Imager | ✓ | | |
| MARDI | Mars Descent Imager | ✓ | | |
| NAVCAM | Navigation Camera | ✓ | ✓ | ✓ |
| PANCAM | Panoramic Camera | | ✓ | ✓ |
| MINITES | Miniature Thermal Emission Spectrometer | | ✓ | ✓ |

## Response Format

### Photos Response
```json
{
  "photos": [
    {
      "id": 102693,
      "sol": 1000,
      "camera": {
        "id": 20,
        "name": "FHAZ",
        "rover_id": 5,
        "full_name": "Front Hazard Avoidance Camera"
      },
      "img_src": "http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FLB_486265257EDR_F0481570FHAZ00323M_.JPG",
      "earth_date": "2015-05-30",
      "rover": {
        "id": 5,
        "name": "Curiosity",
        "landing_date": "2012-08-06",
        "launch_date": "2011-11-26",
        "status": "active"
      }
    },
    // More photos...
  ]
}
```

### Rover Response
```json
{
  "rover": {
    "id": 5,
    "name": "Curiosity",
    "landing_date": "2012-08-06",
    "launch_date": "2011-11-26",
    "status": "active",
    "max_sol": 3452,
    "max_date": "2022-01-09",
    "total_photos": 567808,
    "cameras": [
      {
        "name": "FHAZ",
        "full_name": "Front Hazard Avoidance Camera"
      },
      // More cameras...
    ]
  }
}
```

## Usage Notes
- Responses are limited to 25 photos per call
- Queries that would return more than 25 photos are split into multiple pages
- Add a `page` parameter to access additional pages of results
- Each camera has a unique function and perspective
- Not all rovers have the same cameras
- The API is subject to the standard rate limits of api.nasa.gov (1,000 requests per hour for registered API keys)
- This API is maintained by Chris Cerami and is one of NASA's most popular APIs for educational purposes
