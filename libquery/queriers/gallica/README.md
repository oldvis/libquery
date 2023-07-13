# Readme

## Data Structure

Using the API provided by Gallica, we store each metadata entry as:

```typescript
interface TextWithLang {
    '@xml:lang': string
    '#text': string
}

interface Record {
    '@xmlns:dc': string
    '@xmlns:oai_dc': string
    '@xmlns:xsi': string
    '@xsi:schemaLocation': string
    'dc:identifier': string | string[]
    'dc:relation': string | string[]
    'dc:source': string
    'dc:title': string | (string | TextWithLang)[]
    /** The author(s). */
    'dc:creator'?: string | string[]
    'dc:date'?: string | string[]
    'dc:subject'?: string | TextWithLang | (string | TextWithLang)[] | null
    'dc:coverage'?: string | string[] | null
    'dc:format'?: string | TextWithLang | (string | TextWithLang)[]
    /** For collections within the BnF, the language code has 3 characters. */
    /** For collections from outside, the language code can be arbitrary. */
    'dc:language'?: string | string[]
    /** Type of the document, e.g., monograph, map, image, */
    /** fascicle, manuscript, score, sound, object and video. */
    'dc:type'?: (string | TextWithLang)[]
    'dc:rights'?: TextWithLang[]
    'dc:publisher'?: string | string[]
    'dc:description'?: string | string[]
    'dc:contributor'?: string | string[]
    '#text'?: string
}

interface Page {
    numero: string | null
    ordre: string
    pagination_type: string | null
    image_width: string
    image_height: string
    legend?: string
}

interface MetadataEntry {
    uuid: string
    url: string
    source: 'Gallica'
    idInSource: string
    accessDate: string
    /** The query return from API. */
    sourceData: {
        identifier: string
        record: Record
        pages: Page[]
    }
}
```
