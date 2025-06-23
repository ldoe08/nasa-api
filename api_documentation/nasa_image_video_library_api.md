# NASA Image and Video Library API

## Overview
The NASA Image and Video Library API provides access to NASA's extensive collection of images, videos, and audio files. This RESTful API allows developers to search, retrieve, and use NASA's media assets programmatically.

## API Organization
The API is organized around REST principles, with predictable resource-oriented URLs and standard HTTP response codes to indicate API errors. It uses built-in HTTP features such as HTTP authentication and HTTP verbs, making it compatible with standard HTTP clients.

## Base URL
`https://images-api.nasa.gov`

## Response Format
All API responses, including errors, are returned in JSON format. Each endpoint also provides example snippets using the curl command-line tool, Unix pipelines, and Python to output API responses in an easy-to-read format.

## Available Endpoints

### Search Media
`GET /search`

Search for NASA images, videos, and audio files.

#### Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `q` | string | Free text search terms to compare to all indexed metadata |
| `center` | string | NASA center that created the media |
| `description` | string | Terms to search for in the description field |
| `keywords` | string | Terms to search for in the keywords field |
| `location` | string | Terms to search for in the location field |
| `media_type` | string | Media type to filter results by (image, video, audio) |
| `nasa_id` | string | The NASA ID of the media |
| `page` | integer | Page number of results, starting from 1 |
| `year_start` | integer | Starting year for results |
| `year_end` | integer | Ending year for results |

#### Example Request
```
GET https://images-api.nasa.gov/search?q=apollo%2011&media_type=image
```

### Get Asset
`GET /asset/{nasa_id}`

Retrieve the media asset's manifest, which contains links to the available file sizes and formats.

#### Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `nasa_id` | string | The NASA ID of the media asset |

#### Example Request
```
GET https://images-api.nasa.gov/asset/as11-40-5874
```

### Get Metadata
`GET /metadata/{nasa_id}`

Retrieve detailed metadata for a specific media asset.

#### Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `nasa_id` | string | The NASA ID of the media asset |

#### Example Request
```
GET https://images-api.nasa.gov/metadata/as11-40-5874
```

### Get Captions
`GET /captions/{nasa_id}`

Retrieve the location of a video asset's caption file (if available).

#### Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `nasa_id` | string | The NASA ID of the video asset |

#### Example Request
```
GET https://images-api.nasa.gov/captions/Apollo%2011%20Overview
```

## Example Responses

### Search Response
```json
{
  "collection": {
    "version": "1.0",
    "href": "https://images-api.nasa.gov/search?q=apollo%2011&media_type=image",
    "items": [
      {
        "href": "https://images-assets.nasa.gov/image/as11-40-5874/collection.json",
        "data": [
          {
            "center": "JSC",
            "title": "Apollo 11 Mission image - Astronaut Edwin Aldrin walks on lunar surface",
            "nasa_id": "as11-40-5874",
            "media_type": "image",
            "keywords": ["Apollo 11", "Moon", "Lunar Surface", "Astronaut"],
            "date_created": "1969-07-20T00:00:00Z",
            "description": "Apollo 11 Mission image - Astronaut Edwin Aldrin walks on the lunar surface near a leg of the Lunar Module."
          }
        ],
        "links": [
          {
            "href": "https://images-assets.nasa.gov/image/as11-40-5874/as11-40-5874~thumb.jpg",
            "rel": "preview",
            "render": "image"
          }
        ]
      }
    ],
    "metadata": {
      "total_hits": 1000
    },
    "links": [
      {
        "rel": "next",
        "prompt": "Next",
        "href": "https://images-api.nasa.gov/search?q=apollo%2011&media_type=image&page=2"
      }
    ]
  }
}
```

### Asset Response
```json
{
  "collection": {
    "version": "1.0",
    "href": "https://images-api.nasa.gov/asset/as11-40-5874",
    "items": [
      {
        "href": "https://images-assets.nasa.gov/image/as11-40-5874/as11-40-5874~orig.jpg"
      },
      {
        "href": "https://images-assets.nasa.gov/image/as11-40-5874/as11-40-5874~large.jpg"
      },
      {
        "href": "https://images-assets.nasa.gov/image/as11-40-5874/as11-40-5874~medium.jpg"
      },
      {
        "href": "https://images-assets.nasa.gov/image/as11-40-5874/as11-40-5874~small.jpg"
      },
      {
        "href": "https://images-assets.nasa.gov/image/as11-40-5874/as11-40-5874~thumb.jpg"
      }
    ]
  }
}
```

## Usage Notes
- The API does not require authentication or an API key
- JSON is returned by all API responses, including errors
- Search results are paginated, with links to navigate between pages
- Media assets are available in multiple sizes and formats
- The API supports cross-origin resource sharing (CORS) to allow browser-based applications to use it
- For large-scale or production applications, consider implementing caching to reduce load on NASA's servers
- The API is accessible through the website at [images.nasa.gov](https://images.nasa.gov)
- Full documentation is available at the [NASA Image and Video Library API documentation](https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf)

## Additional Resources
- [NASA Image and Video Library Website](https://images.nasa.gov)
- [API Documentation PDF](https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf)
