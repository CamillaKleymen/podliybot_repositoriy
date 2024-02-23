from telebot import types

def user_num():
   
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    number = types.KeyboardButton('Please send a number', request_contact=True)
    kb.add(number)
    return kb


def user_loc():
   
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)  
    location = types.KeyboardButton('Please send a location', request_location=True)
    kb.add(location)
    return kb