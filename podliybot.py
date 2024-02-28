# import telebot
# import podliybuttons as pb
# import podliydb as pd
# from geopy import Nominatim
# import types
# my_chat_id = 631104511
#
#
#
# bot = telebot.TeleBot('7094307129:AAHf8MgTkC9_u-7EtYUnGyngDNT4-IJyLfs')
# geolocator = Nominatim(
#     user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0'
#     'Safari/537.36'
# )
#
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_dice(message.chat.id)
#     keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     button1 = types.KeyboardButton(text='Registration')
#     button2 = types.KeyboardButton(text='Menu')
#     button3 = types.KeyboardButton(text='About us')
#     keyboard.add(button1, button2, button3)
#     bot.send_message(message.chat.id, 'Good afternoon! Fast food "talabalunch" greeting you!', reply_markup=keyboard)
#
# def registr(message):
#     user_id = message.from_user.id
#     check = pd.check_user(user_id)
#     if check:
#         bot.send_message(user_id, 'Welcome to our fast food!',
#                          reply_markup=telebot.types.ReplyKeyboardRemove())
#     else:
#         bot.send_message(user_id, 'Hello! '
#                                   'Lets make registration!\n'
#                                   'Enter your name!',
#                          reply_markup=telebot.types.ReplyKeyboardRemove())
#         bot.register_next_step_handler(message, get_name)
#
#
# def get_name(message):
#     user_id = message.from_user.id
#     user_name = message.text
#     bot.send_message(user_id, 'Cool, now send a number!',
#                      reply_markup=pb.user_num())
#     bot.register_next_step_handler(message, get_number, user_name)
#
#
# def get_number(message, user_name):
#     user_id = message.from_user.id
#     if message.contact:
#         user_number = message.contact.phone_number
#         bot.send_message(user_id, 'And now send a location!',
#                          reply_markup=pb.user_loc())
#         bot.register_next_step_handler(message, get_location,
#                                        user_name, user_number)
#     else:
#         bot.send_message(user_id, 'Send a location through button!',
#                          reply_markup=pb.user_num())
#         bot.register_next_step_handler(message, get_number, user_name)
#
#
#
# def get_location(message, user_name, user_number):
#     user_id = message.from_user.id
#     if message.location:
#         user_location = geolocator.reverse(f'{message.location.latitude}, '
#                                            f'{message.location.longitude}')
#         pb.register(user_id, user_name, user_number, str(user_location))
#         bot.send_message(user_id, 'Registration passed successfully!')
#     else:
#         bot.send_message(user_id, 'Send a location through button!',
#                          reply_markup=pb.user_loc())
#         bot.register_next_step_handler(message, get_location,
#                                        user_name, user_number)
#
#
# def info_func(message):
#     keyboard = types.InlineKeyboardMarkup()
#     url_button = types.InlineKeyboardButton(text='Link to our website', url='https://kfc.com/')
#     keyboard.add(url_button)
#     bot.send_message(message.chat.id, 'Info about the fastfood', reply_markup=keyboard)
#
# ###
# def send_request(message):
#     mes = f'New order: {message.text}'
#     bot.send_message(my_chat_id, mes)
#     bot.send_message(message.chat.id, 'Thanks for your order! Our staff will contact you soon.')
#
# def send_service(message):
#     services = [
#         '1. Make a year report',
#         '2. Pay a tax',
#         '3. Account a budget'
#     ]
#     bot.send_message(message.chat.id, '\n'.join(services))
#
# @bot.message_handler(content_types=['text'])
# def repeat_all_messages(message):
#     if message.text.lower() == 'about us':
#         info_func(message)
#     elif message.text.lower() == 'make an order':
#         bot.send_message(message.chat.id, 'We would be glad to serve you! Please leave your contact data.')
#         bot.register_next_step_handler(message, send_request)
#     elif message.text.lower() == 'service':
#         send_service(message)
#
# if __name__ == '__main__':
#     bot.infinity_polling()





import sqlite3
from telebot import types
from geopy import Nominatim
import telebot
import podliybuttons as pb
my_chat_id = 631104511

# Establish connection to the SQLite database
connection = sqlite3.connect('podliybot.db', check_same_thread=False)
sql = connection.cursor()

geolocator = Nominatim(
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0'
    'Safari/537.36'
)

bot = telebot.TeleBot('7094307129:AAHf8MgTkC9_u-7EtYUnGyngDNT4-IJyLfs')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_dice(message.chat.id)
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Registration')
    button2 = types.KeyboardButton(text='Menu')
    button3 = types.KeyboardButton(text='About us')
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Good afternoon! Fast food "talabalunch" greeting you!', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.text.lower() == 'about us':
        info_func(message)
    elif message.text.lower() == 'make an order':
        bot.send_message(message.chat.id, 'We would be glad to serve you! Please leave your contact data.')
        bot.register_next_step_handler(message, send_request)
    elif message.text.lower() == 'service':
        send_menu(message)

def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='Link to our website', url='https://kfc.com/')
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Info about the fastfood', reply_markup=keyboard)

def send_request(message):
    mes = f'New order: {message.text}'
    bot.send_message(my_chat_id, mes)
    bot.send_message(message.chat.id, 'Thanks for your order! Our staff will contact you soon.')

def send_menu(message):
    services = [
        '1. hot dog',
        '2. burger',
        '3. lavash'
    ]
    bot.send_message(message.chat.id, '\n'.join(services))


def check_user(fd_id):
    check = sql.execute('SELECT * FROM podlie_users WHERE id=?;', (fd_id,))
    if check.fetchone():
        return True
    else:
        return False


def register(id, name, number, location):
    sql.execute('INSERT INTO podlie_users VALUES(?, ?, ?, ?);', (id, name, number, location))
    connection.commit()


if __name__ == '__main__':
    bot.infinity_polling()


