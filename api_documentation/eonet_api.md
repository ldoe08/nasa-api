# EONET: Earth Observatory Natural Event Tracker API

## Overview
The Earth Observatory Natural Event Tracker (EONET) is a prototype web service that provides access to a curated source of continuously updated natural event metadata. EONET links these natural events to thematically-related web service-enabled image sources, allowing developers to access near real-time (NRT) imagery of natural events as they occur.

## Purpose and Background
As NASA makes more imagery available via web services (WMS, WMTS, etc.) in near real-time, EONET provides a structured way to access and utilize this data for monitoring natural events. The service was developed to address the need for a centralized API that provides a curated list of natural events and links to relevant imagery.

## Development
EONET was developed beginning in 2015 with support from NASA's Earth Observatory and the Earth Science Data and Information System (ESDIS) Project.

## API Documentation

### Base URL
`https://eonet.gsfc.nasa.gov/api/v3`

### Endpoints

#### 1. Events

##### Endpoint
`GET https://eonet.gsfc.nasa.gov/api/v3/events`

##### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `source` | string | all | Filter events by source |
| `status` | string | all | Filter by event status ('open', 'closed', 'all') |
| `limit` | integer | 50 | Number of events to retrieve (max 1000) |
| `days` | integer | 30 | Get events for the last n days |
| `start` | date | none | Start date for events (YYYY-MM-DD) |
| `end` | date | none | End date for events (YYYY-MM-DD) |
| `category` | string | all | Filter by event category ID |
| `bbox` | string | none | Filter by bounding box (min lon, min lat, max lon, max lat) |

##### Example Request
```
GET https://eonet.gsfc.nasa.gov/api/v3/events?limit=5&days=20&status=open
```

#### 2. Categories

##### Endpoint
`GET https://eonet.gsfc.nasa.gov/api/v3/categories`

##### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `source` | string | all | Filter categories by source |
| `status` | string | all | Filter by event status ('open', 'closed', 'all') |
| `limit` | integer | 50 | Number of categories to retrieve |
| `days` | integer | 30 | Get categories with events from the last n days |

##### Example Request
```
GET https://eonet.gsfc.nasa.gov/api/v3/categories
```

#### 3. Layers

##### Endpoint
`GET https://eonet.gsfc.nasa.gov/api/v3/layers`

##### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `category` | string | all | Filter layers by category ID |
| `source` | string | all | Filter layers by source |

##### Example Request
```
GET https://eonet.gsfc.nasa.gov/api/v3/layers/8
```

#### 4. Sources

##### Endpoint
`GET https://eonet.gsfc.nasa.gov/api/v3/sources`

##### Example Request
```
GET https://eonet.gsfc.nasa.gov/api/v3/sources
```

## Response Format

### Events Response
```json
{
  "title": "EONET Events",
  "description": "Natural events from EONET",
  "link": "https://eonet.gsfc.nasa.gov/api/v3/events",
  "events": [
    {
      "id": "EONET_5037",
      "title": "Tropical Storm Cristina",
      "description": null,
      "link": "https://eonet.gsfc.nasa.gov/api/v3/events/EONET_5037",
      "closed": null,
      "categories": [
        {
          "id": "severeStorms",
          "title": "Severe Storms"
        }
      ],
      "sources": [
        {
          "id": "GDACS",
          "url": "https://www.gdacs.org/Cyclones/report.aspx?eventid=1000722&eventtype=TC"
        },
        {
          "id": "NOAA_NHC",
          "url": "https://www.nhc.noaa.gov/archive/2020/CRISTINA.shtml"
        }
      ],
      "geometry": [
        {
          "magnitudeValue": 45,
          "magnitudeUnit": "kts",
          "date": "2020-07-10T18:00:00Z",
          "type": "Point",
          "coordinates": [-110.3, 16.6]
        }
      ]
    }
  ]
}
```

### Categories Response
```json
{
  "title": "EONET Event Categories",
  "description": "List of available event categories",
  "link": "https://eonet.gsfc.nasa.gov/api/v3/categories",
  "categories": [
    {
      "id": "drought",
      "title": "Drought",
      "link": "https://eonet.gsfc.nasa.gov/api/v3/categories/drought",
      "description": "Long lasting absence of precipitation affecting agriculture and livestock, and the overall availability of food and water.",
      "layers": "https://eonet.gsfc.nasa.gov/api/v3/layers/drought"
    }
  ]
}
```

## Usage Notes
- EONET is particularly useful for monitoring natural disasters and environmental events in near real-time
- The API can be integrated with mapping applications to visualize events geographically
- Events can be filtered by various parameters including category, status, and geographic location
- EONET links to NASA's Earth Observatory Worldview, allowing users to browse the entire globe daily and look for natural events as they occur
- The service is designed to be a prototype and may evolve over time
- No API key is required to access EONET, making it easily accessible for developers

## Related Resources
- [NASA EOSDIS' Worldview](https://worldview.earthdata.nasa.gov/)
- [NASA's Earth Observatory](https://earthobservatory.nasa.gov/)
- [Earth Science Data and Information System (ESDIS) Project](https://earthdata.nasa.gov/esdis)
