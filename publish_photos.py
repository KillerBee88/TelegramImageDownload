import os
import random
import schedule
import time
from dotenv import load_dotenv
from telegram import Bot
import argparse


def send_photo(bot, chat_id, photo_path):
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id, photo=photo)


def publish_photo(bot, image_directory):
    all_files = os.listdir(image_directory)
    image_files = [f for f in all_files if os.path.isfile(os.path.join(image_directory, f))]
    random.shuffle(image_files)
    for image_file in image_files:
        send_photo(bot, os.path.join(image_directory, image_file))
        time.sleep(3600)


if __name__ == "__main__":
    load_dotenv()
    
    parser = argparse.ArgumentParser(description='Публикация изображений в Телеграм канал каждые N часов.')
    parser.add_argument('dir', help='Директория с изображениями.')
    parser.add_argument('--hours', type=int, default=4, help='Интервал между постами в часах.')
    args = parser.parse_args()

    token = os.getenv('TG_BOT_API')
    chat_id = os.getenv('TG_CHAT_ID')

    bot = Bot(token)
    schedule.every(args.hours).hours.do(publish_photo, bot=bot, chat_id=chat_id, image_directory=args.dir)

    while True:
        schedule.run_pending()
        time.sleep(1)


