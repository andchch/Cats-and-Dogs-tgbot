import random
import argparse
import re
import requests
import telebot
from telebot import types


parser = argparse.ArgumentParser()
parser.add_argument('key', type=str)
args = parser.parse_args()


bot = telebot.TeleBot(args.key)


def get_url(who):
    if who == 'Dog':
        url = requests.get('https://random.dog/woof.json').json()['url']
        file_extension = re.search("([^.]*)$", url).group(1).lower()
        return url, file_extension
    if who == 'Cat':
        typecat = random.randint(0, 1)
        if typecat == 0:



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     'Привет, я - самый полезный бот в тг')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dog_btn = types.KeyboardButton('Dog')
    cat_btn = types.KeyboardButton('Cat')
    markup.add(dog_btn)
    markup.add(cat_btn)
    bot.send_message(message.chat.id, 'Doggo or kitties?', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == 'Dog':
        dog = get_url('Dog')
        if dog[1] == 'gif':
            bot.send_animation(message.chat.id, dog[0])
        elif dog[1] == 'mp4':
            bot.send_video(message.chat.id, dog[0])
        else:
            bot.send_photo(message.chat.id, dog[0])
    elif message.text == 'Cat':
        cat = get_url('Cat')
        if cat[1] == 1:
            bot.send_animation(message.chat.id, cat[0])
        else:
            bot.send_photo(message.chat.id, cat[0])


bot.infinity_polling()
