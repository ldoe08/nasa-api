# EPIC: Earth Polychromatic Imaging Camera API

## Overview
The EPIC (Earth Polychromatic Imaging Camera) API provides access to the daily imagery collected by DSCOVR's Earth Polychromatic Imaging Camera instrument. Uniquely positioned at the Earth-Sun Lagrange point, EPIC provides full disc imagery of the Earth and captures unique perspectives of certain astronomical events such as lunar transits.

## Technical Specifications
- Camera: 2048x2048 pixel CCD (Charge Coupled Device) detector
- Optics: 30-cm aperture Cassegrain telescope
- Position: Earth-Sun Lagrange point (L1)

## API Documentation

### Base URL
`https://api.nasa.gov/EPIC/api`

### Endpoints

#### 1. Natural Images

##### Endpoint
`GET https://api.nasa.gov/EPIC/api/natural`

##### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `api_key` | string | DEMO_KEY | Your API key |
| `date` | YYYY-MM-DD | most recent | Date of image collection |

##### Example Request
```
GET https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY
```

#### 2. Natural Images by Date

##### Endpoint
`GET https://api.nasa.gov/EPIC/api/natural/date/{date}`

##### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `date` | YYYY-MM-DD | required | Date of image collection |
| `api_key` | string | DEMO_KEY | Your API key |

##### Example Request
```
GET https://api.nasa.gov/EPIC/api/natural/date/2019-05-30?api_key=DEMO_KEY
```

#### 3. Available Dates

##### Endpoint
`GET https://api.nasa.gov/EPIC/api/natural/available`

##### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `api_key` | string | DEMO_KEY | Your API key |

##### Example Request
```
GET https://api.nasa.gov/EPIC/api/natural/available?api_key=DEMO_KEY
```

#### 4. Enhanced Images

##### Endpoint
`GET https://api.nasa.gov/EPIC/api/enhanced`

##### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `api_key` | string | DEMO_KEY | Your API key |

##### Example Request
```
GET https://api.nasa.gov/EPIC/api/enhanced?api_key=DEMO_KEY
```

#### 5. Enhanced Images by Date

##### Endpoint
`GET https://api.nasa.gov/EPIC/api/enhanced/date/{date}`

##### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `date` | YYYY-MM-DD | required | Date of image collection |
| `api_key` | string | DEMO_KEY | Your API key |

##### Example Request
```
GET https://api.nasa.gov/EPIC/api/enhanced/date/2019-05-30?api_key=DEMO_KEY
```

#### 6. Available Dates for Enhanced Images

##### Endpoint
`GET https://api.nasa.gov/EPIC/api/enhanced/available`

##### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `api_key` | string | DEMO_KEY | Your API key |

##### Example Request
```
GET https://api.nasa.gov/EPIC/api/enhanced/available?api_key=DEMO_KEY
```

### Image Retrieval

After getting the metadata from the API, you can construct the image URL using the following pattern:

```
https://api.nasa.gov/EPIC/archive/{collection}/{year}/{month}/{day}/png/{image}.png?api_key=YOUR_API_KEY
```

Where:
- `collection` is either "natural" or "enhanced"
- `year`, `month`, and `day` are from the date of the image
- `image` is the image name returned in the metadata

## Retrievable Metadata
The following information is available for every image in the collection:

- Image name
- Date
- Caption
- centroid_coordinates
- dscovr_j2000_position
- lunar_j2000_position
- sun_j2000_position
- attitude_quaternions

## Response Format

```json
[
  {
    "identifier": "20230701003634",
    "caption": "This image was taken by NASA's EPIC camera onboard the NOAA DSCOVR spacecraft",
    "image": "epic_1b_20230701003634",
    "version": "03",
    "centroid_coordinates": {
      "lat": -4.272705,
      "lon": 159.748675
    },
    "dscovr_j2000_position": {
      "x": -1283061.023029,
      "y": -669893.40206,
      "z": -130240.863957
    },
    "lunar_j2000_position": {
      "x": -47244.025488,
      "y": -366810.98824,
      "z": -108806.563685
    },
    "sun_j2000_position": {
      "x": 121887926.96418,
      "y": -83410533.334285,
      "z": -36159937.252826
    },
    "attitude_quaternions": {
      "q0": -0.308502,
      "q1": -0.119342,
      "q2": 0.210556,
      "q3": 0.919914
    },
    "date": "2023-07-01 00:32:45",
    "coords": {
      "centroid_coordinates": {
        "lat": -4.272705,
        "lon": 159.748675
      },
      "dscovr_j2000_position": {
        "x": -1283061.023029,
        "y": -669893.40206,
        "z": -130240.863957
      },
      "lunar_j2000_position": {
        "x": -47244.025488,
        "y": -366810.98824,
        "z": -108806.563685
      },
      "sun_j2000_position": {
        "x": 121887926.96418,
        "y": -83410533.334285,
        "z": -36159937.252826
      },
      "attitude_quaternions": {
        "q0": -0.308502,
        "q1": -0.119342,
        "q2": 0.210556,
        "q3": 0.919914
      }
    }
  }
]
```

## Usage Notes
- The EPIC API provides both "natural" and "enhanced" color imagery
- Natural images show the Earth as humans would see it from space
- Enhanced images use scientific algorithms to highlight certain features
- Images are available as full-disc views of the Earth
- The API is particularly useful for tracking global weather patterns, cloud formations, and major events visible from space
- Development of the EPIC API began in 2015 and is supported by the Laboratory for Atmospheres in the Earth Sciences Division of the Goddard Space Flight Center
- More information and direct access to imagery is available on the [EPIC website](https://epic.gsfc.nasa.gov/)
- The API is subject to the standard rate limits of api.nasa.gov (1,000 requests per hour for registered API keys)

## Additional Resources
- [EPIC Website](https://epic.gsfc.nasa.gov/)
- [Laboratory for Atmospheres](https://atmospheres.gsfc.nasa.gov/)
