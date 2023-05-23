import argparse
import common
import requests

def fetch_spacex_last_launch(launch_id=None):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
    response.raise_for_status()
    launch_images_data = response.json()
    image_urls = launch_images_data.get('links', {}).get('flickr', {}).get('original', [])
    return image_urls

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch SpaceX images")
    parser.add_argument('--id', type=str, default='5eb87d47ffd86e000604b38a', help="ID of the launch")
    args = parser.parse_args()

    image_links = fetch_spacex_last_launch(args.id)
    common.download_images(image_links)
