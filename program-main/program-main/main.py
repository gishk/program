print('Загрузка программы...') 
import telebot 
from telebot import types
import requests
import sqlite3
bot = telebot.TeleBot('6292695080:AAGt_t9K2DMIUnaKEVFcDQuUPDSAOTSxL1k')
sqlite_connection = sqlite3.connect('data.db', check_same_thread=False)
cursor = sqlite_connection.cursor()
print('Бот запущен!')
 
def controler_keyboard(name_kb): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    if name_kb == 'main':
        b1 = types.KeyboardButton('Популярные фильмы') 
        b2 = types.KeyboardButton('Найти фильм') 
        markup.add(b1) 
        markup.add(b2)
    if name_kb == 'pf': 
        b1 = types.KeyboardButton('Жанры') 
        b2 = types.KeyboardButton('Назад')
        markup.add(b1) 
        markup.add(b2)
    if name_kb == 'look': 
        b1 = types.KeyboardButton('По названию')
        b2 = types.KeyboardButton('По году')
        b3 = types.KeyboardButton('Назад')
        markup.add(b1)
        markup.add(b2)
    if name_kb == 'list': 
        b1 = types.KeyboardButton('Боевик') 
        b2 = types.KeyboardButton('Ужасы')
        b3 = types.KeyboardButton('Фантастика')
        b4 = types.KeyboardButton('Комедия')
        markup.add(b1) 
        markup.add(b2)
        markup.add(b3)
        markup.add(b4) 
    return markup 

def title(message):
    cursor.execute(f"SELECT * FROM films WHERE title LIKE '%{message.text}%'")
    films = cursor.fetchall()
    for film in films:
         bot.send_message(message.chat.id, "" + film[2] + "\n\n Год фильма: " + str(film[3]) + "\n\nСмотреть фильм: " + request(film[4]) + "" )

def yaers(message):
    cursor.execute(f"SELECT * FROM films WHERE year = {message.text}")
    films = cursor.fetchall()
    for film in films:
        bot.send_message(message.chat.id, "" + film[2] + "\n\n Год фильма: " + str(film[3]) + "\n\nСмотреть фильм: " + request(film[4]) + "" )

def request(url):
    res = requests.get('https://clck.ru/--?url=' + url)
    return res.text

@bot.message_handler(commands=['start']) 
def start(message): 
    uid = message.chat.id 
    name = message.from_user.first_name 

    bot.send_message(uid, 'Добро пожаловать!', reply_markup=controler_keyboard('main'))

@bot.message_handler(content_types=['text']) 
def main_controler(message): 
    uid = message.chat.id 
    name = message.from_user.first_name 
    
    if message.text == 'Популярные фильмы':
        bot.send_message(uid, 'Каким способом вы хотите найти фильм?', reply_markup=controler_keyboard('pf'))

    if message.text == 'Найти фильм':
        bot.send_message(uid, 'Как вы хотите найти фильм?', reply_markup=controler_keyboard('look'))

    if message.text == 'По названию':
        bot.send_message(uid, 'Введите текст поиска...')
        bot.register_next_step_handler(message, title)

    if message.text == 'По году':
        bot.send_message(uid, 'Введите год...')
        bot.register_next_step_handler(message, yaers)

    if message.text == 'Жанры':
        bot.send_message(uid, 'Список', reply_markup=controler_keyboard('list') )

    if message.text == 'Боевик':
        bot.send_message(uid, 'Боевики:', reply_markup=controler_keyboard('list') )
        cursor.execute("SELECT * FROM films WHERE genre = 'боевик'")
        films = cursor.fetchall()
        for film in films:
            bot.send_message(uid, "" + film[2] + "\n\n Год фильма: " + str(film[3]) + "\n\nСмотреть фильм: " + request(film[4]) + "" )
    if message.text == 'Ужасы':
        bot.send_message(uid, 'Ужас:', reply_markup=controler_keyboard('list') )
        cursor.execute("SELECT * FROM films WHERE genre = 'ужасы'")
        films = cursor.fetchall()
        for film in films:
           bot.send_message(uid, "" + film[2] + "\n\n Год фильма: " + str(film[3]) + "\n\nСмотреть фильм: " + request(film[4]) + "" )
    if message.text == 'Фантастика':
        bot.send_message(uid, 'Фантастика:', reply_markup=controler_keyboard('list') )
        cursor.execute("SELECT * FROM films WHERE genre = 'фантастика'")
        films = cursor.fetchall()
        for film in films:
            bot.send_message(uid, "" + film[2] + "\n\n Год фильма: " + str(film[3]) + "\n\nСмотреть фильм: " + request(film[4]) + "" )
    if message.text == 'Комедия':
        bot.send_message(uid, 'Комедия:', reply_markup=controler_keyboard('list') )
        cursor.execute("SELECT * FROM films WHERE genre = 'комедия'")
        films = cursor.fetchall()
        for film in films:
            bot.send_message(uid, "" + film[2] + "\n\n Год фильма: " + str(film[3]) + "\n\nСмотреть фильм: " + request(film[4]) + "" )

    if message.text == 'Назад':
        bot.send_message(uid, 'Главное меню:', reply_markup=controler_keyboard('main'))

bot.infinity_polling()
