import telebot
import os
import sqlite3
# import random
# import re
import sys

bot = telebot.TeleBot(token = '5950507768:AAG5OWXQtfIV2vVyskqOj0QBzIXS4zfEgeg')
PATH = os.path.abspath(__file__ + "/.." + "/..")
con = sqlite3.connect(os.path.join(PATH, "database.db"), check_same_thread=False)
cursor = con.cursor()

admin_list = []
question_list = []
last_photo_indx = int

def load_inf():
    cursor.execute("SELECT id FROM users WHERE admin = 1;")
    admin_cort = cursor.fetchall()
    global admin_list
    for i in admin_cort:
        admin_list.append(i[0])

    global question_list
    s = []
    a = cursor.execute("SELECT id FROM orders;")
    a = a.fetchall()
    for i in a:
            if i not in s:
                s.append(i)
    for p in s:
        cursor.execute("SELECT text FROM orders WHERE id = ?;", p)
        txt_qw = cursor.fetchall()
        q = 0
        for i in txt_qw:
            cursor.execute("SELECT user_name FROM orders WHERE id = ?;", p)
            us_name_qw = cursor.fetchall()
            question_list.append((i[0],us_name_qw[q][0],p[0]))
            q += 1

    global last_photo_indx
    a = cursor.execute("SELECT id FROM products;")
    try:
        last_photo_indx = a.fetchall()[-1][0]
    except:
        last_photo_indx = 1



load_inf()
adder = 0
its_user ={}
product_list = []
PATH = os.path.abspath(__file__ + "/.." + "/..")
path_Im_Prod = os.path.join(PATH,"Photo")



#Доп материал
#← ↑ → ↓ △ ▽ ◁ ▷