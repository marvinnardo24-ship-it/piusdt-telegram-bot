import os
import requests
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

def send_alert(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    send_alert("✅ Bot deployed successfully on Render!")