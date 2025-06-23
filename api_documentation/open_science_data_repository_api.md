# Open Science Data Repository API

## Overview
The NASA Open Science Data Repository (OSDR) provides a RESTful Application Programming Interface (API) to its full-text search, data file retrieval, and metadata retrieval capabilities. This API allows programmatic access to NASA's extensive scientific datasets and associated metadata.

## Features
- Full-text search capabilities
- Data file retrieval
- Metadata retrieval for various data types
- Support for multiple output formats (JSON, HTML)
- Integration with other scientific databases

## API Documentation

### Base URL
`https://osdr.nasa.gov/osdr/`

### Data Types
The OSDR API provides access to metadata for 8 different data types:
1. Study datasets
2. Experiments
3. Payloads
4. Subjects
5. Biospecimens
6. Missions
7. Vehicles
8. Hardware

### Study Data File API

#### Endpoint
`GET https://osdr.nasa.gov/osdr/data/osd/files/{OSD_STUDY_IDs}`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page` | integer | 1 | Current page number |
| `size` | integer | 10 | Results per page |
| `all_files` | boolean | false | Whether to include all files |

#### Example Request
```
GET https://osdr.nasa.gov/osdr/data/osd/files/OSD-123?page=1&size=20&all_files=true
```

#### Response Format
Returns a JSON-formatted response containing metadata on data files associated with dataset(s), including the location of these files for download via HTTPS.

### Study Metadata API

#### Endpoint
`GET https://osdr.nasa.gov/osdr/data/osd/meta/{OSD_STUDY_IDs}`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `format` | string | "json" | Output format (json or html) |

#### Example Request
```
GET https://osdr.nasa.gov/osdr/data/osd/meta/OSD-123?format=json
```

#### Response Format
Returns entire sets of metadata for input study dataset accession numbers.

### Search API

#### Endpoint
`GET https://osdr.nasa.gov/osdr/search`

#### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `q` | string | required | Search query |
| `db` | string | "all" | Database to search (all, nih, ebi, anl) |
| `format` | string | "json" | Output format (json or html) |
| `page` | integer | 1 | Current page number |
| `size` | integer | 10 | Results per page |

#### Example Request
```
GET https://osdr.nasa.gov/osdr/search?q=microgravity&db=all&format=json&page=1&size=20
```

#### Response Format
Returns search results matching the query across specified databases.

## External Database Integration
The Search API can also be used to search three other omics databases:
1. National Institutes of Health (NIH) / National Center for Biotechnology Information's (NCBI) Gene Expression Omnibus (GEO)
2. European Bioinformatics Institute's (EBI) Proteomics Identification (PRIDE)
3. Argonne National Laboratory's (ANL) Metagenomics Rapid Annotations using Subsystems Technology (MG-RAST)

## Usage Notes
- The API provides a choice of standard web output formats: either JavaScript Object Notation (JSON) or Hyper Text Markup Language (HTML)
- All data types use a uniform API structure for consistency
- Authentication is not required for public datasets
- Rate limiting may apply to prevent server overload
- For large datasets, pagination is recommended using the page and size parameters
- The API is particularly valuable for researchers working with NASA scientific data and those conducting meta-analyses across multiple datasets

## Example Response (Abbreviated)
```json
{
  "page": 1,
  "size": 10,
  "total_results": 42,
  "total_pages": 5,
  "results": [
    {
      "study_id": "OSD-123",
      "title": "Effects of Microgravity on Gene Expression",
      "description": "Study of gene expression changes in human cells exposed to microgravity on the ISS",
      "files": [
        {
          "file_id": "FILE-456",
          "filename": "gene_expression_data.csv",
          "size_bytes": 2456789,
          "download_url": "https://osdr.nasa.gov/download/FILE-456"
        }
      ]
    }
  ]
}
```
