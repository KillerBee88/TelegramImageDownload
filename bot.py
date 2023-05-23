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
    TG_API_KEY = os.getenv('TG_BOT_API')
    NASA_API_KEY = os.getenv('NASA_API_KEY')
    CHANNEL_ID = os.getenv('CHANNEL_ID')
    
    bot = Bot(token=TG_API_KEY)
    chat_id = CHANNEL_ID

    get_fetch_functions = [fetch_nasa_apod_images, fetch_nasa_epic_images, fetch_spacex_last_launch]
    fetch_func = random.choice(get_fetch_functions)

    if fetch_func == fetch_spacex_last_launch:
        image_urls = fetch_func()
    else:
        image_urls = fetch_func(NASA_API_KEY, count=1)

    print(f"Fetched image URLs: {image_urls}")
    
    if image_urls:
        send_photo_to_channel(bot, chat_id, image_urls[0])

if __name__ == '__main__':
    main()
