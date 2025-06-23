# Insight: Mars Weather Service API

## Overview
The InSight Mars Weather Service API provides access to weather data collected by NASA's InSight Mars lander. The lander takes continuous weather measurements (temperature, wind, pressure) on the surface of Mars at Elysium Planitia, a flat, smooth plain near Mars' equator.

## Important Notice
**Last Updated: 3/30/2021**

THIS SERVICE HAS SIGNIFICANT MISSING DATA DUE TO INSIGHT NEEDING TO MANAGE POWER USE. The API may have gaps in data availability due to power management issues with the InSight lander. Dust accumulation on solar panels and distance from the sun have affected the lander's power situation.

## Data Collection
The API provides per-Sol (Martian day) summary data for each of the last seven available Sols. As more data is downlinked from the spacecraft (sometimes several days later), values may be recalculated and consequently may change as more data is received on Earth.

## Endpoint

### Mars Weather
`GET https://api.nasa.gov/insight_weather/`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `version` | string | "1.0" | API version |
| `feedtype` | string | "json" | Response format (json or csv) |
| `api_key` | string | DEMO_KEY | Your API key |

#### Example Request
```
GET https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0
```

## Response Format
The API returns a JSON object containing:

1. **sol_keys**: An array of strings identifying the available sols (Martian days)
2. **validity_checks**: Information about the validity of the data
3. For each sol in sol_keys, an object containing:
   - **First_UTC**: First UTC timestamp for the sol
   - **Last_UTC**: Last UTC timestamp for the sol
   - **Season**: The Martian season at Elysium Planitia
   - **AT**: Atmospheric temperature sensor data
   - **HWS**: Horizontal wind speed sensor data
   - **PRE**: Pressure sensor data
   - **WD**: Wind direction sensor data

## Example Response (Abbreviated)
```json
{
  "sol_keys": ["259", "260", "261", "262", "263", "264", "265"],
  "259": {
    "First_UTC": "2019-08-16T08:11:09Z",
    "Last_UTC": "2019-08-17T08:50:44Z",
    "Season": "winter",
    "AT": {
      "av": -66.086,
      "ct": 144188,
      "mn": -93.234,
      "mx": -18.674
    },
    "HWS": {
      "av": 4.435,
      "ct": 143467,
      "mn": 0.156,
      "mx": 11.811
    },
    "PRE": {
      "av": 7.5,
      "ct": 144188,
      "mn": 7.386,
      "mx": 7.584
    },
    "WD": {
      "0": {
        "compass_degrees": 0.0,
        "compass_point": "N",
        "compass_right": 0.0,
        "compass_up": 1.0,
        "ct": 2
      },
      "1": {
        "compass_degrees": 22.5,
        "compass_point": "NNE",
        "compass_right": 0.382683432365,
        "compass_up": 0.923879532511,
        "ct": 335
      }
    }
  },
  "validity_checks": {
    "259": {
      "AT": {
        "sol_hours_with_data": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "valid": true
      },
      "HWS": {
        "sol_hours_with_data": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "valid": true
      },
      "PRE": {
        "sol_hours_with_data": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "valid": true
      },
      "WD": {
        "sol_hours_with_data": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "valid": true
      }
    }
  }
}
```

## Sensor Data Details

### AT (Atmospheric Temperature)
- **av**: Average temperature over the sol, in degrees Celsius
- **ct**: Number of data points used for calculations
- **mn**: Minimum temperature over the sol, in degrees Celsius
- **mx**: Maximum temperature over the sol, in degrees Celsius

### HWS (Horizontal Wind Speed)
- **av**: Average wind speed over the sol, in meters per second
- **ct**: Number of data points used for calculations
- **mn**: Minimum wind speed over the sol, in meters per second
- **mx**: Maximum wind speed over the sol, in meters per second

### PRE (Pressure)
- **av**: Average pressure over the sol, in Pascals
- **ct**: Number of data points used for calculations
- **mn**: Minimum pressure over the sol, in Pascals
- **mx**: Maximum pressure over the sol, in Pascals

### WD (Wind Direction)
Wind direction is provided as a collection of compass point "buckets" with:
- **compass_degrees**: Direction in degrees (0-360)
- **compass_point**: Cardinal direction (N, NNE, NE, etc.)
- **compass_right**: X component of direction vector
- **compass_up**: Y component of direction vector
- **ct**: Count of measurements in this direction

## Usage Notes
- Wind and other sensor data may not exist for certain date ranges
- Data gaps are common due to power management issues
- Values may be updated as more data is received from Mars
- Summaries of the data are also available at https://mars.nasa.gov/insight/weather/
- The seasonal weather report plot can be viewed for an illustration of missing data

## Additional Resources
- [Mars InSight Mission](https://mars.nasa.gov/insight/)
- [InSight Weather Page](https://mars.nasa.gov/insight/weather/)
