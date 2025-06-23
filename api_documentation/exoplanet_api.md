# Exoplanet Archive API

## Overview
The Exoplanet Archive API provides programmatic access to NASA's Exoplanet Archive database, a comprehensive collection of data on exoplanets and their host stars. This API contains extensive options for querying and retrieving exoplanet data for research and educational purposes.

## Introduction
The Exoplanet Archive is a rich resource containing confirmed and candidate exoplanets, along with stellar and planetary properties, discovery/characterization data, and various tools for working with these datasets. The API allows developers to access this information programmatically rather than through the web interface.

## API Documentation

### Base URL
The API can be accessed through the NASA Exoplanet Archive:
`https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI`

### Query Parameters

| Parameter | Description |
|-----------|-------------|
| `table` | The table to query (e.g., "exoplanets", "compositepars") |
| `select` | Comma-separated list of columns to return |
| `where` | SQL-like WHERE clause to filter results |
| `order` | Column(s) to sort by |
| `format` | Output format (json, csv, xml, ipac) |

### Available Tables
- `exoplanets`: Confirmed exoplanets
- `compositepars`: Composite planet parameters
- `missionstars`: Stars observed by various missions
- `aliasgdr`: Aliases for stars and planets
- And many more specialized tables

### Example Queries

#### Basic Query for All Confirmed Exoplanets
```
https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=json
```

#### Query for Specific Planet Properties
```
https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_name,pl_orbper,pl_masse,pl_rade,st_dist&format=json
```

#### Query with Filtering
```
https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_name,pl_orbper,pl_masse,pl_rade,st_dist&where=pl_orbper<10 and pl_masse>1&format=json
```

## Response Format
The API can return data in several formats:
- JSON
- CSV
- XML
- IPAC Table Format

### Example JSON Response
```json
[
  {
    "pl_name": "11 Com b",
    "pl_orbper": "326.03",
    "pl_masse": "19.4",
    "pl_rade": "",
    "st_dist": "110.6"
  },
  {
    "pl_name": "11 UMi b",
    "pl_orbper": "516.22",
    "pl_masse": "10.5",
    "pl_rade": "",
    "st_dist": "119.5"
  }
]
```

## Common Parameters and Fields

### Planet Parameters
- `pl_name`: Planet name
- `pl_orbper`: Orbital period (days)
- `pl_orbsmax`: Orbit semi-major axis (AU)
- `pl_rade`: Planet radius (Earth radii)
- `pl_radj`: Planet radius (Jupiter radii)
- `pl_masse`: Planet mass (Earth masses)
- `pl_massj`: Planet mass (Jupiter masses)
- `pl_discmethod`: Discovery method

### Stellar Parameters
- `st_name`: Host star name
- `st_teff`: Effective temperature (K)
- `st_rad`: Stellar radius (solar radii)
- `st_mass`: Stellar mass (solar masses)
- `st_dist`: Distance (parsecs)
- `st_age`: Stellar age (Gyr)

## Usage Notes
- The API is particularly useful for researchers and educators working with exoplanet data
- Queries can be complex and allow for sophisticated filtering of the database
- The API does not require authentication or an API key
- There are rate limits in place to prevent server overload
- For large or complex queries, consider using the batch processing options
- The database is regularly updated as new exoplanets are discovered and characterized

## Additional Resources
- [NASA's Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/)
- [Introductory Materials](https://exoplanetarchive.ipac.caltech.edu/docs/intro.html)
- [Available Data Documentation](https://exoplanetarchive.ipac.caltech.edu/docs/API_exoplanet_columns.html)
- [Best Practices and Troubleshooting](https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html)
