import src.grpc.pb.message_pb2 as message_pb2
from src.logic.handler import MessageHandler
from src.wit.wit import send_text
import src.grpc.pb.message_pb2_grpc as message_pb2_grpc


class MessageServicer(message_pb2_grpc.MessageServicer):
    response_queue = []

    def SingleRequest(self, request, context):
        wit_response = send_text(request.body)
        try:
            response = MessageHandler(wit_response).handle_message()
        except Exception as e:
            print(e)
            return message_pb2.Success(success=False)
        #     return message_pb2.MessageResponse(body='Hier ging was schief')
        self.response_queue.append((response, request.client_type))
        print(self.response_queue)
        return message_pb2.Success(success=True)
        # return message_pb2.MessageResponse(body=response.text)

    def StreamRequest(self, request_iterator, context):
        while True:
            while len(self.response_queue) > 0:
                response = (self.response_queue[0])[0]
                client_type = (self.response_queue[0])[1]
                self.response_queue.pop(0)
                yield message_pb2.MessageResponse(body=response.text, client_type=client_type)
        # message_pb2.MessageResponse(body='erfolgreich')
