from telebot import types

def user_num():
   
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    number = types.KeyboardButton('send a number to podliy bot', request_contact=True)
    kb.add(number)
    return kb


def user_loc():
   
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)  
    location = types.KeyboardButton('send a location to podliy bot', request_location=True)
    kb.add(location)
    return kb
