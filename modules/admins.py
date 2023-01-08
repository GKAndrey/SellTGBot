from modules.settings import *
from modules.products import *

@bot.message_handler(commands=["admin"])
def admins_call(message):
    admins(message)

def adm_pls(ID):
    admin_list.append(ID)
    with open("Admins.json", "w") as write_file:
        json.dump(admin_list, write_file)

def adm_mns(ID):
    try:
        admin_list.remove(ID)
        with open("Admins.json", "w") as write_file:
            json.dump(admin_list, write_file,sort_keys=False,indent=4,ensure_ascii=False,)
    except:
        pass

@bot.message_handler(commands=["admins"])
def admins(message):
    print(message.from_user.id)
    if 1439133134 == message.from_user.id:
        try:
            messs = message.text.split("", 2)[1]
            messs1 = message.text.split("", 2)[2]
        except:
            bot.send_message(message.chat.id, "После команды должен быть ID нового администратора.")

@bot.message_handler(commands=["remove"])
def add(message):
    if message.from_user.id in admin_list:
        txt_mes = message.text.split()
        if len(txt_mes) > 1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            for i in os.listdir(path_Im_Prod):
                ind = i.replace(".png")
                reamove_prod = types.KeyboardButton(f"/remove {ind}")
                markup.add(reamove_prod)
            cansel = types.KeyboardButton("/cansel выход из меню админов")
            markup.add(cansel)
            bot.send_message(message.chat.id, 'Выберите вариант из ниже перечисленныхьили просто введите "/remove (Название обьявления)"', reply_markup=markup)
        else:
            remove_prod()
            up_list_prod()

def admins(message):
    if message.from_user.id in admin_list:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        add_prod = types.KeyboardButton("/add добавить обьявление")
        remove_prod = types.KeyboardButton("/remove удалить обьявление.")
        cansel = types.KeyboardButton("/cansel выход из меню админов")
        markup.add(add_prod, remove_prod, cansel)
        bot.send_message(message.chat.id, "Какая опция вам нужна?", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'Вы (@{message.from_user.username}) не являетесь админом бота. В случае вопросов, предложений или вакансий обращайтесь в тех. поддержку (она же и "Обратная связь" /question).')