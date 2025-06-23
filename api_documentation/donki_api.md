# DONKI: Space Weather Database Of Notifications, Knowledge, Information API

## Overview
The Space Weather Database Of Notifications, Knowledge, Information (DONKI) is a comprehensive online tool for space weather forecasters, scientists, and the general space science community. DONKI chronicles daily interpretations of space weather observations, analysis, models, forecasts, and notifications provided by the Space Weather Research Center (SWRC). It offers comprehensive knowledge-base search functionality to support anomaly resolution and space science research, intelligent linkages, relationships, cause-and-effects between space weather activities, and API access to information stored in the database.

## API Components

### 1. Coronal Mass Ejection (CME)

#### Endpoint
`GET https://api.nasa.gov/DONKI/CME`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `startDate` | YYYY-MM-DD | 30 days prior to current UTC date | Start date for data query |
| `endDate` | YYYY-MM-DD | Current UTC date | End date for data query |
| `api_key` | string | DEMO_KEY | api.nasa.gov key for expanded usage |

#### Example Request
```
GET https://api.nasa.gov/DONKI/CME?startDate=2017-01-01&endDate=2017-01-30&api_key=DEMO_KEY
```

### 2. Coronal Mass Ejection (CME) Analysis

#### Endpoint
`GET https://api.nasa.gov/DONKI/CMEAnalysis`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `startDate` | YYYY-MM-DD | 30 days prior to current UTC date | Start date for data query |
| `endDate` | YYYY-MM-DD | Current UTC date | End date for data query |
| `mostAccurateOnly` | boolean | false | Filter for most accurate results only |
| `speed` | integer | null | Filter by speed (km/s) |
| `halfAngle` | integer | null | Filter by half angle |
| `catalog` | string | null | Filter by catalog |
| `api_key` | string | DEMO_KEY | api.nasa.gov key for expanded usage |

#### Example Request
```
GET https://api.nasa.gov/DONKI/CMEAnalysis?startDate=2016-09-01&endDate=2016-09-30&mostAccurateOnly=true&speed=500&halfAngle=30&catalog=ALL&api_key=DEMO_KEY
```

### 3. Geomagnetic Storm (GST)

#### Endpoint
`GET https://api.nasa.gov/DONKI/GST`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `startDate` | YYYY-MM-DD | 30 days prior to current UTC date | Start date for data query |
| `endDate` | YYYY-MM-DD | Current UTC date | End date for data query |
| `api_key` | string | DEMO_KEY | api.nasa.gov key for expanded usage |

#### Example Request
```
GET https://api.nasa.gov/DONKI/GST?startDate=2017-01-01&endDate=2017-01-30&api_key=DEMO_KEY
```

### 4. Interplanetary Shock (IPS)

#### Endpoint
`GET https://api.nasa.gov/DONKI/IPS`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `startDate` | YYYY-MM-DD | 30 days prior to current UTC date | Start date for data query |
| `endDate` | YYYY-MM-DD | Current UTC date | End date for data query |
| `location` | string | null | Filter by location |
| `catalog` | string | null | Filter by catalog |
| `api_key` | string | DEMO_KEY | api.nasa.gov key for expanded usage |

#### Example Request
```
GET https://api.nasa.gov/DONKI/IPS?startDate=2017-01-01&endDate=2017-01-30&location=LOCATION&catalog=CATALOG&api_key=DEMO_KEY
```

### 5. Solar Flare (FLR)

#### Endpoint
`GET https://api.nasa.gov/DONKI/FLR`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `startDate` | YYYY-MM-DD | 30 days prior to current UTC date | Start date for data query |
| `endDate` | YYYY-MM-DD | Current UTC date | End date for data query |
| `api_key` | string | DEMO_KEY | api.nasa.gov key for expanded usage |

#### Example Request
```
GET https://api.nasa.gov/DONKI/FLR?startDate=2017-01-01&endDate=2017-01-30&api_key=DEMO_KEY
```

### 6. Solar Energetic Particle (SEP)

#### Endpoint
`GET https://api.nasa.gov/DONKI/SEP`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `startDate` | YYYY-MM-DD | 30 days prior to current UTC date | Start date for data query |
| `endDate` | YYYY-MM-DD | Current UTC date | End date for data query |
| `api_key` | string | DEMO_KEY | api.nasa.gov key for expanded usage |

#### Example Request
```
GET https://api.nasa.gov/DONKI/SEP?startDate=2017-01-01&endDate=2017-01-30&api_key=DEMO_KEY
```

### 7. Magnetopause Crossing (MPC)

#### Endpoint
`GET https://api.nasa.gov/DONKI/MPC`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `startDate` | YYYY-MM-DD | 30 days prior to current UTC date | Start date for data query |
| `endDate` | YYYY-MM-DD | Current UTC date | End date for data query |
| `api_key` | string | DEMO_KEY | api.nasa.gov key for expanded usage |

#### Example Request
```
GET https://api.nasa.gov/DONKI/MPC?startDate=2017-01-01&endDate=2017-01-30&api_key=DEMO_KEY
```

## Response Format
All DONKI API endpoints return data in JSON format with specific fields relevant to each space weather event type. Common fields include:

- Event time and date
- Event catalog information
- Observational data
- Analysis results
- Related events
- Source information

## Usage Notes
- The default date range is the 30 days prior to the current UTC date
- All date parameters must be in YYYY-MM-DD format
- Some endpoints offer additional filtering options for more specific queries
- The API is subject to the standard rate limits of api.nasa.gov (1,000 requests per hour for registered API keys)
- DONKI data is particularly valuable for researchers studying space weather phenomena and their effects on Earth and space systems
