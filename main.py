import os
from flask import Flask
from threading import Thread
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "Bot is Alive!"

@bot.message_handler(commands=['start'])
def start(message):
    btn = telebot.types.InlineKeyboardButton("📚 افتح المكتبة", web_app=telebot.types.WebAppInfo(url="https://google.com"))
    markup = telebot.types.InlineKeyboardMarkup().add(btn)
    bot.send_message(message.chat.id, "مرحبا فـ KUTAB-SOUAH 📚", reply_markup=markup)

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

Thread(target=run_flask).start()
bot.infinity_polling()
