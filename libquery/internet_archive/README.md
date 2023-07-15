# README

## Data Structure

Using the python API provided by Internet Archive, we store each metadata entry as:

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
