from modules.settings import *

class Product():
    def __init__(self, id:int, name:str, opis:str, path_photo:str, moneys:str, tegs:list):
        self.name = name
        self.id = id
        self.opis = opis
        self.path_photo = path_photo
        self.moneys = moneys
        tegs = tegs.split(" ")
        self.tegs = []
        for i in tegs:
            self.tegs.append(i)

class User:
    def __init__(self, id:int, last_name:str, username, adm = 0, basket = None):
        self.id = id
        self.last_name = last_name
        self.username = username
        self.admin = adm
        self.basket = basket