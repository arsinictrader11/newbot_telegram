import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, filters

# إعداد التوكن
TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=TOKEN)

# إعداد Flask
app = Flask(__name__)

# إعداد Dispatcher
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0, use_context=True)

# أمر /start
def start(update, context):
    text = (
        "🚀 *مرحبًا!*\n\n"
        "أهلاً بك في القناة، نقدم:\n"
        "- محتوى تعليمي يساعدك على الاعتماد على نفسك في التداول.\n"
        "- جلسات تحليل يومية وصفقات مدروسة.\n"
        "- لايفات أسبوعية لشرح استراتيجيات.\n"
        "- خطط إدارة رأس مال فردية.\n"
        "- متابعة يومية لتحقيق نتائج.\n\n"
        "*رابط القناة: [اضغط هنا للانضمام](https://t.me/Arsenic_Trader0)*"
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode="Markdown")

# إضافة Handler
dispatcher.add_handler(CommandHandler("start", start))

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
        return "OK"
    return "🤖 Bot is running on Vercel!"
