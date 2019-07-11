from src.grpc.pb.message_pb2 import ClientType
from src.logic.reponse import Response
from src.wit.entities.command_entity import CommandEntity
from src.wit.entities.notification_entity import NotificationEntity
from src.wit.entities.search_entity import SearchEntity
from src.wit.entities.thanks_entity import ThanksEntity
from src.wit.wit_response import WitResponse
from src.wit.entities.intent_entity import IntentEntity
from src.wit.entities.message_entity import MessageEntity
from src.wit.entities.timer_entity import TimerEntity
from src.wit.entities.welcome_entity import WelcomeEntity

entity_list = {'intent': IntentEntity, 'message': MessageEntity,
               'begruessung': WelcomeEntity, 'timer': TimerEntity,
               'erinnerung': NotificationEntity, 'danke': ThanksEntity,
               'suche': SearchEntity}


class MessageHandler:
    def __init__(self, wit_response, client_type):
        assert isinstance(wit_response, WitResponse)
        assert isinstance(client_type, ClientType)
        self.wit_response = wit_response
        self.client_type = client_type

    def get_correct_intent(self, value):
        if value in entity_list:
            return entity_list[value]

    def check_and_send(self, response):
        if response is not None:
            # if response.is_question():
            #     return bothandler.send_question(response)
            # elif response.contains_custom_keyboard():
            #     return bothandler.send_message_with_keyboard(response)
            return response
        return Response('Das hat leider nicht geklappt.')

    def handle_command(self):
        if not self.wit_response.is_success():
            return Response('Ich kenne den Befehl leider nicht.')
        command_entity = CommandEntity(self.wit_response)
        response = command_entity.get_response()
        return response

    def handle_message(self):
        Class = None
        if not self.wit_response.is_success():
            return Response('Ich weiß nicht, was ich machen soll...')

        for key in self.wit_response.get_keywords():
            Class = self.get_correct_intent(key)
            if Class is not None:
                break
        if Class is not None:
            temp_class = Class(self.wit_response, self.client_type)
            return self.check_and_send(temp_class.get_response())
        else:
            # response = MessageHandler(response).get_response()
            return Response('Ich kann mit der Eingabe leider nichts anfangen.')
