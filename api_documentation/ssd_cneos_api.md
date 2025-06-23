# SSD/CNEOS API

## Overview
The SSD/CNEOS API provides an interface to machine-readable data related to Solar System Dynamics (SSD) and the Center for Near-Earth Object Studies (CNEOS). This service offers programmatic access to various datasets concerning asteroids, comets, and near-Earth objects, including close approaches, impact assessments, and orbital information.

## Base URL
`https://ssd-api.jpl.nasa.gov/`

## API Components
The API consists of several component services, each providing specific types of data:

### 1. CAD (Close-Approach Data)
`GET /cad.api`

Provides access to current close-approach data for all asteroids and comets in JPL's Small-Body Database (SBDB).

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `date-min` | string | -30 | Start date for search (days from now or YYYY-MM-DD) |
| `date-max` | string | +60 | End date for search (days from now or YYYY-MM-DD) |
| `dist-min` | float | | Minimum approach distance (au or LD) |
| `dist-max` | float | 0.05 | Maximum approach distance (au or LD) |
| `h-min` | float | | Minimum absolute magnitude |
| `h-max` | float | | Maximum absolute magnitude |
| `v-inf-min` | float | | Minimum approach velocity (km/s) |
| `v-inf-max` | float | | Maximum approach velocity (km/s) |
| `v-rel-min` | float | | Minimum relative velocity (km/s) |
| `v-rel-max` | float | | Maximum relative velocity (km/s) |
| `class` | string | | Object class/type filter |
| `pha` | boolean | | Potentially Hazardous Asteroid filter |
| `nea` | boolean | | Near-Earth Asteroid filter |
| `comet` | boolean | | Comet filter |
| `neo` | boolean | | Near-Earth Object filter |
| `kind` | string | | Object kind filter (a=asteroid, c=comet) |
| `spk` | int/string | | Object SPK-ID filter |
| `des` | string | | Object designation filter |
| `body` | string | | Body filter (Earth, Moon, etc.) |
| `sort` | string | date | Sort key |
| `limit` | int | 50 | Maximum number of results |
| `fullname` | boolean | false | Show full object names |
| `format` | string | json | Output format (json, csv, xml) |

#### Example Request
```
GET https://ssd-api.jpl.nasa.gov/cad.api?date-min=2023-01-01&date-max=2023-01-31&dist-max=0.1
```

### 2. Fireball
`GET /fireball.api`

Provides data about fireball atmospheric impact events reported by US Government sensors.

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `date-min` | string | | Start date (YYYY-MM-DD) |
| `date-max` | string | | End date (YYYY-MM-DD) |
| `energy-min` | float | | Minimum energy (kt) |
| `energy-max` | float | | Maximum energy (kt) |
| `impact-e-min` | float | | Minimum impact energy (kt) |
| `impact-e-max` | float | | Maximum impact energy (kt) |
| `vel-min` | float | | Minimum velocity (km/s) |
| `vel-max` | float | | Maximum velocity (km/s) |
| `alt-min` | float | | Minimum altitude (km) |
| `alt-max` | float | | Maximum altitude (km) |
| `req-loc` | boolean | | Require location data |
| `limit` | int | 50 | Maximum number of results |
| `sort` | string | date | Sort key |
| `format` | string | json | Output format (json, csv, xml) |

#### Example Request
```
GET https://ssd-api.jpl.nasa.gov/fireball.api?date-min=2022-01-01&energy-min=1
```

### 3. Mission Design
`GET /mdesign.api`

Provides a small-body mission design suite for trajectory planning and analysis.

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `spk` | int/string | | Object SPK-ID |
| `des` | string | | Object designation |
| `launch-min` | string | | Minimum launch date (YYYY-MM-DD) |
| `launch-max` | string | | Maximum launch date (YYYY-MM-DD) |
| `dur-min` | float | | Minimum mission duration (days) |
| `dur-max` | float | | Maximum mission duration (days) |
| `dv-min` | float | | Minimum delta-v (km/s) |
| `dv-max` | float | | Maximum delta-v (km/s) |
| `format` | string | json | Output format (json, csv, xml) |

#### Example Request
```
GET https://ssd-api.jpl.nasa.gov/mdesign.api?des=433&launch-min=2025-01-01&launch-max=2025-12-31
```

### 4. NHATS (Near-Earth Object Human Space Flight Accessible Targets Study)
`GET /nhats.api`

Provides data about human-accessible NEOs (Near-Earth Objects).

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `spk` | int/string | | Object SPK-ID |
| `des` | string | | Object designation |
| `dv-max` | float | 12 | Maximum delta-v (km/s) |
| `dur-max` | int | 450 | Maximum mission duration (days) |
| `stay-min` | int | 8 | Minimum stay time (days) |
| `launch-min` | string | | Minimum launch date (YYYY-MM-DD) |
| `launch-max` | string | | Maximum launch date (YYYY-MM-DD) |
| `h-max` | float | | Maximum absolute magnitude |
| `occ-min` | int | | Minimum launch opportunities |
| `format` | string | json | Output format (json, csv, xml) |

#### Example Request
```
GET https://ssd-api.jpl.nasa.gov/nhats.api?dv-max=10&dur-max=400
```

### 5. Scout
`GET /scout.api`

Provides NEOCP (Near-Earth Object Confirmation Page) orbits, ephemerides, and impact risk data.

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `tdes` | string | | Temporary designation |
| `eph-start` | string | | Ephemeris start time (YYYY-MM-DD) |
| `eph-stop` | string | | Ephemeris stop time (YYYY-MM-DD) |
| `eph-step` | string | | Ephemeris step size |
| `obs-code` | string | | Observatory code |
| `format` | string | json | Output format (json, csv, xml) |

#### Example Request
```
GET https://ssd-api.jpl.nasa.gov/scout.api?tdes=ZTF0DfD
```

### 6. Sentry
`GET /sentry.api`

Provides NEO Earth impact risk assessment data.

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `spk` | int/string | | Object SPK-ID |
| `des` | string | | Object designation |
| `h-min` | float | | Minimum absolute magnitude |
| `h-max` | float | | Maximum absolute magnitude |
| `ps-min` | float | | Minimum Palermo Scale |
| `ps-max` | float | | Maximum Palermo Scale |
| `ip-min` | float | | Minimum impact probability |
| `ip-max` | float | | Maximum impact probability |
| `limit` | int | 50 | Maximum number of results |
| `format` | string | json | Output format (json, csv, xml) |

#### Example Request
```
GET https://ssd-api.jpl.nasa.gov/sentry.api?ip-min=0.01
```

### 7. SBDB (Small-Body Database)
`GET /sbdb.api`

Provides access to the Small-Body Database, containing information about asteroids and comets.

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `spk` | int/string | | Object SPK-ID |
| `des` | string | | Object designation |
| `name` | string | | Object name |
| `neo` | boolean | | Near-Earth Object filter |
| `pha` | boolean | | Potentially Hazardous Asteroid filter |
| `nea` | boolean | | Near-Earth Asteroid filter |
| `comet` | boolean | | Comet filter |
| `kind` | string | | Object kind filter (a=asteroid, c=comet) |
| `mb` | boolean | | Main-belt Asteroid filter |
| `tro` | boolean | | Trojan Asteroid filter |
| `cen` | boolean | | Centaur filter |
| `tno` | boolean | | Trans-Neptunian Object filter |
| `fullname` | boolean | false | Show full object names |
| `format` | string | json | Output format (json, csv, xml) |

#### Example Request
```
GET https://ssd-api.jpl.nasa.gov/sbdb.api?des=433
```

## Response Format
The API supports multiple output formats:
- JSON (default)
- CSV
- XML

### Example JSON Response (CAD API, abbreviated)
```json
{
  "signature": {
    "source": "NASA/JPL SBDB Close Approach Data API",
    "version": "1.4"
  },
  "count": 2,
  "fields": [
    "des", "orbit_id", "jd", "cd", "dist", "dist_min", "dist_max", "v_rel", "v_inf", "t_sigma_f", "h"
  ],
  "data": [
    [
      "2010 PK9",
      "26",
      "2459580.747488796",
      "2022-Jan-01 05:56:23",
      "0.0429050287950056",
      "0.0428998556546592",
      "0.0429102019353521",
      "6.0387266869819",
      "6.03643333147289",
      "< 00:01",
      "27.7"
    ],
    [
      "2021 RQ46",
      "7",
      "2459580.7511284285",
      "2022-Jan-01 06:01:37",
      "0.0257325567493916",
      "0.0257324159910166",
      "0.0257326975077666",
      "8.31341729693859",
      "8.31209270668452",
      "< 00:01",
      "26.1"
    ]
  ]
}
```

## Usage Notes
- The API does not require authentication or an API key
- Default query parameters are set for typical CNEOS web-site searches
- For human-readable data, users should visit the main SSD and CNEOS websites
- The API is particularly valuable for researchers, astronomers, and developers working with near-Earth object data
- Large queries may take time to process; consider using appropriate filters
- Some endpoints have rate limits to prevent server overload

## Additional Resources
- [JPL SSD/CNEOS API](https://ssd-api.jpl.nasa.gov/)
- [Solar System Dynamics (SSD)](https://ssd.jpl.nasa.gov/)
- [Center for Near-Earth Object Studies (CNEOS)](https://cneos.jpl.nasa.gov/)
- For questions or support: contact-ssd-api@jpl.nasa.gov
