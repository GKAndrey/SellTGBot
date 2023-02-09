from modules.func import start, murk, opt
from modules.settings import bot

# strt() #Отсылает пользователям статус готовности, выключайте на время тестов.

@bot.message_handler(commands=["start"])
def strt(message):
    start(message)



@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Оповещения выключены 🔕✅")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Оповещения включены 🔕❌")
    elif call.data == 'close_quest':
        bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Отменено.')
        murk(call)
    elif call.data == 'close_menu':
        opt(call.message)