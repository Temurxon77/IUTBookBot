import telebot
from telebot.types import InlineKeyboardButton,ReplyKeyboardMarkup

def Sophomore_2Sem():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.row(InlineKeyboardButton('Academic English 4'),InlineKeyboardButton('Basic Korean 2'))
    markup.row(InlineKeyboardButton('Circuit and Lab'),InlineKeyboardButton('Engineering Mathematics'))
    markup.row(InlineKeyboardButton('System Programming'),InlineKeyboardButton('Computer Architecture'))
    markup.row(InlineKeyboardButton('Internet programming'))
    return markup

