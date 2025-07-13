from flask import Flask, request
from telegram import Bot, Update

import os

app = Flask(__name__)

TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=TOKEN)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot)
    chat_id = update.message.chat.id
    message_text = update.message.text

    if message_text == "/start":
        bot.send_message(chat_id=chat_id, text="🚀 مرحبًا! البوت يعمل بنجاح على Vercel 🎉")

    return "OK"

if __name__ == "__main__":
    app.run()
