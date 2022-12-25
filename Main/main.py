import telebot,os, json, Token
from telebot import types
# from gtts import gTTS

adder = 0
PATH = os.path.abspath(__file__ + "/.." + "/..")
path_Im_Prod = PATH + "\ImageProduct"
path_user = PATH + "\JsonForUserDialog"



class Product():
    def __init__(self, name):
        self.name = name
    def add_photo(self):
        self.Pash_photo = f'{path_Im_Prod}\{Token.product_list[-1].name}.png'
    def add_opis(self,opis):
        self.opis = opis
    def tegs_prod(self, list):
        self.tegs_list = []
        for i in list:
            self.tegs_list.append(i)
        Token.save_prod()

class User():
    def __init__(self):
        pass
    def user_save(self):
        list_p = []
        with open(path_user + self.name + ".json", "w") as write_file:
            json.dump(list_p, write_file, indent = 4)

bot = telebot.TeleBot(token = Token.token)

@bot.message_handler(commands=["start"])
def start(message):
    pass



@bot.message_handler(commands=["admin"])
def admins(message):
    if message.from_user.id in Token.admin_list:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        add_prod = types.KeyboardButton("/add добавить обьявление")
        remove_prod = types.KeyboardButton("/remove удалить обьявление")
        cansel = types.KeyboardButton("/cansel выход из меню админов")
        markup.add(add_prod, remove_prod, cansel)
        bot.send_message(message.chat.id, "Какая опция вам нужна?", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'Вы (@{message.from_user.username}) не являетесь админом бота. В случае вопросов, предложений или вакансий обращайтесь в тех. поддержку (она же и "Обратная связь" /question).')

@bot.message_handler(commands=['cansel'])
def cans(message: types.Message):
    bot.send_message(message.chat.id, "Жду следующей команды.", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(commands=["add"])
def add(message):
    if message.from_user.id in Token.admin_list:
        global adder
        bot.send_message(message.chat.id, "Пришлите мне **Название** для обьявления.", reply_markup=types.ReplyKeyboardRemove())
        adder = 1

@bot.message_handler(content_types=["text"])
def text(message):
    if message.from_user.id in Token.admin_list:
        global adder
        if adder == 1:
            Token.product_list.append(Product(message.text))
            adder = 2
            bot.send_message(message.chat.id, "Пришлите мне **Фото** для обьявления.")
        elif adder == 3:
            Token.product_list[-1].add_opis(message.text)
            bot.send_message(message.chat.id, 'Пришлите мне **Теги** для обьявления. Пример: "#Спорт #Мода #Електроника".')
            adder = 4
        elif adder == 4:
            tegs = message.text.split()
            bot.send_message(message.chat.id, 'Все готово, обьявление добавленно в каталог.')
            Token.product_list[-1].tegs_prod(tegs)

@bot.message_handler(content_types=["photo"])
def poto_use(message):
    if message.from_user.id in Token.admin_list:
        global adder
        if adder == 2:
            try:
                file = bot.get_file(message.photo[-1].file_id)
                file = bot.download_file(file.file_path)
                with open(f'{path_Im_Prod}\{Token.product_list[-1].name}.png', 'wb') as f:
                    f.write(file)
                Token.product_list[-1].add_photo()
                bot.send_message(message.chat.id, 'Фото получено. Введите **Описание** обьявления/продукта.')
                adder = 3
            except:
                pass



@bot.message_handler(commands=["question"])
def question(message):
    pass

bot.infinity_polling()