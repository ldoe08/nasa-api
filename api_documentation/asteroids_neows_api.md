# Asteroids NeoWs: Near Earth Object Web Service API

## Overview
The Near Earth Object Web Service (NeoWs) is a RESTful web service providing information about near-Earth asteroids. This API allows users to search for asteroids based on their closest approach date to Earth, look up specific asteroids using their NASA JPL small body ID, and browse the overall asteroid dataset.

## Data Source
All data is sourced from the NASA JPL Asteroid team (http://neo.jpl.nasa.gov/).

## Endpoints

### 1. Neo - Feed
Retrieves a list of asteroids based on their closest approach date to Earth.

#### Endpoint
`GET https://api.nasa.gov/neo/rest/v1/feed`

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `start_date` | YYYY-MM-DD | none | Starting date for asteroid search |
| `end_date` | YYYY-MM-DD | 7 days after start_date | Ending date for asteroid search |
| `api_key` | string | DEMO_KEY | api.nasa.gov key for expanded usage |

#### Example Request
```
GET https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY
```

#### Response Structure
The response includes:
- Links to related API calls
- Element count
- Near Earth Objects organized by date
- For each asteroid: ID, name, NASA JPL URL, estimated diameter, close approach data, and hazard assessment

### 2. Neo - Lookup
Lookup a specific asteroid based on its NASA JPL small body ID.

#### Endpoint
`GET https://api.nasa.gov/neo/rest/v1/neo/{asteroid_id}`

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `asteroid_id` | string | required | Asteroid SPK-ID |
| `api_key` | string | DEMO_KEY | api.nasa.gov key for expanded usage |

#### Example Request
```
GET https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=DEMO_KEY
```

### 3. Neo - Browse
Browse the overall dataset of near-Earth asteroids.

#### Endpoint
`GET https://api.nasa.gov/neo/rest/v1/neo/browse`

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page` | int | 0 | Page number (0-indexed) |
| `size` | int | 20 | Number of elements per page |
| `api_key` | string | DEMO_KEY | api.nasa.gov key for expanded usage |

#### Example Request
```
GET https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=DEMO_KEY
```

## Usage Notes
- The feed endpoint is limited to a date range of 7 days due to computational requirements
- For larger datasets, use the browse endpoint and paginate through results
- The API follows standard RESTful conventions and returns data in JSON format
- All asteroid data includes detailed information about size, orbit, and potential hazard assessment
- The API is subject to the standard rate limits of api.nasa.gov (1,000 requests per hour for registered API keys)

## Example Response (Abbreviated)
```json
{
  "links": {
    "next": "http://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-08&end_date=2015-09-09&detailed=false&api_key=DEMO_KEY",
    "prev": "http://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-06&end_date=2015-09-07&detailed=false&api_key=DEMO_KEY",
    "self": "http://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&detailed=false&api_key=DEMO_KEY"
  },
  "element_count": 24,
  "near_earth_objects": {
    "2015-09-08": [
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/3726710?api_key=DEMO_KEY"
        },
        "id": "3726710",
        "neo_reference_id": "3726710",
        "name": "(2015 RC)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3726710",
        "absolute_magnitude_h": 24.3,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0366906138,
            "estimated_diameter_max": 0.0820427065
          },
          "meters": {
            "estimated_diameter_min": 36.6906137531,
            "estimated_diameter_max": 82.0427064882
          }
        },
        "is_potentially_hazardous_asteroid": false,
        "close_approach_data": [
          {
            "close_approach_date": "2015-09-08",
            "epoch_date_close_approach": 1441695600000,
            "relative_velocity": {
              "kilometers_per_second": "19.4850295284",
              "kilometers_per_hour": "70146.1062021456",
              "miles_per_hour": "43586.0625062531"
            },
            "miss_distance": {
              "astronomical": "0.0269230459",
              "lunar": "10.4730644226",
              "kilometers": "4027630.5",
              "miles": "2502354.75"
            },
            "orbiting_body": "Earth"
          }
        ]
      }
    ]
  }
}
```
