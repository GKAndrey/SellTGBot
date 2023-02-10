from modules.products import findfiles_on_search
from modules.settings import telebot, bot, admin_list, cursor, con, last_photo_indx
from modules.user_log import us_log, its_user

def start(message):
    global its_user
    us_log(message)
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("👋 Перейти к меню")
    markup.add(btn1)
    msg = bot.send_message(message.from_user.id, "👋 Привет! Я магазин ShopBot!", reply_markup=markup)
    bot.register_next_step_handler(msg, start_bot)



def murk(mess):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Товары 🛒')
    btn2 = telebot.types.KeyboardButton('Опции ⚙')
    cns = telebot.types.KeyboardButton('Закрыть ❌')
    if its_user[mess.from_user.id].admin == 1:
        btn3 = telebot.types.KeyboardButton('Админ панель 🎮')
        markup.add(btn1, btn2, btn3, cns)
    else:
        markup.add(btn1, btn2, cns)
    msg = bot.send_message(mess.from_user.id, 'Выберете что вам нужно:', reply_markup=markup)
    bot.register_next_step_handler(msg, check_answ)



def start_bot(message):
    if message.text == '👋 Перейти к меню':
        murk(message)
    elif message.text == '\start':
        start(message)
        return
    else:
        bot.send_message(message.from_user.id, 'Просим вас заранее, не стоит ломать логику бота, врятли у вас это получится, к тому же, хуже вы сделаете только себе, если администрация заметит вас как виновника и добавит в черный список. Если это не намерянно, то будьте окуратнее и пользуйтесь кнопками, они не только для красоты были созданы.')
        msg = bot.send_message(message.from_user.id, 'Выберете что вам нужно:')
        bot.register_next_step_handler(msg, check_answ)



def check_answ(message):
    if message.text == 'Товары 🛒':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_search_ontag = telebot.types.KeyboardButton('По тегу 🏷️')
        btn_search_onname = telebot.types.KeyboardButton('По названию 🔤')
        btn_close_products = telebot.types.KeyboardButton('Закрыть ❌')
        markup.add(btn_search_onname,btn_search_ontag,btn_close_products)
        msg = bot.send_message(message.from_user.id, 'Поиск:', reply_markup=markup)
        bot.register_next_step_handler(msg, findfiles_on_search)

    elif message.text == 'Опции ⚙':
        opt(message)

    elif message.text == 'Админ панель 🎮':
        if its_user[message.from_user.id].admin == 1:
            admin_menu(message)
        else:
            bot.send_message(message.chat.id, f'Вы (@{message.from_user.username}) не являетесь админом бота. В случае вопросов, предложений или вакансий обращайтесь в тех. поддержку (Помощь ❓).')

    elif message.text == 'Закрыть ❌':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton('/start')
        markup.add(btn1)
        bot.send_message(message.chat.id, "Буду ждать новой встречи.", reply_markup=markup)

    elif message.text == '\start':
        start(message)
        return

    else:
        bot.send_message(message.from_user.id, 'Просим вас, не стоит ломать логику бота, врятли у вас это получится, к тому же, хуже вы сделаете только себе, если администрация заметит вас как виновника и добавит в черный список. Если это не намерянно, то будьте окуратнее и пользуйтесь кнопками, они не только для красоты были созданы.')
        msg = bot.send_message(message.from_user.id, 'Выберете что вам нужно:')
        bot.register_next_step_handler(msg, check_answ)



def optional(message):
    if message.text == "Информация 📗":
        mess = '''**Инфо**
Данный бот был создан, в большей части, в образовательных и развлекательных целях. Коммерческого использования не имеет, оплата и продукция исключительно виртуальная.
Большое спасибо, что решили поинтересоваться этой информацией, надеемся, вы еще встретитесь с нашей продукцией в более серьезном мотиве и оно будет вам реально полезно
А пока что, можем лишь предложить поддержать создателей копеечкой '''
        bot.send_message(message.chat.id,mess,parse_mode = "Markdown")
        bot.send_message(message.chat.id,"Бот создан: **Ещё в разработке**", parse_mode = "Markdown")
        bot.send_message(message.chat.id,"Над ботом работали:") #тут можно отметить девов (разрабов)

    elif message.text == 'Помощь ❓':
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton("Отмена", callback_data="close_quest")
        markup.add(btn1)
        bot.send_message(message.from_user.id, '--------------------------------------', reply_markup=telebot.types.ReplyKeyboardRemove())
        msg = bot.send_message(message.from_user.id, 'Введите свой вопрос:', reply_markup=markup)
        bot.register_next_step_handler(msg, quests)

    elif message.text == "Выход ❌":
        murk(message)

    elif message.text == '\start':
        start(message)
        return

    elif message.text == "Оповещения 🔔":
        inlinemarkups = telebot.types.InlineKeyboardMarkup()
        inlinemarkups.row_width = 2
        btn1 = telebot.types.InlineKeyboardButton("Выключить  оповещения 🔕", callback_data="cb_off")
        btn2 = telebot.types.InlineKeyboardButton("Включить оповещения 🔔", callback_data="cb_on")
        close_menu = telebot.types.InlineKeyboardButton("Выйти в меню опций ⚙", callback_data="cb_close")
        inlinemarkups.add(btn1, btn2, close_menu)
        bot.send_message(message.chat.id, "Выключить оповещения?", reply_markup=inlinemarkups)



def quests(message):
    global question_list
    question_list.append((message.chat.id, message.from_user.username, message.text))
    orders_sql = '''
    INSERT INTO orders
    VALUES (?,?,?);
    '''
    cursor.execute(orders_sql, question_list[-1])
    con.commit()
    for i in admin_list:
        bot.send_message(i,f"У вас новый вопрос. Всего {len(question_list)} вопросов.")
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Товары 🛒')
    btn2 = telebot.types.KeyboardButton('Информация 📗')
    btn4 = telebot.types.KeyboardButton('Помощь ❓')
    cns = telebot.types.KeyboardButton('Закрыть ❌')
    if its_user[message.from_user.id].admin == 1:
        btn3 = telebot.types.KeyboardButton('Админ панель 🎮')
        markup.add(btn1, btn2, btn3, btn4, cns)
    else:
        markup.add(btn1, btn2, btn4, cns)
    msg = bot.send_message(message.chat.id,f"Вопрос отправлен, ожидайте ответа. Ваш вопрос находится под номером {len(question_list)} в очереди", reply_markup=markup)
    bot.register_next_step_handler(msg, check_answ)



def opt(message):
    btn1 = telebot.types.KeyboardButton('Информация 📗')
    btn2 = telebot.types.KeyboardButton('Помощь ❓')
    btn3 = telebot.types.KeyboardButton('Оповещения 🔔')
    cns = telebot.types.KeyboardButton('Выход ❌')
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn1, btn2, btn3, cns)
    msg = bot.send_message(message.chat.id,"Выберите действие из следующих вариантов:", reply_markup=markup)
    bot.register_next_step_handler(msg, optional)



def mud(call):
    bot.send_message(call.id, "Ввод отменен. Возврат к главному меню.")
    murk(call)


#Админская часть


def adm_pls(ID):
    add_admin = f'''
UPDATE users
SET admin = '1'
WHERE id = '{ID}';
'''
    cursor.execute(add_admin)
    con.commit()



def adm_mns(ID):
    add_admin = f'''
UPDATE users
SET admin = NULL
WHERE id = '{ID}';
'''
    cursor.execute(add_admin)
    con.commit()



def admin_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) #🛠
    add_prod = telebot.types.KeyboardButton("Работа над продукцией 🏷✏")
    remove_prod = telebot.types.KeyboardButton("Админский состав 👮‍♂️") #🗑
    qst = telebot.types.KeyboardButton("Вопросы пользователей ❓")
    cansel = telebot.types.KeyboardButton("Выход из меню админов 🛑")
    markup.add(add_prod, remove_prod, qst, cansel)
    msg = bot.send_message(message.chat.id, "Ого, важные люди. Какова цель вашего визита?", reply_markup=markup)
    bot.register_next_step_handler(msg, next_admin_click)



def next_admin_click(message):
    if message.text == "Работа над продукцией 🏷✏":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = telebot.types.KeyboardButton("Просмотреть список товаров")
        btn2 = telebot.types.KeyboardButton("Добавить продукт ➕")
        btn3 = telebot.types.KeyboardButton("удалить продукт ✂")
        btn4 = telebot.types.KeyboardButton("Выйти в меню админов 👮‍♂️")
        markup.add(btn1, btn2, btn3, btn4)
        # msg = bot.send_message(message.chat.id, "Пришлите мне Название для обьявления.", reply_markup=telebot.types.ReplyKeyboardRemove())
        # bot.register_next_step_handler(msg, add1)
    elif message.text == "Админский состав 👮‍♂️":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        show_adm_list_btn = telebot.types.KeyboardButton("Просмотреть список админов 📄")
        add_adm_btn = telebot.types.KeyboardButton("Добавить админа ➕")
        del_adm_btn = telebot.types.KeyboardButton("Удалить админа ✂")
        exit_on_menuadm_btn = telebot.types.KeyboardButton("Выйти в меню админов 👮‍♂️")
        markup.add(show_adm_list_btn, add_adm_btn, del_adm_btn, exit_on_menuadm_btn)
        msg = bot.send_message(message.chat.id, "Выберите нужное действие из католога:", reply_markup=markup)
        bot.register_next_step_handler(msg, adm_chec)
    elif message.text == "Вопросы пользователей ❓":
        user_quest_work(message)
        msg = bot.send_message(message.chat.id, "Что дальше?")
        bot.register_next_step_handler(msg, next_admin_click)
    elif message.text == '\start':
        start(message)
        return
    elif message.text == "Выход из меню админов 🛑":
        bot.send_message(message.chat.id, "Вы вышли из меню админов.")
        murk(message)


def adm_chec(message):
    if message.text == "Просмотреть список админов 📄":
        sqlreq = '''
        SELECT user_name FROM admins WHERE admin = 1;'''
        cursor.execute(sqlreq)
        fetchall = cursor.fetchall()
        msg = ''''''
        num = 1
        for i in fetchall:
            msg += (f'''{num}) {i[0]}\n''')
            bot.send_message(message.chat.id, msg)
            num += 1
        msg = bot.send_message(message.chat.id, "Выберите нужное действие из каталога:")
        bot.register_next_step_handler(msg, adm_chec)
    if message.text == "Добавить админа ➕":
        pass
    if message.text == "Удалить админа ✂":
        msg = bot.send_message(message.chat.id, "Выберите нужное действие из каталога:")
        bot.register_next_step_handler(msg, del_adm)
    if message.text == "Выйти в меню админов 👮‍♂️":
        murk(message)


def del_adm(message):
    sqlreq = '''
    SELECT user_name FROM admins WHERE admin = 1;
    '''
    cursor.execute(sqlreq)
    fetchall = cursor.fetchall()
    admin_name = fetchall[message.text - 1]
    sqlreq2 = '''
    SELECT id FROM admins WHERE user_name = ?;
    '''
    cursor.execute(sqlreq2, admin_name)
    fetchall2 = cursor.fetchall()
    adm_mns(fetchall2[0])

def add1(message):
    global prod_us_var
    # product_list.append(Product(message.text))
    if message.content_type == "text" and message.text != "":
        prod_us_var = []
        prod_us_var.append(last_photo_indx + 1)
        msg = bot.send_message(message.chat.id, "Пришлите мне **Фото** для обьявления (.png).", parse_mode = "Markdown")
        prod_us_var.append(message.text)
        bot.register_next_step_handler(msg, add2)



def add2(message):
    global prod_us_var
    if message.content_type == "photo":
        file = bot.get_file(message.photo[-1].file_id)
        file = bot.download_file(file.file_path)
        with open(f'{prod_us_var[0]}.png', 'wb') as f:
            f.write(file)
        msg = bot.send_message(message.chat.id, 'Фото получено. Введите **Описание** обьявления/продукта одним сообщением.',parse_mode = "Markdown")
        bot.register_next_step_handler(msg, add3)
    else:
        msg = bot.send_message(message.chat.id, 'Отправте пожалуйста картинку формата .pdf')
        bot.register_next_step_handler(msg, add2)



def add3(message):
    global prod_us_var
    if message.content_type == "text" and message.text != "":
        prod_us_var.append(message.text)
        bot.send_message(message.chat.id, 'Пришлите мне **Теги** для обьявления. Пример: "#Спорт#Мода#Електроника".')



def user_quest_work(message):
    a = cursor.execute("SELECT * FROM orders;")
    a = a.fetchall()
    nomer = 1
    for i in a:
        mess = f'''
Вопрос №{nomer}

**@{i[1]}**
{i[2]}'''
        bot.send_message(message.chat.id, mess, parse_mode = "Markdown")
        nomer += 1
    bot.send_message(message.chat.id, "К какому вопросу желаете перейти? (Введите номер вопроса)", parse_mode = "Markdown")



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
        cursor.execute(f"DELETE FROM orders WHERE id={question_list[int(id)-1][0]}, text={question_list[int(id)-1][2]};")
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
