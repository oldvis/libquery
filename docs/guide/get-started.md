# Get Started

libquery is a collection of query functions for accessing metadata and images in digital libraries.

## Installation

```sh
pip install libquery
```

## Usage Example

```python
from libquery import DavidRumseyMapCollection

querier = DavidRumseyMapCollection(
    metadata_dir=f'./metadata',
    img_dir=f'./imgs',
)
querier.fetch_metadata(queries=[
    'https://www.davidrumsey.com/luna/servlet/as/search?q=type=chart',
])
```

More examples can be found in the API Reference.
