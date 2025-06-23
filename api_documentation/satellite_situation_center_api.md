# Satellite Situation Center API

## Overview
The Satellite Situation Center (SSCWeb) API provides a system to cast geocentric spacecraft location information into a framework of empirical geophysical regions. This API has been developed and is operated jointly by the NASA/GSFC Space Physics Data Facility (SPDF) and the National Space Science Data Center (NSSDC) to support NASA science programs and fulfill key international NASA responsibilities.

## Purpose
The SSCWeb API enables mission science planning (for both single missions and coordinated observations of multiple spacecraft) and subsequent multi-mission data analysis. It provides spacecraft location information within the context of Earth's magnetic field and other geophysical regions, which is crucial for space physics research and mission planning.

## Base URL
`https://sscweb.gsfc.nasa.gov/WS/sscr/2`

## API Documentation

### Endpoints

#### Get Observatories
`GET /observatories`

Returns a list of all available spacecraft (observatories) in the system.

#### Example Request
```
GET https://sscweb.gsfc.nasa.gov/WS/sscr/2/observatories
```

#### Get Observatory Groups
`GET /observatoryGroups`

Returns predefined groups of spacecraft.

#### Example Request
```
GET https://sscweb.gsfc.nasa.gov/WS/sscr/2/observatoryGroups
```

#### Get Locations
`GET /locations/{spacecraft}/{startTime},{endTime}/{resolution}`

Retrieves spacecraft location data for specified spacecraft, time range, and resolution.

##### Parameters
| Parameter | Description |
|-----------|-------------|
| `spacecraft` | Comma-separated list of spacecraft IDs |
| `startTime` | Start time in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ) |
| `endTime` | End time in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ) |
| `resolution` | Time resolution in seconds |

#### Example Request
```
GET https://sscweb.gsfc.nasa.gov/WS/sscr/2/locations/ace,wind/2020-01-01T00:00:00Z,2020-01-02T00:00:00Z/3600
```

#### Get Coordinate Systems
`GET /coordinateSystems`

Returns available coordinate systems for location data.

#### Example Request
```
GET https://sscweb.gsfc.nasa.gov/WS/sscr/2/coordinateSystems
```

#### Get Spacecraft Data
`GET /spaseObservatories`

Returns SPASE (Space Physics Archive Search and Extract) metadata for spacecraft.

#### Example Request
```
GET https://sscweb.gsfc.nasa.gov/WS/sscr/2/spaseObservatories
```

## Response Format
The API supports multiple response formats:

- JSON (default)
- XML
- CDF (Common Data Format)
- CSV (Comma-Separated Values)
- TSV (Tab-Separated Values)

To specify a format, use the appropriate Accept header or format parameter.

### Example JSON Response (Abbreviated)
```json
{
  "Result": {
    "StatusCode": 200,
    "StatusSubCode": "",
    "Data": [
      {
        "Id": "ace",
        "Name": "ACE",
        "StartTime": "1997-08-25T00:00:00.000Z",
        "EndTime": "2023-05-31T23:59:59.999Z",
        "Description": "Advanced Composition Explorer"
      },
      {
        "Id": "wind",
        "Name": "Wind",
        "StartTime": "1994-11-01T00:00:00.000Z",
        "EndTime": "2023-05-31T23:59:59.999Z",
        "Description": "Wind"
      }
    ]
  }
}
```

## Coordinate Systems
The API supports multiple coordinate systems for location data:

- GEI (Geocentric Equatorial Inertial)
- GEO (Geographic)
- GSE (Geocentric Solar Ecliptic)
- GSM (Geocentric Solar Magnetospheric)
- SM (Solar Magnetic)
- GNS (Geocentric Solar Magnetospheric)
- RTN (Radial-Tangential-Normal)

## Usage Notes
- The API does not require authentication
- Data is available for numerous spacecraft, including historical missions
- Location data can be provided in various coordinate systems
- Time ranges should be reasonable to avoid excessive data retrieval
- The API is particularly valuable for space physics research and mission planning
- For large data requests, consider using the CDF format for efficient data handling

## Additional Resources
- [Satellite Situation Center Web (SSCWeb) service](https://sscweb.gsfc.nasa.gov/)
- [NASA/GSFC Space Physics Data Facility (SPDF)](https://spdf.gsfc.nasa.gov/)
- [SSCWeb User Guide](https://sscweb.gsfc.nasa.gov/WebServices/SSCWebServices.pdf)
