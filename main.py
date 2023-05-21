import os
import requests
from dotenv import load_dotenv 
from urllib.parse import unquote, urlsplit
from os.path import splitext
from datetime import datetime

load_dotenv()
API_KEY = os.getenv('NASA_API_KEY')


def get_extension_from_url(url):
    parsed_url = urlsplit(url)
    path = unquote(parsed_url.path)
    extension = splitext(path)[1]
    return extension


def fetch_nasa_apod_images(api_key, count):
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}&count={count}')
    response.raise_for_status()
    apod_data = response.json()
    image_urls = [item['url'] for item in apod_data if 'image' in item['media_type']]
    return image_urls


def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
    response.raise_for_status()
    launch_data = response.json()
    image_urls = launch_data.get('links', {}).get('flickr', {}).get('original', [])
    return image_urls


def fetch_nasa_epic_images(api_key, count):
    response = requests.get(f'https://api.nasa.gov/EPIC/api/natural?api_key={api_key}')
    response.raise_for_status()
    data = response.json()

    image_urls = []
    for image in data[:count]:
        date = datetime.strptime(image['date'], "%Y-%m-%d %H:%M:%S").date()
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date.strftime('%Y/%m/%d')}/png/{image['image']}.png"
        image_urls.append(image_url)
    return image_urls


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


if __name__ == "__main__":
    image_links = fetch_spacex_last_launch()
    download_images(image_links)

    nasa_image_links = fetch_nasa_apod_images(API_KEY, 50)
    download_images(nasa_image_links)

    nasa_epic_image_links = fetch_nasa_epic_images(API_KEY, 10)
    download_images(nasa_epic_image_links)
  