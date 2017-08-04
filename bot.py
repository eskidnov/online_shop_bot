# -*- coding: utf-8 -*-

import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
button1 = types.KeyboardButton(text='Новинки')
button2 = types.KeyboardButton(text='Каталог')
button3 = types.KeyboardButton(text='ID товара')
button4 = types.KeyboardButton(text='Оставить отзыв')
button5 = types.KeyboardButton(text='Разработчики')
keyboard.add(button1, button2, button3, button4, button5)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id, text=config.start, reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(chat_id=message.chat.id, text=config.help, reply_markup=keyboard)


@bot.message_handler(func=lambda item: item.text == 'Новинки', content_types=['text'])
def new(item):
    pass


@bot.message_handler(func=lambda item: item.text == 'Каталог', content_types=['text'])
def shop(item):
    pass


@bot.message_handler(func=lambda item: item.text == 'ID товара', content_types=['text'])
def item_id(item):
    pass


@bot.message_handler(func=lambda item: item.text == 'Оставить отзыв', content_types=['text'])
def callback(item):
    bot.send_message(chat_id=item.chat.id, text='Напишите ваши пожелания и предложения. Нам очень важно ваше мнение.')
    config.callback_flag = 1


@bot.message_handler(func=lambda item: item.text == 'Разработчики', content_types=['text'])
def Developers(item):
    bot.send_message(chat_id=item.chat.id, text=config.developers)


@bot.message_handler(content_types=['text'])
def restart(message):
    if config.callback_flag:
        # Отправить в бд или ещё куда
        bot.send_message(chat_id=message.chat.id, text='Спасибо за ваш отзыв!')
        config.callback_flag = 0

    bot.send_message(chat_id=message.chat.id, text='Выберите пункт меню или введите корректный запрос', reply_markup=keyboard)



if __name__ == '__main__':
    bot.polling(none_stop=True)