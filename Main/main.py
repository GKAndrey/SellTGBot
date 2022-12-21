import telebot, os, json, Token
from telebot import types
# from gtts import gTTS

PATH = os.path.abspath(__file__ + "/.." + "/..")
path_Im_Prod = PATH + "\ImageProduct" #То, куда будут сохранятся картинки
path_Prod = PATH + "\JsonForProduct" #Место сохранения json файлов с описанием товаров
path_user = PATH + "\JsonForUserDialog" #Сюда сохраняем инфу о пользователе, его заказы и "корзину".

#Надо не забыть создать разгрузку файлов из папок.

class Product():
    def __init__(self, name):
        self.name = name
        #Прописать основные параметры продукта
    def prod_save(self):
        list_p = [] #Записываем параметры, которые будут нужны продукту. Нельзя сохранить обьект, к сожалению.
        with open(path_Prod + self.name + ".json", "w") as write_file:
            json.dump(list_p, write_file, indent = 4)

class User():
    def __init__(self):
        pass #Прописываем параметры и возможности пользователя.
    def user_save(self):
        list_p = [] #Записываем параметры, которые надо сохранить человеку. Например то, где находился диалог и состояние корзины. Нельзя сохранить обьект, к сожалению.
        with open(path_user + self.name + ".json", "w") as write_file:
            json.dump(list_p, write_file, indent = 4)

bot = telebot.TeleBot(token = Token.token) #Токен скрыт для сохранения в гитхаб.

@bot.message_handler(commands=["start"]) #Основная панель юзера, где прописываются все взаимодействия.
def start(message):
    pass

@bot.message_handler(commands=["admin"]) #Панель админов с добавлениями, удалениями или изменениями продуктов.
def admins(message):
    if message.user_id in Token.admin_list:
        pass

@bot.message_handler(commands=["question"]) #Вопросы к администрации бота, с повода ошибок, багов, вопросов и тд.
def question(message):
    pass