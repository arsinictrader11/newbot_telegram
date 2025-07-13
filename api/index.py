import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# إعداد التوكن من متغير البيئة في Vercel
TOKEN = os.environ.get("BOT_TOKEN")

# إعداد Flask
app = Flask(__name__)

# إعداد بوت تيليجرام
application = Application.builder().token(TOKEN).build()

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    await update.message.reply_text(text, parse_mode="Markdown")

# إضافة أوامر البوت
application.add_handler(CommandHandler("start", start))

# Route لفحص التشغيل
@app.route("/", methods=["GET"])
def index():
    return "🤖 Bot is running on Vercel!"

# Route لمعالجة Webhook
@app.route("/", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return "OK"

# لا تضع app.run هنا لأن Vercel يديره تلقائيًا
