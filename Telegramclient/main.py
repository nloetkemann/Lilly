from telepot.loop import MessageLoop
from src.logic.bot_handler import bothandler
from src.grpc.client import Client, temp_dir
from src.logic.message import Message

client = Client()


def on_chat_message(message):
    message = Message(message)
    # if message.is_command():
    #     response_text = client.single_message(message.get_text(), 'command')
    if message.is_text():
        # response_text = client.single_message(message.get_text())
        client.single_message(message.get_text(), message.chat_id)
    elif message.is_voice():
        file_id = message.get_file_id()
        file_type = message.get_atr('mime_type', 'voice').split('/')[1]
        filename = file_id + '.' + file_type
        message.download_file(temp_dir + filename)
        client.upload_file(filename, message.chat_id)
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

MessageLoop(bothandler.bot, {
    'chat': on_chat_message,
    # 'inline_query': on_inline_query,
    # 'chosen_inline_result': on_inline_query,
    'callback_query': on_callback
}).run_forever()
