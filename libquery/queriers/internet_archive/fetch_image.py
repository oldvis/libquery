from .extract_images import extract_images
from .fetch_file import fetch_file


def fetch_image(metadata_path: str,
                download_dir: str,
                img_dir: str):
    fetch_file(metadata_path, download_dir)
    extract_images(download_dir, img_dir)
