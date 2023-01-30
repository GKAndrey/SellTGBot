from modules.models import *
from modules.func import *

# def add_product_sql(id): #Сохранение нового товара
#     add_product_sql = '''
# INSERT INTO products
# VALUES (?,?,?,?,?,?);
# '''
#     cursor.execute(add_product_sql, (product_list[id].id, product_list[id].name, product_list[id].tags, product_list[id].opis, product_list[id].path_photo, product_list[id].maney))
#     con.commit()

# def get_product():
#     get_product = '''
#     SELECT tegs FROM products;'''
#     cursor.execute(get_product)
#     result = cursor.fetchall()
#     for i in result:
#         cursor.execute("SELECT name FROM products WHERE id = ?;", i)
#         name = cursor.fetchall()
#         cursor.execute("SELECT tags FROM products WHERE id = ?;", i)
#         tags = cursor.fetchall()
#         cursor.execute("SELECT opis FROM products WHERE id = ?;", i)
#         opis = cursor.fetchall()
#         cursor.execute("SELECT maney FROM products WHERE id = ?;", i)
#         maney = cursor.fetchall()
#         tags = tags[0].split("/")
#         product_list.append(Product(result[0], name[0],tags,opis[0],maney[0]))



def findfiles_on_search(message):
    if message.text == 'По названию 🔤':
        msg = bot.send_message(message.chat.id,"Введите название товара",reply_markup=types.ReplyKeyboardRemove())
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