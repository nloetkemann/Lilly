import os
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from urllib3.exceptions import ProtocolError

from src.logic.reponse import Response


class BotHandler:
    def __init__(self):
        self.bot = telepot.Bot(os.environ['BOT_TOKEN'])
        self.retry = 0

    def send_message(self, response, keyboard=None):
        assert isinstance(response, Response)
        try:
            self.retry = 0
            return self.bot.sendMessage(response.origin_message.chat_id, response.text, reply_markup=keyboard)
        except ProtocolError as e:
            if self.retry == 0:
                self.send_message(response, keyboard)
                self.retry = 1
            else:
                self.retry = 0
                raise e

    def send_question(self, response):
        return self.send_message(response, self._get_inline__keyboard(response.get_args()))

    def send_message_with_keyboard(self, response):
        return self.send_message(response, self._get_custom_keyboard(response.get_args()))

    #  values should be dict
    def _get_inline__keyboard(self, values):
        assert isinstance(values, dict)
        all_keyboard = []
        for key in values.keys():
            print(values[key])
            all_keyboard.append(InlineKeyboardButton(text=key, callback_data=values[key]))
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            all_keyboard,
        ])
        return keyboard

    # values should be array
    def _get_custom_keyboard(self, values):
        assert isinstance(values, list)
        keyboard = ReplyKeyboardMarkup(keyboard=values, one_time_keyboard=True, resize_keyboard=True)
        return keyboard

    def download_file(self, file_id, path):
        self.bot.download_file(file_id, path)

    def answer_callback(self, query_id, text):
        return self.bot.answerCallbackQuery(query_id, text)

    def edit_message(self, message_id, text):
        return self.bot.editMessageText(message_id, text, reply_markup=None)

    def get_message_identifier(self, message):
        return telepot.message_identifier(message)

    def delete_message(self, message_id):
        self.bot.deleteMessage(message_id)

    def restart(self):
        self.bot = telepot.Bot(os.environ['BOT_TOKEN'])


bothandler = BotHandler()
