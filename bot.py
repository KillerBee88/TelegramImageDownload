from telegram import Bot
import os
from dotenv import load_dotenv
from fetch_nasa_apod_images import fetch_nasa_apod_images
from fetch_nasa_epic_images import fetch_nasa_epic_images
from fetch_spacex_last_launch import fetch_spacex_last_launch
import random


def send_photo_to_channel(bot, chat_id, photo_url):
    bot.send_photo(chat_id=chat_id, photo=photo_url)


def main():
    load_dotenv()
    tg_api_key = os.getenv('TG_BOT_API')
    nasa_api_key = os.getenv('NASA_API_KEY')
    chat_id = os.getenv('TG_CHAT_ID')
    
    bot = Bot(token=tg_api_key)

    fetch_functions = [fetch_nasa_apod_images, fetch_nasa_epic_images, fetch_spacex_last_launch]
    image_urls = []

    for fetch_func in fetch_functions:
        if fetch_func == fetch_spacex_last_launch:
            image_urls += fetch_func()
        elif fetch_func == fetch_nasa_apod_images:
            image_urls += fetch_func(nasa_api_key, count=1)
        else:
            image_urls += fetch_func(nasa_api_key, days=1)
    
    if image_urls:
        random_image_url = random.choice(image_urls)
        send_photo_to_channel(bot, chat_id, random_image_url)

if __name__ == '__main__':
    main()
