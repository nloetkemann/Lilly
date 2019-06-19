from src.logic.bot_handler import bothandler
from src.logic.callback import Callback
from src.reponse import Response
from src.wit.entities.command_entity import CommandEntity
from src.wit.entities.notification_entity import NotificationEntity
from src.wit.entities.thanks_entity import ThanksEntity
from src.wit.wit_response import WitResponse
from src.message import Message
from src.wit.wit import send_audio_file
from src.wit.entities.intent_entity import IntentEntity
from src.wit.entities.message_entity import MessageEntity
from src.wit.entities.timer_entity import TimerEntity
from src.wit.entities.welcome_entity import WelcomeEntity

entity_list = {'intent': IntentEntity, 'message': MessageEntity,
               'begruessung': WelcomeEntity, 'timer': TimerEntity,
               'erinnerung': NotificationEntity, 'danke': ThanksEntity}


class MessageHandler:
    def __init__(self, message, wit_response=None):
        assert isinstance(message, Message)
        if wit_response is not None:
            assert isinstance(wit_response, WitResponse)
            self.wit_response = wit_response
        self.message = message

    def get_correct_intent(self, value):
        if value in entity_list:
            return entity_list[value]

    def check_and_send(self, response):
        if response is not None:
            if response.is_question():
                return bothandler.send_question(response)
            elif response.contains_custom_keyboard():
                return bothandler.send_message_with_keyboard(response)
            return bothandler.send_message(response)
        return bothandler.send_message(Response('Das hat leider nicht geklappt.', self.message))

    def handle_command(self):
        if not self.wit_response.is_success():
            return bothandler.send_message(Response('Ich kenne den Befehl leider nicht.', self.message))
        command_entity = CommandEntity(self.wit_response, self.message)
        response = command_entity.get_response()
        return bothandler.send_question(response)

    def handle_callback(self):
        old_message_id = bothandler.get_message_identifier(self.message.get_atr('message'))
        data = self.message.get_atr('data')
        text = Callback().callback_action(data)
        bothandler.answer_callback(self.message.chat_id, 'Erledigt')
        if text != '' and text is not None:
            bothandler.edit_message(old_message_id, text)
        else:
            bothandler.delete_message(old_message_id)

    def handle_message(self):
        Class = None
        if self.message.is_voice_file and CommandEntity.get_voice_mode(CommandEntity) == 't' and self.wit_response.text != '':
            return bothandler.send_message(Response(self.wit_response.text, self.message))

        if not self.wit_response.is_success():
            return bothandler.send_message(Response('Ich weiß nicht, was ich machen soll...', self.message))

        for key in self.wit_response.get_keywords():
            Class = self.get_correct_intent(key)
            if Class is not None:
                break

        if Class is not None:
            temp_class = Class(self.wit_response, self.message)
            return self.check_and_send(temp_class.get_response())
        else:
            # response = MessageHandler(response).get_response()
            return bothandler.send_message(Response('Ich kann mit der Eingabe leider nichts anfangen.', self.message))


class FileHandler:
    def __init__(self):
        self.temp_dir = 'temp/'

    def download_file(self):
        pass

    def handle_file(self, message, type):
        filename = self.temp_dir + message.get_file_id() + '.' + type.split('/')[1]
        message.download_file(filename)

        # send to wit and get response
        return send_audio_file(filename)
