from modules.products import *

# def adm_pls(ID):
#     admin_list.append(ID)
#     with open("Admins.json", "w") as write_file:
#         json.dump(admin_list, write_file)

# def adm_mns(ID):
#     try:
#         admin_list.remove(ID)
#         with open("Admins.json", "w") as write_file:
#             json.dump(admin_list, write_file,sort_keys=False,indent=4,ensure_ascii=False,)
#     except:
#         pass

# @bot.message_handler(commands=["adminp"])
# def admins(message):
#     print(message.from_user.id)
#     if 1439133134 == message.from_user.id:
#         try:
#             messs = message.text.split("", 2)[1]
#             messs1 = message.text.split("", 2)[2]
#         except:
#             bot.send_message(message.chat.id, "После команды должен быть ID нового администратора.")

# @bot.message_handler(commands=["remove"])
# def add(message):
#     if message.from_user.id in admin_list:
#         txt_mes = message.text.split()
#         if len(txt_mes) > 1:
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#             for i in os.listdir(path_Im_Prod):
#                 ind = i.replace(".png")
#                 reamove_prod = types.KeyboardButton(f"/remove {ind}")
#                 markup.add(reamove_prod)
#             cansel = types.KeyboardButton("/cansel выход из меню админов")
#             markup.add(cansel)
#             bot.send_message(message.chat.id, 'Выберите вариант из ниже перечисленныхьили просто введите "/remove (Название обьявления)"', reply_markup=markup)
#         # else:
#         #     remove_prod()
#         #     up_list_prod()

def admin_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    add_prod = types.KeyboardButton("Добавить товар ➕")
    remove_prod = types.KeyboardButton("Удалить товар 🗑")
    qst = types.KeyboardButton("Меню поддержки ")
    cansel = types.KeyboardButton("Выход из меню админов 🛑")
    markup.add(add_prod, remove_prod, qst, cansel)
    msg = bot.send_message(message.chat.id, "Ого, важные люди. Какова цель вашего визита?", reply_markup=markup)
    bot.register_next_step_handler(msg, next_admin_click)

def next_admin_click(message):
    if message.text == "Добавить товар ➕":
        global adder
        msg = bot.send_message(message.chat.id, "Пришлите мне Название для обьявления.", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, add1)

def add1(message):
    product_list.append(Product(message.text))
    msg = bot.send_message(message.chat.id, "Пришлите мне **Фото** для обьявления.")
    bot.register_next_step_handler(msg, add2)

def add2(message):
    try:
        file = bot.get_file(message.photo[-1].file_id)
        file = bot.download_file(file.file_path)
        with open(f'{path_Im_Prod}/{product_list[-1].name}.png', 'wb') as f:
            f.write(file)
        product_list[-1].add_photo()
        bot.send_message(message.chat.id, 'Фото получено. Введите **Описание** обьявления/продукта.')
        adder = 3
    except:
        pass

@bot.message_handler(commands=["answer"])
def answ(message):
    global question_list
    try:
        id = message.text.split(' ', maxsplit = 2)[1]
        text = message.text.split(' ', maxsplit = 2)[2]
        bot.send_message(question_list[int(id)-1][0], f"Вы получили ответ на свой вопрос({question_list[int(id)-1][1]}):")
        bot.send_message(question_list[int(id)-1][0], text)
        del question_list[int(id)- 1]
        bot.reply_to(message, 'Ответ отправлен')
        cursor.execute("DELETE FROM orders WHERE id=? text=?;", [question_list[int(id)-1][0], question_list[int(id)-1][2]])
    except:
        bot.reply_to(message, "Нельзя ответить на несуществующий вопрос.")

@bot.message_handler(commands=["qq"])
def show_question(message):
    if question_list == []:
        bot.send_message(message.chat.id, f'Вопросов нет.')
    elif message.chat.id in admin_list:
        j = 1
        for i in question_list:
            bot.send_message(message.chat.id, f'{j}) {i[1]} (от @{i[2]})')
            j += 1

# @bot.message_handler(content_types=["text"])
# def text(message):
#     if message.from_user.id in admin_list:
#         global adder
#         if adder == 1:
#             product_list.append(Product(message.text))
#             adder = 2
#             bot.send_message(message.chat.id, "Пришлите мне **Фото** для обьявления.")
#         elif adder == 3:
#             product_list[-1].add_opis(message.text)
#             bot.send_message(message.chat.id, 'Пришлите мне **Теги** для обьявления. Пример: "#Спорт#Мода#Електроника".')
#             adder = 4
#         elif adder == 5:
#             bot.send_message(message.chat.id, 'Все готово, обьявление добавленно в каталог.')
#             adder = 0
#             product_list[-1].add_money(message.text)
#             save_prod()
#             up_list_prod()
#         elif adder == 4:
#             try:
#                 tegs = message.text.split("#")
#                 bot.send_message(message.chat.id, 'Введите цену на этот продукт.')
#                 product_list[-1].tegs_prod(tegs)
#                 adder = 5
#             except:
#                 bot.send_message(message.chat.id, 'Будьте внимательнее и следуйте инструкции (#Sport#Спорт#Електроника#Надо).')