import json, os

token = "5950507768:AAG5OWXQtfIV2vVyskqOj0QBzIXS4zfEgeg"

PATH = os.path.abspath(__file__ + "/.." + "/..")
path_Im_Prod = PATH + "\ImageProduct"
path_Prod = PATH + "\JsonForProduct"
product_list = []

def save_prod():
    der_prod = os.listdir(path_Im_Prod)
    for i in range(len(product_list)):
        if product_list[i] not in der_prod:
            prod_dir = [product_list[i].name, product_list[i].Pash_photo, product_list[i].opis, product_list[i].tegs_list]
            with open(f"{path_Prod}\{product_list[i].name}.json", "w") as write_file:
                json.dump(prod_dir, write_file, indent = 4)

with open("Admins.json", "r") as read_file:
    admin_list = json.load(read_file)

def adm_pls(ID):
    admin_list.append(ID)
    with open("Admins.json", "w") as write_file:
        json.dump(admin_list, write_file)

def adm_mns(ID):
    try:
        admin_list.remove(ID)
        with open("Admins.json", "w") as write_file:
            json.dump(admin_list, write_file)
    except:
        print("ERROR. NOT FOUND ID.")