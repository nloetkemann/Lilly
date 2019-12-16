from telepot.loop import MessageLoop
from src.logic.bot_handler import bothandler
from src.grpc.client import Client, temp_dir
from src.logic.message import Message
from src.logic.command import CommandHandler

client = Client()


def on_chat_message(message):
    message = Message(message)
    if message.is_command():
        CommandHandler(message).get_command(message.get_text())
    elif message.is_text():
        client.single_message(message.get_text(), message.chat_id)
    elif message.is_voice():
        file_id = message.get_file_id()
        file_type = message.get_atr('mime_type', 'voice').split('/')[1]
        filename = file_id + '.' + file_type
        message.download_file(temp_dir + filename)
        client.upload_file(filename, message.chat_id)
    elif message.is_document():
        filename = message.get_atr('file_name', 'document')
        message.download_file(temp_dir + filename)
        client.upload_file(filename, message.chat_id)


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
    message = Message(message)
    old_message_id = bothandler.get_message_identifier(message.get_atr('message'))
    try:
        CommandHandler.Callback().callback_action(message.get_atr('data'))
        bothandler.delete_message(old_message_id)
        bothandler.answer_callback(message.chat_id, 'Erledigt')
    except Exception as e:
        bothandler.delete_message(old_message_id)
        bothandler.answer_callback(message.chat_id, 'Es gab leider einen Fehler')


MessageLoop(bothandler.bot, {
    'chat': on_chat_message,
    # 'inline_query': on_inline_query,
    # 'chosen_inline_result': on_inline_query,
    'callback_query': on_callback
}).run_forever()
