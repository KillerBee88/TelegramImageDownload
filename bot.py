from telegram import Bot
import os
from dotenv import load_dotenv
from fetch_nasa_apod_images import fetch_nasa_apod_images

load_dotenv()
TG_API_KEY = os.getenv('TG_BOT_API')
NASA_API_KEY = os.getenv('NASA_API_KEY')

def send_photo_to_channel(bot, chat_id, photo_url):
    bot.send_photo(chat_id=chat_id, photo=photo_url)

def main():
    bot = Bot(token=TG_API_KEY)
    chat_id = "@test_channel2406"

    image_urls = fetch_nasa_apod_images(NASA_API_KEY, count=1)
    
    if image_urls:
        send_photo_to_channel(bot, chat_id, image_urls[0])

if __name__ == '__main__':
    main()