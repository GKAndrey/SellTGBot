# from modules.models import *
# from modules.products import *
# from modules.admins import *
from modules.func import *
from modules.user_log import *

# strt() #Отсылает пользователям статус готовности, выключайте на время тестов.

@bot.message_handler(commands=["start"])
def start(message):
    global its_user
    us_log(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Перейти к меню")
    markup.add(btn1)
    msg = bot.send_message(message.from_user.id, "👋 Привет! Я магазин ShopBot!", reply_markup=markup)
    bot.register_next_step_handler(msg, start_bot)

# @bot.message_handler(commands=["show_questions"])
# def show_question(message):
#     if question_list == []:
#         bot.send_message(message.chat.id, f'Вопросов нет.')
#     elif message.chat.id in admin_list:
#         j = 1
#         for i in question_list:
#             bot.send_message(message.chat.id, f'{j}) {i[1]} (от @{i[2]})')
#             j += 1

# @bot.message_handler(content_types=["photo"])
# def poto_use(message):
#     if message.from_user.id in admin_list:
#         global adder
#         if adder == 2:
#             try:
#                 file = bot.get_file(message.photo[-1].file_id)
#                 file = bot.download_file(file.file_path)
#                 with open(f'{path_Im_Prod}/{product_list[-1].name}.png', 'wb') as f:
#                     f.write(file)
#                 product_list[-1].add_photo()
#                 bot.send_message(message.chat.id, 'Фото получено. Введите **Описание** обьявления/продукта.')
#                 adder = 3
#             except:
#                 pass
