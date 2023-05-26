import common
import requests

def fetch_spacex_launch_images(launch_id):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
    response.raise_for_status()
    spacex_launch_images = response.json()
    return spacex_launch_images.get('links', {}).get('flickr', {}).get('original', [])

def fetch_spacex_last_launch_id():
    response = requests.get('https://api.spacexdata.com/v5/launches')
    response.raise_for_status()
    spacex_launch_images = response.json()
    return spacex_launch_images[-1].get('id')

def fetch_spacex_last_launch(default_launch_id='5eb87d47ffd86e000604b38a'):
    launch_id = fetch_spacex_last_launch_id()
    image_urls = fetch_spacex_launch_images(launch_id)
    
    if not image_urls:
        image_urls = fetch_spacex_launch_images(default_launch_id)
    
    return image_urls

if __name__ == "__main__":
    image_links = fetch_spacex_last_launch()
    
    for url in image_links:
        common.download_image(url)
