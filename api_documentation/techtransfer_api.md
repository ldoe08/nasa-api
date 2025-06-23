# TechTransfer API

## Overview
The NASA TechTransfer API provides structured, searchable developer access to NASA's patents, software, and technology spinoff descriptions. This API is part of NASA's Technology Transfer Program, which ensures that innovations developed for exploration and discovery are broadly available to the public, benefiting US citizens through partnerships and licensing agreements with industry.

## Purpose
NASA's patent portfolio is available to benefit US citizens. Through partnerships and licensing agreements with industry, these patents ensure that NASA's investments in pioneering research find secondary uses that benefit the economy, create jobs, and improve quality of life. This API provides programmatic access to these resources.

## Base URL
`https://api.nasa.gov/techtransfer`

## Endpoints

### Patents
`GET https://api.nasa.gov/techtransfer/patent`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `patent` | string | None | Return patents that match the string provided |
| `patent_issued` | string | None | Returns patent results that match the string within the information about how issued each patent |
| `api_key` | string | DEMO_KEY | Your API key |

#### Example Request
```
GET https://api.nasa.gov/techtransfer/patent/?engine&api_key=DEMO_KEY
```

### Software
`GET https://api.nasa.gov/techtransfer/software`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `software` | string | None | Returns NASA software that matches given string |
| `api_key` | string | DEMO_KEY | Your API key |

#### Example Request
```
GET https://api.nasa.gov/techtransfer/software/?autonomous&api_key=DEMO_KEY
```

### Spinoff
`GET https://api.nasa.gov/techtransfer/spinoff`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `spinoff` | string | None | Returns spinoff examples that match given word |
| `api_key` | string | DEMO_KEY | Your API key |

#### Example Request
```
GET https://api.nasa.gov/techtransfer/spinoff/?water&api_key=DEMO_KEY
```

## Response Format
All endpoints return data in JSON format. The structure varies slightly depending on the endpoint:

### Patent Response Example
```json
{
  "count": 2,
  "results": [
    {
      "patent_number": "9,123,456",
      "patent_expiration_date": "2034-05-27",
      "patent_title": "Advanced Engine Technology",
      "patent_abstract": "This invention relates to an advanced engine design that improves fuel efficiency...",
      "center": "Glenn Research Center",
      "primary_class": "60/200.1",
      "secondary_class": null,
      "application_sn": "13/456,789",
      "application_filing_date": "2014-05-27",
      "patent_issue_date": "2016-08-15",
      "inventors": "John Smith, Jane Doe",
      "patent_url": "https://patft.uspto.gov/netacgi/nph-Parser?patentnumber=9123456"
    },
    {
      "patent_number": "8,987,654",
      "patent_expiration_date": "2033-11-12",
      "patent_title": "Combustion Chamber Design",
      "patent_abstract": "A novel combustion chamber design for rocket engines...",
      "center": "Marshall Space Flight Center",
      "primary_class": "60/257",
      "secondary_class": "60/258",
      "application_sn": "13/123,456",
      "application_filing_date": "2013-11-12",
      "patent_issue_date": "2015-03-24",
      "inventors": "Robert Johnson, Maria Garcia",
      "patent_url": "https://patft.uspto.gov/netacgi/nph-Parser?patentnumber=8987654"
    }
  ]
}
```

### Software Response Example
```json
{
  "count": 1,
  "results": [
    {
      "software_title": "Autonomous Navigation System",
      "software_description": "Software for autonomous navigation of unmanned vehicles...",
      "center": "Jet Propulsion Laboratory",
      "release_date": "2020-06-15",
      "software_id": "JPL-12345",
      "categories": ["Autonomous Systems", "Navigation"],
      "download_url": "https://software.nasa.gov/software/JPL-12345"
    }
  ]
}
```

### Spinoff Response Example
```json
{
  "count": 1,
  "results": [
    {
      "title": "Water Purification System",
      "description": "NASA technology adapted for water purification in developing countries...",
      "year": "2019",
      "spinoff_id": "SP-12345",
      "original_nasa_application": "Water recycling systems for the International Space Station",
      "commercial_application": "Portable water purification for disaster relief",
      "url": "https://spinoff.nasa.gov/spinoff/SP-12345"
    }
  ]
}
```

## Usage Notes
- All API responses are in JSON format
- The API is subject to the standard rate limits of api.nasa.gov (1,000 requests per hour for registered API keys)
- Search parameters are case-insensitive
- Partial word matches are supported
- Multiple results may be returned for each query
- The count field indicates the total number of results returned
- Additional information about NASA's technology transfer programs can be found at:
  - [technology.nasa.gov](https://technology.nasa.gov)
  - [software.nasa.gov](https://software.nasa.gov)
  - [spinoff.nasa.gov](https://spinoff.nasa.gov)

## Additional Resources
- [NASA Technology Transfer Program](https://technology.nasa.gov)
- [NASA Software Catalog](https://software.nasa.gov)
- [NASA Spinoff](https://spinoff.nasa.gov)
