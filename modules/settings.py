import telebot
import os
import json
import sqlite3
import random
from telebot import types

adder = 0
product_list = []
PATH = os.path.abspath(__file__ + "/.." + "/..")
path_Im_Prod = os.path.join(PATH,"ImageProduct")
path_user = os.path.join(PATH, "JsonForUserDialog")
path_Prod = os.path.join(PATH, "JsonForProduct")
der_prod = os.listdir(path_Im_Prod)
der_prod_js = os.listdir(path_Prod)

try:
    with open("questionlist.json", "r") as read_file:
        question_list = json.load(read_file)
except:
    question_list = []

with open("Admins.json", "r") as read_file:
    admin_list = json.load(read_file)

bot = telebot.TeleBot(token = '5956477413:AAHI-UxeI0p_XhJRJiqgGlcEA3CFTh1VmeU')
con = sqlite3.connect("tutorial.db")