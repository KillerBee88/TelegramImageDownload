import argparse
import requests
import common
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('NASA_API_KEY')

def fetch_nasa_apod_images(api_key, count):
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}&count={count}')
    response.raise_for_status()
    apod_data = response.json()
    image_urls = [item['url'] for item in apod_data if 'image' in item['media_type']]
    return image_urls

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch NASA APOD images")
    parser.add_argument('--count', type=int, default=10, help="Number of images to fetch")
    args = parser.parse_args()

    nasa_image_links = fetch_nasa_apod_images(API_KEY, args.count)
    common.download_images(nasa_image_links)
