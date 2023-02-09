from modules.settings import cursor, con, bot, telebot, its_user
from modules.models import User

def us_log(message):
    global its_user
    us_id = cursor.execute("SELECT id FROM users;")
    us_id = us_id.fetchall()
    if (message.from_user.id,) not in us_id:
        add_user_sql = '''
INSERT INTO users
VALUES (?,?,?,?,?,?);
'''
        cursor.execute(add_user_sql, (message.from_user.id, message.from_user.username, None, None, None, 1))
        con.commit()
    mood = message.from_user.id
    adminer = cursor.execute("SELECT admin FROM users WHERE id = ?;", (mood, ))
    adminer = adminer.fetchall()
    its_user[message.from_user.id] = User(message.from_user.id, message.from_user.last_name, message.from_user.username, adminer[0][0])

def strt():
    us_id = cursor.execute("SELECT id FROM users WHERE sends = 1;")
    us_id = us_id.fetchall()
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('/start')
    markup.add(btn1)
    for i in us_id:
        bot.send_message(i[0], "Я снова работаю.", reply_markup = markup)