# Internet Archive

The class for fetching metadata and images from [Internet Archive](https://archive.org/) with its [Python API](https://archive.org/developers/internetarchive/index.html).

## Usage

Create a querier for Internet Archive:

```python
from libquery import InternetArchive

directory = './output/internet-archive'
querier = InternetArchive(
    metadata_dir=f'{directory}/metadata',
    download_dir=f'{directory}/downloads',
    img_dir=f'{directory}/imgs',
)
```

Query metadata:

```python
queries = [
    'creator:(Snow, John) AND -collection:(david-rumsey-map-collection) AND date:[1800-01-01 TO 1950-12-31]',
    'creator:(Cheysson, Émile) AND -collection:(david-rumsey-map-collection) AND date:[0001-01-01 TO 1990-12-31]',
]
querier.fetch_metadata(queries=queries)
```

Query images:

```python
querier.fetch_image()
```

## Metadata Schema

Each metadata entry is stored as:

```typescript
interface FileMetadata {
    name: string
    source: string
    format: string
    md5: string
    btih?: string
    mtime?: string
    size?: string
    crc32?: string
    sha1?: string
    rotation?: string
    original?: string
}

interface InternetArchiveMetadata {
    /**
     * The identifier that can be used to retrieve the item through
     * internetarchive.get_item(identifier).
     */
    identifier: string
    mediatype: string
    title: string
    publicdate: string
    uploader: string
    addeddate: string
    collection: string[] | string
    call_number?: string
    /** The entries' corresponding location. */
    coverage?: string[] | string
    creator?: string[] | string
    /** The publication date. */
    date?: string[] | string
    description?: string
    'external-identifier'?: string[]
    format?: string
    'map-type'?: string[] | string
    publisher?: string
    /** Copyright information. */
    rights?: string
    scanner?: string
    size?: string
    /** The url of the entry in the original data source. */
    source?: string
    subject?: string[] | string
    /** The warning about the metadata. */
    warning?: string
    year?: string
}

interface SourceData {
    created: number
    d1: string
    d2: string
    dir: string
    files: FileMetadata[]
    files_count: number
    item_last_updated: number
    item_size: number
    metadata: InternetArchiveMetadata
    server: string
    uniq: number
    workable_servers: string[]
    reviews?: string[]
    servers_unavailable?: boolean
}

interface MetadataEntry {
    uuid: string
    url: string
    source: 'Internet Archive'
    idInSource: string
    accessDate: string
    /** The query return from python API. */
    sourceData: SourceData
}
```
