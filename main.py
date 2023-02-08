print('Загрузка программы...') 
import telebot 
from telebot import types  
bot = telebot.TeleBot('6292695080:AAGt_t9K2DMIUnaKEVFcDQuUPDSAOTSxL1k')  
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
        b2 = types.KeyboardButton('Новинки')
        b3 = types.KeyboardButton('Назад')
        markup.add(b1) 
        markup.add(b2)
        markup.add(b3)
    if name_kb == 'look': 
        b1 = types.KeyboardButton('По названию') 
        b2 = types.KeyboardButton('По актёру')
        b3 = types.KeyboardButton('Назад')
        markup.add(b1) 
        markup.add(b2)
        markup.add(b3)
    return markup 
 
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
   
bot.infinity_polling()
