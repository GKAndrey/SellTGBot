from modules.models import *

def add_product_sql(id): #Сохранение нового товара
    add_product_sql = '''
INSERT INTO products
VALUES (?,?,?,?,?,?);
'''
    cursor.execute(add_product_sql, (product_list[id].id, product_list[id].name, product_list[id].tags, product_list[id].opis, product_list[id].path_photo, product_list[id].maney))
    con.commit()

def get_product():
    get_product = '''
    SELECT id FROM products;'''
    cursor.execute(get_product)
    result = cursor.fetchall()
    for i in result:
        cursor.execute("SELECT name FROM products WHERE id = ?;", i)
        name = cursor.fetchall()
        cursor.execute("SELECT tags FROM products WHERE id = ?;", i)
        tags = cursor.fetchall()
        cursor.execute("SELECT opis FROM products WHERE id = ?;", i)
        opis = cursor.fetchall()
        cursor.execute("SELECT path_photo FROM products WHERE id = ?;", i)
        path_photo = cursor.fetchall()
        cursor.execute("SELECT maney FROM products WHERE id = ?;", i)
        maney = cursor.fetchall()
        tags = tags[0].split("/")
        product_list.append(Product(result[0], name[0],tags,opis[0],path_photo[0],maney[0]))
