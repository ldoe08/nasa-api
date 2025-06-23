# APOD: Astronomy Picture of the Day API

## Overview
The Astronomy Picture of the Day (APOD) API provides access to one of NASA's most popular websites. This API delivers the daily astronomy image along with its description and metadata, allowing developers to incorporate these stunning astronomical images into their applications.

## Endpoint
`GET https://api.nasa.gov/planetary/apod`

## Authentication
Requires an API key that can be obtained from [api.nasa.gov](https://api.nasa.gov/).

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `api_key` | string | None | Your API key. Use "DEMO_KEY" for testing. |
| `date` | string | today | The date of the APOD image to retrieve in YYYY-MM-DD format. Must be after 1995-06-16. |
| `start_date` | string | None | Start date for a range of dates in YYYY-MM-DD format. Cannot be used with `date`. |
| `end_date` | string | current date | End date for a range of dates in YYYY-MM-DD format. Requires `start_date`. |
| `count` | int | None | Number of random images to retrieve (maximum 100). Cannot be used with `date` or `start_date`/`end_date`. |
| `thumbs` | boolean | False | Return thumbnail URL for video content. |
| `concept_tags` | boolean | False | Return concept tags for the image explanation. |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `resource` | object | Dictionary describing the image set or planet. |
| `concept_tags` | boolean | Reflection of the supplied option. |
| `title` | string | The title of the image. |
| `date` | string | Date of the image in YYYY-MM-DD format. |
| `url` | string | URL of the APOD image or video. |
| `hdurl` | string | URL for high-resolution image (omitted if not available). |
| `media_type` | string | Type of media returned ('image' or 'video'). |
| `explanation` | string | Text explanation of the image. |
| `concepts` | array | Most relevant concepts within the explanation (only if `concept_tags=True`). |
| `thumbnail_url` | string | URL of video thumbnail (only for videos when `thumbs=True`). |
| `copyright` | string | Name of the copyright holder (omitted for NASA images). |
| `service_version` | string | The service version used. |

## Example Request
```
GET https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2014-10-01&concept_tags=True
```

## Example Response
```json
{
  "resource": {
    "image_set": "apod"
  },
  "concept_tags": true,
  "date": "2014-10-01",
  "title": "Filaments of the Vela Supernova Remnant",
  "url": "http://apod.nasa.gov/apod/image/1310/velafilaments_jadescope_960.jpg",
  "hdurl": "http://apod.nasa.gov/apod/image/1310/velafilaments_jadescope_2048.jpg",
  "media_type": "image",
  "explanation": "The explosion is over but the consequences continue. About eleven thousand years ago a star in the constellation of Vela could be seen to explode, creating a strange point of light briefly visible to humans living near the beginning of recorded history. The outer layers of the star crashed into the interstellar medium, driving a shock wave that is still visible today.",
  "concepts": ["Astronomy", "Supernova", "Vela"],
  "copyright": "Jade Scope Observatory",
  "service_version": "v1"
}
```

## Usage Notes
- The APOD API is one of NASA's most popular APIs and is an excellent starting point for developers.
- Images are available from June 16, 1995, to the present day.
- When requesting a date range or random images, the response will be an array of objects.
- The `concept_tags` parameter can be useful for categorizing or tagging images automatically.
- The API has rate limits of 1,000 requests per hour for registered API keys and much lower limits for the DEMO_KEY.

## GitHub Repository
For more detailed information and implementation examples, visit the [APOD API GitHub repository](https://github.com/nasa/apod-api).
