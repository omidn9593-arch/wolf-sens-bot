from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import os

TOKEN = os.getenv("BOT_TOKEN")

keyboard = [
    ["🎯 دریافت سنس"],
    ["⚙ آموزش ژیروسکوپ"],
    ["📺 یوتیوب WOLF"],
    ["👤 پشتیبانی"]
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐺 به WOLF Sens Bot خوش اومدی!\n\nیکی از گزینه‌های زیر را انتخاب کن.",
        reply_markup=reply_markup
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🎯 دریافت سنس":
        await update.message.reply_text(
            "🔥 این بخش به زودی تکمیل می‌شود."
        )

    elif text == "⚙ آموزش ژیروسکوپ":
        await update.message.reply_text(
            "🎮 آموزش ژیروسکوپ به زودی اضافه می‌شود."
        )

    elif text == "📺 یوتیوب WOLF":
        await update.message.reply_text(
            "لینک کانال یوتیوبت را اینجا قرار بده."
        )

    elif text == "👤 پشتیبانی":
        await update.message.reply_text(
            "@YourTelegramID"
        )

    else:
        await update.message.reply_text(
            "از منوی پایین یک گزینه را انتخاب کن."
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

    print("🐺 WOLF Sens Bot Started")

    app.run_polling()

if __name__ == "__main__":
    main()
