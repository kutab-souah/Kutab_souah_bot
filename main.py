import os
from flask import Flask, send_from_directory
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import threading

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)

# هاد اللينك هو ديال الميني آب
WEBAPP_URL = "https://kutab-souah-bot.onrender.com"

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📚 افتح المكتبة", web_app=WebAppInfo(url=WEBAPP_URL)))
    bot.send_message(message.chat.id, "📚 مرحبا في KUTAB-SOUAH\n\nورك على الزر باش تدخل للمكتبة!", reply_markup=markup)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

def run_bot():
    bot.infinity_polling()

if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
