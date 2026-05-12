import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# --- Часть для Render (чтобы не падал) ---
app = Flask('')

@app.route('/')
def health_check():
    return "Бот работает!"

def keep_alive():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

threading.Thread(target=keep_alive).start()
# --- Конец части для Render ---

# --- Telegram-бот ---
TOKEN = os.environ.get("8077681625:AAE-fIOx__QlIg-ImrlHXsSDWihQrTyJaQs")

async def start(update: Update, context):
    await update.message.reply_text("Привет! Я бот и работаю на Render! 🚀")

async def echo(update: Update, context):
    await update.message.reply_text(f"Вы написали: {update.message.text}")

bot_app = Application.builder().token(TOKEN).build()
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

def run_bot():
    bot_app.run_polling(allowed_updates=Update.ALL_TYPES)

threading.Thread(target=run_bot).start()
