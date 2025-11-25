from config import token 
import random
import telebot

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я новая верся бота от Лёнчика")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока!")

@bot.message_handler(commands=['random_number'])
def random_number(message):
    n = int(message.text.split()[1]) if len(message.text.split()) > 1 else 10
    number = random.randint(1, n)
    bot.reply_to(message, number)


bot.polling()
