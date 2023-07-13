"""
The entrance to querier class.
"""

from typing import List

from ...base import BaseQuerierWithQueryReturn
from ...typing import ImageQuery
from ...utils.fetch_image import fetch_image
from ...utils.jsonl import save_jl
from .._utils.metadata import deduplicate
from .fetch_metadata import fetch_metadata, merge_metadata
from .typing import MetadataEntry, SourceData


def get_download_url(source_data: SourceData) -> str:
    return source_data['urlSize4'] if 'urlSize4' in source_data\
        else source_data['urlSize2']


def build_image_queries(metadata: List[MetadataEntry]) -> List[ImageQuery]:
    """Build a list of image urls to query."""

    return [{
        'url': get_download_url(d['sourceData']),
        'uuid': d['uuid'],
    } for d in metadata]


class Querier(BaseQuerierWithQueryReturn):
    """
    The querier for the `David Rumsey Map Collection` data source.
    """

    def fetch_metadata(self, queries: List[str]) -> None:
        """
        Args
        ----
        queries : List[str]
            The base urls for which query results are to be stored.
        """

        fetch_metadata(queries, self.query_return_dir)
        entries = merge_metadata(queries, self.query_return_dir)
        save_jl(entries, self.metadata_path)
        deduplicate(self.metadata_path)

    def fetch_image(self) -> None:
        fetch_image(self.metadata_path,
                    self.img_dir,
                    build_image_queries)
