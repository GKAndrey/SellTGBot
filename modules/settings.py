import telebot
import os
import sqlite3
# import random
import sys
from telebot import types

bot = telebot.TeleBot(token = '5956477413:AAHI-UxeI0p_XhJRJiqgGlcEA3CFTh1VmeU')
PATH = os.path.abspath(__file__ + "/.." + "/..")
con = sqlite3.connect(os.path.join(PATH, "database.db"), check_same_thread=False)
cursor = con.cursor()

cursor.execute("SELECT id FROM users WHERE admin = 1;")
admin_cort = cursor.fetchall()
admin_list = []
for i in admin_cort:
    admin_list.append(i[0])

question_list = []
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

adder = 0
its_user ={}
product_list = []
PATH = os.path.abspath(__file__ + "/.." + "/..")
path_Im_Prod = os.path.join(PATH,"Photo")
del a, i, p, q, s, us_name_qw, txt_qw, admin_cort