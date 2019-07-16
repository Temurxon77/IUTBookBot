import telebot
from telebot.types import InlineKeyboardButton,ReplyKeyboardMarkup

def Buttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.row(InlineKeyboardButton('TimeTable'),InlineKeyboardButton('Books'))
    return markup