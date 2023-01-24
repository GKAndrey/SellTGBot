# from modules.models import *
# from modules.products import *
from modules.admins import *

def start_bot(message):
    if message.text == '👋 Перейти к меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Товары 🛒')
            btn2 = types.KeyboardButton('Информация 📗')
            btn3 = types.KeyboardButton('Помощь ❓')
            cns = types.KeyboardButton('Закрыть ❌')
            if its_user[message.from_user.id].admin == 1:
                btn4 = types.KeyboardButton('Админ панель 🎮')
                markup.add(btn1, btn2, btn3, btn4, cns)
            else:
                markup.add(btn1, btn2, btn3, cns)
            msg = bot.send_message(message.from_user.id, 'Выберете что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(msg, check_answ)

def check_answ(message):
    if message.text == 'Товары 🛒': #Над логикой работает Ваня
        bot.send_message(message.chat.id,"Товары 🛒") #дальше этого сообщения оно не заходит хз почему
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_search_ontag = types.KeyboardButton('Искать по тегу 🏷️')
        btn_search_onname = types.KeyboardButton('Искать по названию 🔤')
        # a = markup.add(btn_search_onname,btn_search_ontag)
        if its_user[message.from_user.id].admin == 1:
            btn4 = types.KeyboardButton('Админ панель 🎮')
            markup.add(btn_search_onname,btn_search_ontag,btn4)
        else:
            markup.add(btn_search_ontag,btn_search_onname)
        msg = bot.send_message(message.from_user.id, 'Выберете что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(msg)
    elif message.text == 'Информация 📗':
        bot.send_message(message.chat.id,"Инфо о боте:")
        bot.send_message(message.chat.id,"Бот создан: **Ещё в разработке**")
        bot.send_message(message.chat.id,"Над ботом работали:") #тут можно отметить девов (разрабов)
    elif message.text == 'Админ панель 🎮':
        if its_user[message.from_user.id].admin == 1:
            admin_menu(message)
        else:
            bot.send_message(message.chat.id, f'Вы (@{message.from_user.username}) не являетесь админом бота. В случае вопросов, предложений или вакансий обращайтесь в тех. поддержку (Помощь ❓).')
    elif message.text == 'Помощь ❓':
        msg = bot.send_message(message.from_user.id, 'Введите свой вопрос:', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, quests)
    elif message.text == 'Закрыть ❌':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('/start')
        markup.add(btn1)
        bot.send_message(message.chat.id, "Буду ждать новой встречи.", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Просим вас заранее, не стоит ломать логику бота, врятли у вас это получится, к тому же, хуже вы сделаете только себе, если администрация заметит вас как виновника и добавит в черный список. Если это не намерянно, то будьте окуратнее и пользуйтесь кнопками, они не только для красоты были созданы.')
        msg = bot.send_message(message.from_user.id, 'Выберете что вам нужно:')
        bot.register_next_step_handler(msg, check_answ)

def quests(message):
    global question_list
    question_list.append((message.chat.id, message.text, message.from_user.username))
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

# def get_quests():
#     '''
#     SELECT * FROM orders;
#     '''
#     cursor.execute(get_quests)
#     result = cursor.fetchall()


#     for i in admin_list:
#         bot.send_message(i,f"У вас новый вопрос. Всего {len(question_list)} вопросов.")#напишешь, потом расскажешь что зачем
