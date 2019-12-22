import src.grpc.pb.message_pb2 as message_pb2
from src.logic.handler import MessageHandler
from src.logic.message_queue import MessageQueue
from src.logic.reponse import Response
from src.wit.entities.search_entity import SearchEntity
from src.wit.wit import send_text
import src.grpc.pb.message_pb2_grpc as message_pb2_grpc
from src.wit.wit_response import WitResponse


class MessageServicer(message_pb2_grpc.MessageServicer):

    def SingleRequest(self, request, context):
        wit_response = send_text(request.body)
        try:
            response = MessageHandler(wit_response, request.client_type).handle_message()
        except Exception as e:
            print(e)
            return message_pb2.Success(success=False)
        MessageQueue.add(response, request.client_type)
        return message_pb2.Success(success=True)

    def StreamRequest(self, request_iterator, context):
        while True:
            while MessageQueue.get_length() > 0:
                response, client_type = MessageQueue.get_first()
                if isinstance(response, Response):
                    if response.is_question() and isinstance(response.args[0], list):
                        keyboardlist = response.args[0]
                        callbackmethod = response.args[1]
                        keyboard = message_pb2.MessageResponse.Keyboard(keyboard=keyboardlist,
                                                                        callbackmethod=callbackmethod)
                        yield message_pb2.MessageResponse(body=response.text, client_type=client_type,
                                                          keyboard=keyboard)
                    else:
                        keyboard = message_pb2.MessageResponse.Keyboard(keyboard=[], callbackmethod="")
                        yield message_pb2.MessageResponse(body=response.text, client_type=client_type,
                                                          keyboard=keyboard)
                else:
                    response = Response("Es gabe leider ein kleines Problem")
                    keyboard = message_pb2.MessageResponse.Keyboard(keyboard=[], callbackmethod="")
                    yield message_pb2.MessageResponse(body=response.text, client_type=client_type, keyboard=keyboard)

    def DirectRequest(self, request, context):
        if request.entity_name == 'wiki':
            wit_response = WitResponse(request.body, {'query': [request.body], 'suche': ['suche']})
            try:
                response = SearchEntity.Wikipedia().search(wit_response)
            except Exception:
                return message_pb2.Success(success=False)
            MessageQueue.add(response, request.client_type)
            return message_pb2.Success(success=True)

        elif request.entity_name == 'wolfram':
            wit_response = WitResponse(request.body, {'query': [request.body], 'suche': ['suche']})
            try:
                response = SearchEntity.Wolfram().search(wit_response)
            except Exception:
                return message_pb2.Success(success=False)
            MessageQueue.add(response, request.client_type)
            return message_pb2.Success(success=True)

        else:
            response = Response('Ich weiß nicht an wen ich die Nachricht schicken soll.')
            MessageQueue.add(response, request.client_type)
