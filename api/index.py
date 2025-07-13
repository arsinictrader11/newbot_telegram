import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("⚠️ BOT_TOKEN is not set in environment variables.")

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 البوت يعمل بنجاح.\n\n"
        "للانضمام إلى قناة التداول:\n"
        "https://t.me/Arsenic_Trader0"
    )

application.add_handler(CommandHandler("start", start))

@app.route("/", methods=["GET"])
def home():
    return "🤖 Bot is running on Vercel!"

@app.route("/", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return "OK"
