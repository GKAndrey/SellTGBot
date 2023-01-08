from modules.settings import *
from modules.models import *
from modules.products import *

def start_bot(message):
    if message.text == '👋 Перейти к меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Товары 🛒')
            btn2 = types.KeyboardButton('Информация 📗')
            btn4 = types.KeyboardButton('Помощь ❓')
            cns = types.KeyboardButton('Закрыть ❌')
            if message.from_user.id in admin_list:
                btn3 = types.KeyboardButton('Админ панель 🎮')
                markup.add(btn1, btn2, btn3, btn4, cns)
            else:
                markup.add(btn1, btn2, btn4, cns)
            msg = bot.send_message(message.from_user.id, 'Выберете что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(msg, check_answ)

def check_answ(message):
    if message.text == 'Товары 🛒': #Над логикой работает Ваня
        pass
    elif message.text == 'Информация 📗':
        pass
    elif message.text == 'Админ панель 🎮':
        if message.from_user.id in admin_list:
            pass
    elif message.text == 'Помощь ❓':
        msg = bot.send_message(message.from_user.id, 'Введите свой вопрос)', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, quests)
    elif message.text == 'Закрыть ❌':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('/start')
        markup.add(btn1)
        bot.send_message(message.chat.id, "Буду ждать новой встречи.", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Просим вас заранее, не стоит ломать логику бота, врятли у вас это получится, к тому же, хуже вы сделаете только себе, если администрация заметит вас как виновника и добавит в черный список. Если это не намерянно, то будьте окуратнее.')
        msg = bot.send_message(message.from_user.id, 'Выберете что вам нужно:')
        bot.register_next_step_handler(msg, check_answ)

def quests(message):
    global question_list
    bot.send_message(message.chat.id,f"Вопрос отправлен, ожидайте ответа. Ваш вопрос находится под номером {len(question_list)+1} в очереди")
    question_list.append([message.chat.id, message.text, message.from_user.username])
    with open(f"{PATH}/questionlist.json", "w") as write_file:
        json.dump(question_list, write_file,sort_keys=False,indent=4,ensure_ascii=False,)
    for i in admin_list:
        bot.send_message(i,f"У вас новый вопрос. Всего {len(question_list)} вопросов.")