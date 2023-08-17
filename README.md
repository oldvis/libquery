<a href="https://pypi.org/project/libquery/">
    <img alt="Newest PyPI version" src="https://img.shields.io/pypi/v/libquery.svg">
</a>
<a href="https://github.com/psf/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
</a>
<a href="http://commitizen.github.io/cz-cli/">
    <img alt="Commitizen friendly" src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg">
</a>

# libquery

A Python package for querying digital libraries.

## Installation

```sh
pip install libquery
```

## Usage Example

Query metadata and images in [David Rumsey Map Collection](https://www.davidrumsey.com/):

```python
from libquery import DavidRumseyMapCollection
querier = DavidRumseyMapCollection("./metadata/", "./imgs/")
querier.fetch_metadata(["https://www.davidrumsey.com/luna/servlet/as/search?q=type=chart"])
querier.fetch_image()
```

## Documentation

See our [documentation website](https://oldvis.github.io/libquery/).
