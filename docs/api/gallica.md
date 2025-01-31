# Gallica

The class for fetching metadata and images from [Gallica](https://gallica.bnf.fr/) with its [search API](https://api.bnf.fr/api-gallica-de-recherche) and [metadata API](https://api.bnf.fr/api-document-de-gallica).

## Usage

Create a querier for Gallica:

```python
from libquery import Gallica

directory = "./output/gallica"
querier = Gallica(
    metadata_dir=f"{directory}/metadata",
    img_dir=f"{directory}/imgs",
)
```

Query metadata:

```python
base_url = "https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&maximumRecords={maximumRecords}&startRecord={startRecord}"
queries = [
    f"{base_url}&query=dc.title all %22cartes figurative%22",
    f"{base_url}&query=dc.title all %22tableau graphique%22",
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
