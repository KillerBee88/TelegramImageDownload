import argparse
import requests
import common
from dotenv import load_dotenv
import os


def fetch_nasa_apod_images(api_key, count):
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}&count={count}')
    response.raise_for_status()
    apod_images = response.json()
    image_urls = [item['url'] for item in apod_images if 'image' in item['media_type']]
    return image_urls

if __name__ == "__main__":
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')
    
    parser = argparse.ArgumentParser(description="Fetch NASA APOD images")
    parser.add_argument('--count', type=int, default=10, help="Number of images to fetch")
    args = parser.parse_args()

    nasa_image_links = fetch_nasa_apod_images(nasa_api_key, args.count)
    
    for url in nasa_image_links:
        common.download_image(url)
