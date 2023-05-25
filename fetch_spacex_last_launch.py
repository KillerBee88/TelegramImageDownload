import common
import requests

def fetch_spacex_last_launch_id():
    response = requests.get('https://api.spacexdata.com/v5/launches')
    response.raise_for_status()
    spacex_launch_images = response.json()
    last_launch_id = spacex_launch_images[-1].get('id')
    return last_launch_id

def fetch_spacex_last_launch(default_launch_id='5eb87d47ffd86e000604b38a'):
    launch_id = fetch_spacex_last_launch_id()
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
    response.raise_for_status()
    launch_images_data = response.json()
    image_urls = launch_images_data.get('links', {}).get('flickr', {}).get('original', [])
    
    if not image_urls:
        response = requests.get(f'https://api.spacexdata.com/v5/launches/{default_launch_id}')
        response.raise_for_status()
        launch_images_data = response.json()
        image_urls = launch_images_data.get('links', {}).get('flickr', {}).get('original', [])
    return image_urls

if __name__ == "__main__":
    image_links = fetch_spacex_last_launch()
    
    for url in image_links:
        common.download_image(url)
