from telepot.loop import MessageLoop
from src.logic.bot_handler import bothandler
from src.logic.client import Client
from src.logic.message import Message
from src.logic.reponse import Response

client = Client()


def on_chat_message(message):
    message = Message(message)
    if message.is_command():
        response_text = client.single_message(message.get_text(), 'command')
    elif message.is_text():
        response_text = client.single_message(message.get_text())
    elif message.is_voice():
        response_text = 'Ist noch nicht fertig'
    elif message.is_document():
        response_text = 'Ist auch noch nicht fertig'
    else:
        response_text = 'Kein Type'
    bothandler.send_message(Response(response_text, message))


#  todo muss noch gemacht werden
# def on_inline_query(message):
#     print(message)
#
#
# def on_choosen_inline_query(message):
#     result_id, from_id, query_string = bothandler.bot.glance(message, flavor='chosen_inline_result')
#     print(result_id, ':', 'Chosen Inline Result:', result_id, from_id, query_string)
#
#
def on_callback(message):
    pass
    # message = Message(message)
    # handler = MessageHandler(message)
    # handler.handle_callback()


print('Bot is running')

MessageLoop(bothandler.bot, {
    'chat': on_chat_message,
    # 'inline_query': on_inline_query,
    # 'chosen_inline_result': on_inline_query,
    'callback_query': on_callback
}).run_forever()