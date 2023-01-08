from modules.settings import *

class Product():
    def __init__(self, name):
        self.name = name
    def add_photo(self, paths = None):
        if paths:
            self.Pash_photo = paths
        else:
            self.Pash_photo = f'{path_Im_Prod}/{product_list[-1].name}.png'
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
        self.is_admin = False
    def user_save(self):
        list_p = []
        with open(path_user + self.name + ".json", "w") as write_file:
            json.dump(list_p, write_file, indent = 4)
    def start(self):
        if self.is_admin:
            print('menu with button wich redirect on admin panel')
        else:
            print('menu without button wich redirect on admin panel')

# class User:
#     def __init__(self, first_name,last_name,username,orders):
#         self.id = id 
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username
#         self.orders = orders # many objects of Order class
# class ProductType:
#     def __init__(self):
#         self.id = id
#         self.name = name
#         self.description = description
# class Product:
#     def __init__(self):
#         self.id = id 
#         self.name = name
#         self.description = description
#         self.price = price
#         self.product_type = product_type # one object of ProductType class 
# class Order:
#     def __init__(self):
#         self.id = id
#         self.products = products # many objects of Product class