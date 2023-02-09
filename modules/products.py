from modules.settings import telebot, os, bot, cursor, bot, path_Im_Prod
from modules.func import *

def findfiles_on_search(message):
    if message.text == 'По названию 🔤':
        msg = bot.send_message(message.chat.id,"Введите название товара",reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, find_on_search)
    # bot.register_next_step_handler(msg, start_bot)
    elif message.text == "Закрыть ❌":
        bot.send_message(message.chat.id,"Возвращаемся обратно")
        murk(message)

def find_on_search(message):
    try:
        name_prod = '''
    SELECT id FROM products WHERE name = ?;
    '''
        name = cursor.fetchall(cursor.execute(name_prod, message.text))
        bot.send_photo(os.path.join(path_Im_Prod, str(id)))
        description_prod = '''
    SELECT opis FROM products WHERE name = ?;
    '''
        cursor.execute(description_prod, message.text) #description = opis
        opis = cursor.fetchall()
        money_prod = '''
    SELECT maney FROM products WHERE name = ?;
    '''
        cursor.execute(money_prod,message.text)
        maney = cursor.fetchall()
        msg = f'''
        🔤Имя: {name}
        🧾Описание: {description_prod}
        💵Цена: {money_prod}
        '''
        bot.send_message(message.chat.id,msg)

        #имя, опписание , цена
    except:
        msg = bot.send_message(message.chat.id,"Такого товара не существует. Повторите попытку:",reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, findfiles_on_search)