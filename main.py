import telebot
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home(): return "Bot is Alive"
def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive(): Thread(target=run).start()

TOKEN = '8635104387:AAGpL9j9f00Udnu--_VyzMhfjIMG6HjOSkA'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "البوت شغال أونلاين 24 ساعة يا ليجند!")

if __name__ == "__main__":
    keep_alive()
    bot.polling(none_stop=True)
  
