import src.grpc.pb.message_pb2 as message_pb2
from src.logic.handler import MessageHandler
from src.logic.message_queue import MessageQueue
from src.wit.wit import send_text
import src.grpc.pb.message_pb2_grpc as message_pb2_grpc


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
                yield message_pb2.MessageResponse(body=response.text, client_type=client_type)
