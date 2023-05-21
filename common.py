import os
from urllib.parse import unquote, urlsplit
from os.path import splitext
import requests


def get_extension_from_url(url):
    parsed_url = urlsplit(url)
    path = unquote(parsed_url.path)
    extension = splitext(path)[1]
    return extension


def download_images(image_urls, save_dir='images'):
    os.makedirs(save_dir, exist_ok=True)
    for url in image_urls:
        extension = get_extension_from_url(url)
        if extension.lower() not in ['.jpg', '.jpeg', '.png']:
            continue
        response = requests.get(url)
        response.raise_for_status()
        image_name = url.split('/')[-1]
        with open(os.path.join(save_dir, image_name), 'wb') as f:
            f.write(response.content)
