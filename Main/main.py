import telebot,os, json
from telebot import types
# from gtts import gTTS

adder = 0
PATH = os.path.abspath(__file__ + "/.." + "/..")
path_Im_Prod = PATH + "\ImageProduct"
path_user = PATH + "\JsonForUserDialog"
path_Prod = PATH + "\JsonForProduct"
der_prod = os.listdir(path_Im_Prod)
der_prod_js = os.listdir(path_Prod)



with open("Admins.json", "r") as read_file:
    admin_list = json.load(read_file)

def remove_prod():
    os.remove()

def save_prod():
    for i in range(len(product_list)):
        if f'{product_list[i].name}.json' not in der_prod_js:
            prod_dir = [product_list[i].name, product_list[i].Pash_photo, product_list[i].opis, product_list[i].tegs_list, product_list[i].money]
            save_list = prod_dir[3].pop(0)
            with open(f"{path_Prod}\{product_list[i].name}.json", "w") as write_file:
                json.dump(save_list, write_file, indent = 4,ensure_ascii=False,)

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
        print("ERROR. NOT FOUND ID.")

def up_list_prod():
    global product_list
    product_list = []
    for i in der_prod_js:
        with open(f"{path_Prod}\{i}", "r", encoding='utf-8') as read_file:
            prod_inf_list = json.load(read_file)
        product_list.append(Product(prod_inf_list[0]))
        product_list[-1].add_photo(prod_inf_list[1])
        product_list[-1].add_opis(prod_inf_list[2])
        product_list[-1].tegs_prod(prod_inf_list[3])
        print(prod_inf_list[3])



class Product():
    def __init__(self, name):
        self.name = name
    def add_photo(self, paths = None):
        if paths:
            self.Pash_photo = paths
        else:
            self.Pash_photo = f'{path_Im_Prod}\{product_list[-1].name}.png'
    def add_opis(self,opis):
        self.opis = opis
    def tegs_prod(self, list):
        self.tegs_list = []
        for i in list:
            self.tegs_list.append(i)
    def add_money(self, mon):
        self.money = mon

class User():
    def __init__(self):
        pass
    def user_save(self):
        list_p = []
        with open(path_user + self.name + ".json", "w") as write_file:
            json.dump(list_p, write_file, indent = 4)

bot = telebot.TeleBot(token = '5950507768:AAG5OWXQtfIV2vVyskqOj0QBzIXS4zfEgeg')
up_list_prod()

@bot.message_handler(commands=["start"])
def start(message):
    pass



@bot.message_handler(commands=["admin"])
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

@bot.message_handler(commands=["admins"])
def admins(message):
    print(message.from_user.id)
    if 1439133134 == message.from_user.id:
        try:
            messs = message.text.split()[1]
            
        except:
            bot.send_message(message.chat.id, "После команды должен быть ID нового администратора.")

@bot.message_handler(commands=['cansel'])
def cans(message: types.Message):
    bot.send_message(message.chat.id, "Жду следующей команды.", reply_markup=types.ReplyKeyboardRemove())

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
                with open(f'{path_Im_Prod}\{product_list[-1].name}.png', 'wb') as f:
                    f.write(file)
                product_list[-1].add_photo()
                bot.send_message(message.chat.id, 'Фото получено. Введите **Описание** обьявления/продукта.')
                adder = 3
            except:
                pass



@bot.message_handler(commands=["question"])
def question(message):
    pass

bot.infinity_polling()