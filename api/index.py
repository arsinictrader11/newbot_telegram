import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# الحصول على التوكن من متغيرات البيئة في Vercel
TOKEN = os.environ.get("BOT_TOKEN")

# تأكيد وجود التوكن
if not TOKEN:
    raise ValueError("⚠️ BOT_TOKEN is not set in environment variables.")

# إعداد Flask
app = Flask(__name__)

# إعداد تطبيق تيليجرام
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

# إضافة الأوامر إلى التطبيق
application.add_handler(CommandHandler("start", start))

# Route للفحص
@app.route("/", methods=["GET"])
def index():
    return "🤖 Bot is running on Vercel!"

# Route للـ Webhook
@app.route("/", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    print("✅ Webhook received data:", data)  # لمراقبة وصول الطلبات في لوج Vercel
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return "OK"

# لا تقم بإضافة app.run لأن Vercel يدير التشغيل تلقائيًا
