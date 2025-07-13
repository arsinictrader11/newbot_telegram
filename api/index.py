import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# احضار التوكن من Vercel Environment
TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN is not set in environment variables.")

# إعداد Flask
app = Flask(__name__)

# إعداد بوت تيليجرام باستخدام ApplicationBuilder
bot_app = ApplicationBuilder().token(TOKEN).build()

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 *مرحبًا!*\n\n"
        "أهلاً بك في القناة، نقدم:\n"
        "- محتوى تعليمي يساعدك على الاعتماد على نفسك في التداول.\n"
        "- جلسات تحليل يومية وصفقات مدروسة.\n"
        "- لايفات أسبوعية لشرح استراتيجيات.\n"
        "- خطط إدارة رأس مال فردية.\n"
        "- متابعة يومية لتحقيق نتائج.\n\n"
        "*رابط القناة: [اضغط هنا للانضمام](https://t.me/Arsenic_Trader0)*",
        parse_mode="Markdown"
    )

# إضافة الأوامر
bot_app.add_handler(CommandHandler("start", start))

# Route اختبار
@app.route("/", methods=["GET"])
def home():
    return "🤖 Bot is running!"

# Route Webhook
@app.route("/", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot_app.bot)
    await bot_app.process_update(update)
    return "OK"

# لا تضع app.run هنا لأن Vercel يدير التشغيل تلقائيًا
