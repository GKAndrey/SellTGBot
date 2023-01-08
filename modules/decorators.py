from modules.settings import *
from modules.models import *
from modules.products import *
from modules.admins import *
from modules.func import *

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Перейти к меню")
    markup.add(btn1)
    msg = bot.send_message(message.from_user.id, "👋 Привет! Я магазин ShopBot!", reply_markup=markup)
    bot.register_next_step_handler(msg, start_bot)

@bot.message_handler(commands=["question"])
def q(message):
    global question_list
    try:
        question_text = message.text.split(' ',maxsplit = 1)[1]
        bot.send_message(message.chat.id,f"Вопрос отправлен, ожидайте ответа. Ваш вопрос находится под номером {len(question_list)+1} в очереди")
        question_list.append([message.chat.id, question_text, message.from_user.username])
        with open(f"{PATH}/questionlist.json", "w") as write_file:
            json.dump(question_list, write_file,sort_keys=False,indent=4,ensure_ascii=False,)
        for i in admin_list:
            bot.send_message(i,f"У вас новый вопрос. Всего {len(question_list)} вопросов.")
    except:
        bot.send_message(message.chat.id,"Введите через пробел свой вопрос после команды. (/question текст)")

@bot.message_handler(commands=["show_questions"])
def show_question(message):
    if question_list == []:
        bot.send_message(message.chat.id, f'Вопросов нет.')
    elif message.chat.id in admin_list:
        j = 1
        for i in question_list:
            bot.send_message(message.chat.id, f'{j}) {i[1]} (от @{i[2]})')
            j += 1

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
    except:
        bot.reply_to(message, "Нельзя ответить на несуществующий вопрос.")

@bot.message_handler(commands=["add"])
def add(message):
    if message.from_user.id in admin_list:
        global adder
        bot.send_message(message.chat.id, "Пришлите мне **Название** для обьявления.", reply_markup=types.ReplyKeyboardRemove())
        adder = 1

@bot.message_handler(content_types=["text"])
def text(message):
    if message.from_user.id in admin_list:
        global adder
        if adder == 1:
            product_list.append(Product(message.text))
            adder = 2
            bot.send_message(message.chat.id, "Пришлите мне **Фото** для обьявления.")
        elif adder == 3:
            product_list[-1].add_opis(message.text)
            bot.send_message(message.chat.id, 'Пришлите мне **Теги** для обьявления. Пример: "#Спорт#Мода#Електроника".')
            adder = 4
        elif adder == 5:
            bot.send_message(message.chat.id, 'Все готово, обьявление добавленно в каталог.')
            adder = 0
            product_list[-1].add_money(message.text)
            save_prod()
            up_list_prod()
        elif adder == 4:
            try:
                tegs = message.text.split("#")
                bot.send_message(message.chat.id, 'Введите цену на этот продукт.')
                product_list[-1].tegs_prod(tegs)
                adder = 5
            except:
                bot.send_message(message.chat.id, 'Будьте внимательнее и следуйте инструкции (#Sport#Спорт#Електроника#Надо).')

@bot.message_handler(content_types=["photo"])
def poto_use(message):
    if message.from_user.id in admin_list:
        global adder
        if adder == 2:
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
