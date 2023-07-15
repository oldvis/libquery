# README

## Data Structure

Using the LUNA API provided by David Rumsey Map Collection, we store each metadata entry as:

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
