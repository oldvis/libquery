# API Design

Each querier in [libquery](https://github.com/oldvis/libquery) and [libquery_extensions](https://github.com/oldvis/libquery_extensions) corresponds to a querier class that inherits `BaseQuerier` ([Source](https://github.com/oldvis/libquery/blob/main/libquery/base.py)).

`BaseQuerier` has abstract methods `fetch_metadata` and `fetch_image` .
Note that `fetch_metadata` and `fetch_image` return `None`.
Both methods use side effects to store fetched metadata and images on the local disk.

The fetched metadata is stored as a [JSON Lines](https://jsonlines.org/) file.
Each entry in the JSON Lines file follows the data structure `MetadataEntry` ([Source](https://github.com/oldvis/libquery/blob/main/libquery/typing.py)).
