"""
The entrance to querier class.
"""

from typing import List

from ...base import BaseQuerier
from ...utils.jsonl import save_jl
from .fetch_metadata import (fetch_metadata,
                             merge_deduplicate_metadata)
from .fetch_image import fetch_image


class Querier(BaseQuerier):
    """
    The querier for the `Internet Archive` data source.
    """

    def __init__(self, metadata_path: str,
                 download_dir: str,
                 img_dir: str):
        """
        Args
        ----
        metadata_path : str
            The file storing the metadata from each query.
        download_dir : str
            The directory storing the downloads from each query.
        img_dir : str
            The directory storing the images extract from downloads.
        """
        
        self.metadata_path = metadata_path
        self.download_dir = download_dir
        self.img_dir = img_dir

    @property
    def query_return_dir(self) -> str:
        """The directory storing the metadata from each query."""

        dirname = 'query-return'
        return f'{self.metadata_dir}/{dirname}'

    def fetch_metadata(self, queries: List[str]) -> None:
        fetch_metadata(queries,
                       self.query_return_dir,
                       deduplicate=True)
        entries = merge_deduplicate_metadata(
            queries, self.query_return_dir)
        save_jl(entries, self.metadata_path)

    def fetch_image(self) -> None:
        fetch_image(self.metadata_path,
                    self.download_dir,
                    self.img_dir)
