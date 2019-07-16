#importing imortant things
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton,KeyboardButton,InlineKeyboardMarkup
from config import Token
import cairosvg
import mysql.connector
import re
from buttons import Buttons
import requests
bot = telebot.TeleBot(Token.TOKEN)
user_data = {"user_id":"None"}

@bot.message_handler(commands=['start'])
def Start(message):
    try:
        chat_id = message.chat.id
        #print(message)
        userid = bot.reply_to(message,'Enter user ID:')
        bot.register_next_step_handler(userid,Ask_ID)
    except Exception as e:
        bot.send_message(chat_id,'ooops')
@bot.message_handler(func=lambda mess: "TimeTable" == mess.text, content_types=['text'])
def Show_Timetable(message):
    try:
        chat_id = message.chat.id
        URL = 'http://34.76.166.90/tt/byStudentId/'+user_data["user_id"]
        svg = requests.get(URL).content
        cairosvg.svg2png(bytestring=svg,write_to="sunny.png")
        timetable_data = open('sunny.png', 'rb')
        bot.send_photo(chat_id,timetable_data)
    except Exception as err:
        bot.send_message(chat_id,'ooops')

@bot.message_handler(func=lambda mess: "Books" == mess.text,content_types=['text'])
def Show_Books(message):
    try:
        chat_id = message.chat.id
        URL = 'http://34.76.166.90/book/byStudentId/'+user_data["user_id"]
        book = requests.get(URL).content
        bot.send_message(chat_id,book)
    except Exception as e:
        bot.send_message(chat_id,'ooops')

def Ask_ID(message):
    try:
        chat_id = message.chat.id
        userid = message.text
        regex = "^(U|u)(1){1}([5-8]){1}(1){1}([0-1]){1}([0-9]{3})$"
        check_id = re.match(regex,userid)
        if not check_id:
            msg = bot.reply_to(message, 'Wrong user ID: ')
            bot.register_next_step_handler(msg, Ask_ID)
        else:
            user_data["user_id"] = userid
            print(user_data["user_id"])
            bot.send_message(chat_id,'You are successfully registered now you can easily see your timetable  \n or download books from your course ',reply_markup=Buttons())
            #bot.register_next_step_handler(Show_Timetable,message)
    except Exception as e:
        bot.reply_to(message, 'oooops')



bot.polling(none_stop=True)