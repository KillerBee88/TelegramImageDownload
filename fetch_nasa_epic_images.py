import argparse
import requests
import common
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('NASA_API_KEY')


def fetch_nasa_epic_images(api_key, days):
    image_urls = []
    base_url = "https://api.nasa.gov/EPIC/archive/natural/"

    for i in range(days, 0, -1):
        date = (datetime.now() - timedelta(days=i)).date()
        date_str = date.strftime("%Y/%m/%d")
        url = f"{base_url}{date_str}/png/epic_1b_{date.strftime('%Y%m%d')}0000059.png?api_key={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            image_urls.append(url)

    return image_urls

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch NASA EPIC images")
    parser.add_argument('--days', type=int, default=10, help="Number of past days to fetch images for")
    args = parser.parse_args()

    nasa_epic_image_links = fetch_nasa_epic_images(API_KEY, args.days)
    common.download_images(nasa_epic_image_links)
