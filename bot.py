from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
from dotenv import load_dotenv

load_dotenv()
TG_API_KEY = os.getenv('TG_BOT_API')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я твой новый бот.')

def send_message_to_channel(bot, chat_id, message):
    bot.send_message(chat_id=chat_id, text=message)

def main():
    bot = Bot(token=TG_API_KEY)
    print(bot.get_me())
    
    chat_id = "@test_channel2406"
    message = "Это мое тестовое сообщение"
    send_message_to_channel(bot, chat_id, message)

if __name__ == '__main__':
    main()