# David Rumsey Map Collection

The class for fetching metadata and images from [David Rumsey Map Collection](https://www.davidrumsey.com/) with its [LUNA API](https://doc.lunaimaging.com/display/V74D/LUNA+API+Documentation).

## Usage

Create a querier for David Rumsey Map Collection:

```python
from libquery import DavidRumseyMapCollection

directory = "./output/david-rumsey-map-collection"
querier = DavidRumseyMapCollection(
    metadata_dir=f"{directory}/metadata",
    img_dir=f"{directory}/imgs",
)
```

Query metadata:

```python
base_url = "https://www.davidrumsey.com/luna/servlet/as/search?"
queries = [
    f"{base_url}q=type=chart",
    f"{base_url}q=type=diagram",
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
type Fields = 'Author' | 'Date' | 'Short Title'
    | 'Publisher' | 'Publisher Location' | 'Type'
    | 'Obj Height cm' | 'Obj Width cm' | 'Scale 1'
    | 'World Area' | 'Subject' | 'Full Title'
    | 'List No' | 'Page No' | 'Series No'
    | 'Engraver or Printer' | 'Publication Author'
    | 'Pub Date' | 'Pub Title' | 'Pub List No'
    | 'Pub Type' | 'Pub Maps'
    | 'Pub Height cm' | 'Pub Width cm'
    | 'Image No' | 'Download 1' | 'Download 2' | 'Authors'

interface SourceData {
    displayName: string
    description: string
    mediaType: string
    relayButtonUrl: string
    relayButtonTitle: string
    urlSize4?: string
    urlSize3?: string
    urlSize2: string
    urlSize1: string
    urlSize0: string
    iiifManifest: string
    id: string
    fieldValues: Record<Fields, string[]>[]
    relatedFieldValues: unknown[]
}

interface MetadataEntry {
    uuid: string
    url: string
    source: 'David Rumsey Map Collection'
    idInSource: string
    accessDate: string
    /** The query return from LUNA API. */
    sourceData: SourceData
}
```
