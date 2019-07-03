import src.grpc.pb.message_pb2 as message_pb2
from src.logic.handler import MessageHandler
from src.wit.wit import send_text
import src.grpc.pb.message_pb2_grpc as message_pb2_grpc


class MessageServicer(message_pb2_grpc.MessageServicer):

    def SingleRequest(self, request, context):
        wit_response = send_text(request.body)
        try:
            response = MessageHandler(wit_response).handle_message()
        except Exception as e:
            print(e)
            return message_pb2.MessageResponse(body='Hier ging was schief')
        return message_pb2.MessageResponse(body=response.text)

    def StreamRequest(self, request_iterator, context):
        for request in request_iterator:
            # request ist die anfrage vom clienten
            yield message_pb2.MessageResponse(body='erfolgreich')
