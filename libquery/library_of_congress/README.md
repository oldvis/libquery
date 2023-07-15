# Readme

## Data Structure

Using the API provided by Gallica, we store each metadata entry as:

```typescript
interface RelatedItem {
    title: string
    url: string
}

interface Creator {
    link: string
    role: string
    title: string
}

interface Format {
    link: string
    title: string
}

interface Item {
    created_published?: string | string[]
    digital_id?: string[]
    format?: string | string[]
    language?: string | string[]
    notes?: string[]
    repository?: string | string[]
    title?: string
    date?: string
    location?: string[]
    medium?: string[]
    other_title?: string[]
    source_collection?: string | string[]
    subjects?: string[]
    translated_title?: string[]
    call_number?: string | string[]
    contributors?: string[]
    number_former_id?: string[]
    contents?: string | string[]
    creator?: string
    genre?: string[]
    summary?: string | string[]
    rights?: string
    reproduction_number?: string | string[]
    access_advisory?: string | string[]
    related_items?: RelatedItem[]
    rights_advisory?: string | string[]
    control_number?: string
    created?: string
    created_published_date?: string
    creators?: Creator[]
    display_offsite?: boolean
    formats?: Format[]
    id?: string
    link?: string
    marc?: string
    medium_brief?: string
    mediums?: string[]
    modified?: string
    resource_links?: string[]
    rights_information?: string
    service_low?: string
    service_medium?: string
    sort_date?: string
    source_created?: string
    source_modified?: string
    stmt_of_responsibility?: string
    subject_headings?: string[]
    thumb_gallery?: string
}

interface Resource {
    /** The number of files. */
    files?: number
    /** The image URL. */
    image?: string
    /** The metadata query URL. */
    search?: string
    segments?: number
    /** The collection entry URL on loc.gov. */
    url?: string
    caption?: string
    captions?: string | number
    zip?: string
    pdf?: string
    representative_index?: number
    djvu_text_file?: string
    fulltext_derivative?: string
    fulltext_file?: string
    paprika_resource_path?: string
    version?: number
}

interface Segment {
    count: number
    link: string
    url: string
}

interface Related {
    neighbors: string
    group_record?: string
}

interface SourceData {
    access_restricted: boolean
    /** Alternative identifiers for documents (e.g., shortcut urls). */
    aka: string[]
    campaigns: unknown[]
    digitized: boolean
    /** Timestamp of most recent ETL (extract-transform-load) */
    /** process that produced this item. In ISO 8601 format, UTC. */
    extract_timestamp: string
    /**
     * The ETL processes that produced this item.
     * For many items, different attributes are contributed by different ETL processes.
     */
    group: string[]
    /**
     * Whether this item has segmented data
     * (pages, bounding boxes of images, audio segmentation, etc.) in the index.
     */
    hassegments: boolean
    /** HTTP version of the URL for the item, including its identifier. Always appears. */
    id: string
    /**
     * URLs for images in various sizes, if available.
     * If the item is not something that has an image
     * (e.g. it's a book that's not digitized or an exhibit),
     * the URL for the image might be for an icon image file.
     */
    image_url: string[]
    index: number
    /**
     * The item attribute of the item response object provides
     * subfields with information for display of the item on the loc.gov website.
     */
    item: Item
    /** Formats available for download. */
    mime_type: string[]
    /** Format available via the website. */
    online_format: string[]
    /** The kind of object being described (not the digitized version). */
    original_format: string[]
    /** Alternative language titles and other alternative titles. */
    other_title: string[]
    /**
     * Collections, divisions, units in the Library of Congress,
     * or any of a number of less formal groupings and subgroupings used for organizing content.
     */
    partof: string[]
    resources: Resource[]
    /**
     * The primary sorting field of the item record.
     * This field really only has meaning within loc.gov, and is not a canonical identifier.
     */
    shelf_id: string
    timestamp: string
    title: string
    /**
     * URL on the loc.gov website.
     * If the items is something in the library catalog,
     * the URL will start with lccn.loc.gov.
     */
    url: string
    date?: string
    dates?: string[]
    description?: string[]
    language?: string[]
    location?: string[]
    number?: string[]
    number_source_modified?: string[]
    number_related_items?: string[]
    segments?: Segment[]
    site?: string[]
    number_lccn?: string[]
    subject?: string[]
    contributor?: string[]
    location_country?: string[]
    location_county?: string[]
    location_state?: string[]
    location_city?: string[]
    number_former_id?: string[]
    number_carrier_type?: string[]
    number_oclc?: string[]
    type?: string[]
    related?: Related
    reproductions?: string
    unrestricted?: boolean
    publication_frequency?: string[]
}

interface MetadataEntry {
    uuid: string
    url: string
    source: 'Library of Congress'
    idInSource: string
    accessDate: string
    /** The query return from API. */
    sourceData: SourceData
}
```
