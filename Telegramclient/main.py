from telepot.loop import MessageLoop
from src.logic.bot_handler import bothandler
from src.logic.client import Client
from src.logic.message import Message
from src.logic.thread import FunctionThread

client = Client()

temp_dir = '../temp/'

message_list = []


def wait_for_response(stop_thread):
    responses = client.stream_message()
    for response in responses:
        client_type = response[1]
        if client_type.telegramm is not None and client_type.telegramm != '':
            chat_id = client_type.telegramm.chat_id
            bothandler.bot.sendMessage(chat_id, response[0])


def on_chat_message(message):
    message = Message(message)
    # if message.is_command():
    #     response_text = client.single_message(message.get_text(), 'command')
    if message.is_text():
        # response_text = client.single_message(message.get_text())
        client.single_message(message.get_text(), message.chat_id)
    # elif message.is_voice():
    #     file_id = message.get_file_id()
    #     file_type = message.get_atr('mime_type', 'voice').split('/')[1]
    #     filename = temp_dir + file_id + '.' + file_type
    #     message.download_file(filename)
    #     response_text = client.upload_file(filename)
    # elif message.is_document():
    #     response_text = 'Ist auch noch nicht fertig'
    # else:
    #     response_text = 'Kein Type'
    # bothandler.send_message(Response(response_text, message))


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

thread = FunctionThread(wait_for_response)
thread.start()

MessageLoop(bothandler.bot, {
    'chat': on_chat_message,
    # 'inline_query': on_inline_query,
    # 'chosen_inline_result': on_inline_query,
    'callback_query': on_callback
}).run_forever()
