import telebot
import podliybuttons as pb
import podliydb as pd
from geopy import Nominatim
import webbrowser

bot = telebot.TeleBot('7094307129:AAHf8MgTkC9_u-7EtYUnGyngDNT4-IJyLfs')
geolocator = Nominatim(
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0'
    'Safari/537.36'
)


@bot.message_handler(commands=['start'])

def start(message):
    gr_id = message.from_user.id
    check = pd.check_user(gr_id)
    if check:
        bot.send_message(gr_id, "Hello, I'm glad to see you",
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(gr_id, 'Hi!\n'
                                  'Let\'s do registration!\n'
                                  'Enter your name',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)


def get_name(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, 'Cool, and now send me your number please!',
                     reply_markup=pb.user_num())
    bot.register_next_step_handler(message, get_number, user_name)


def get_number(message, user_name):
    user_id = message.from_user.id
    if message.contact:
        user_number = message.contact.phone_number
        bot.send_message(user_id, 'Now send me a location!',
                         reply_markup=pb.user_loc())
        bot.register_next_step_handler(message, get_location,
                                       user_name, user_number)
    else:
        bot.send_message(user_id, 'Send a number through the button!!',
                         reply_markup=pb.user_num())
        bot.register_next_step_handler(message, get_number, user_name)


def get_location(message, user_name, user_number):
    user_id = message.from_user.id
    if message.location:
        user_location = geolocator.reverse(f'{message.location.latitude}, '
                                           f'{message.location.longitude}')
        pd.register(user_id, user_name, user_number, str(user_location))
        bot.send_message(user_id, 'Registration passed successfully')
    else:
        bot.send_message(user_id, 'Send a location through the button!!',
                         reply_markup=pb.user_loc())
        bot.register_next_step_handler(message, get_location,
                                       user_name, user_number)


@bot.message_handler(commands= ['site'])
def site(message):
    webbrowser.open('https://github.com/CamillaKleymen/podliybot_repositoriy.git?authuser=0')
@bot.message_handler(commands=['hello'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}{message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'you will not get a kind a help')


@bot.message_handler(commands=['fishkibota'])
def main(message):
    bot.send_message(message.chat.id, 'This bot was created in a deep night, when a creator did not know which bot create. So and then author decided create a bot which can find different person and make potential friends ')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}{message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == '/start':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}{message.from_user.last_name}')

bot.polling()
