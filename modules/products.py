from modules.settings import *
from modules.models import Product

def up_list_prod():
    global product_list
    product_list = []
    for i in der_prod_js:
        with open(f"{path_Prod}/{i}", "r") as read_file:
            prod_inf_list = json.load(read_file)
        product_list.append(Product(prod_inf_list[0]))
        product_list[-1].add_photo(prod_inf_list[1])
        product_list[-1].add_opis(prod_inf_list[2])
        product_list[-1].tegs_prod(prod_inf_list[3])

def save_prod():
    for i in range(len(product_list)):
        if f'{product_list[i].name}.json' not in der_prod_js:
            prod_dir = [product_list[i].name, product_list[i].Pash_photo, product_list[i].opis, product_list[i].tegs_list, product_list[i].money]
            save_list = prod_dir[3].pop(0)
            with open(f"{path_Prod}/{product_list[i].name}.json", "w") as write_file:
                json.dump(save_list, write_file, indent = 4,ensure_ascii=False,)

def remove_prod():
    os.remove()

up_list_prod()