from modules.admins import admin_menu
from modules.user_log import *

def murk(mess):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Товары 🛒')
    btn2 = types.KeyboardButton('Опции ⚙')
    cns = types.KeyboardButton('Закрыть ❌')
    if its_user[mess.from_user.id].admin == 1:
        btn3 = types.KeyboardButton('Админ панель 🎮')
        markup.add(btn1, btn2, btn3, cns)
    else:
        markup.add(btn1, btn2, cns)
    msg = bot.send_message(mess.from_user.id, 'Выберете что вам нужно:', reply_markup=markup)
    bot.register_next_step_handler(msg, check_answ)



def start_bot(message):
    if message.text == '👋 Перейти к меню':
        murk(message)
    else:
        bot.send_message(message.from_user.id, 'Просим вас заранее, не стоит ломать логику бота, врятли у вас это получится, к тому же, хуже вы сделаете только себе, если администрация заметит вас как виновника и добавит в черный список. Если это не намерянно, то будьте окуратнее и пользуйтесь кнопками, они не только для красоты были созданы.')
        msg = bot.send_message(message.from_user.id, 'Выберете что вам нужно:')
        bot.register_next_step_handler(msg, check_answ)



def check_answ(message):
    if message.text == 'Товары 🛒': #Над логикой работает Ваня #дальше этого сообщения оно не заходит хз почему
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_search_ontag = types.KeyboardButton('По тегу 🏷️')
        btn_search_onname = types.KeyboardButton('По названию 🔤')
        markup.add(btn_search_onname,btn_search_ontag)
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
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('/start')
        markup.add(btn1)
        bot.send_message(message.chat.id, "Буду ждать новой встречи.", reply_markup=markup)

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
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Отмена", callback_data="close_quest")
        markup.add(btn1)
        bot.send_message(message.from_user.id, '--------------------------------------', reply_markup=telebot.types.ReplyKeyboardRemove())
        msg = bot.send_message(message.from_user.id, 'Введите свой вопрос:', reply_markup=markup)
        bot.register_next_step_handler(msg, quests)
    elif message.text == "Выход ❌":
        murk(message)
    elif message.text == "Оповещения 🔔":
        inlinemarkups = types.InlineKeyboardMarkup()
        inlinemarkups.row_width = 2
        btn1 = types.InlineKeyboardButton("Выключить  оповещения 🔕", callback_data="cb_off")
        btn2 = types.InlineKeyboardButton("Включить оповещения 🔔", callback_data="cb_on")
        close_menu = types.InlineKeyboardButton("Выйти в меню опций ⚙", callback_data="cb_close")
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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Товары 🛒')
    btn2 = types.KeyboardButton('Информация 📗')
    btn4 = types.KeyboardButton('Помощь ❓')
    cns = types.KeyboardButton('Закрыть ❌')
    if its_user[message.from_user.id].admin == 1:
        btn3 = types.KeyboardButton('Админ панель 🎮')
        markup.add(btn1, btn2, btn3, btn4, cns)
    else:
        markup.add(btn1, btn2, btn4, cns)
    msg = bot.send_message(message.chat.id,f"Вопрос отправлен, ожидайте ответа. Ваш вопрос находится под номером {len(question_list)} в очереди", reply_markup=markup)
    bot.register_next_step_handler(msg, check_answ)



def opt(message):
    btn1 = types.KeyboardButton('Информация 📗')
    btn2 = types.KeyboardButton('Помощь ❓')
    btn3 = types.KeyboardButton('Оповещения 🔔')
    cns = types.KeyboardButton('Выход ❌')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn1, btn2, btn3, cns)
    msg = bot.send_message(message.chat.id,"Выберите действие из следующих вариантов:", reply_markup=markup)
    bot.register_next_step_handler(msg, optional)



def mud(call):
    bot.send_message(call.id, "Ввод отменен. Возврат к главному меню.")
    murk(call)