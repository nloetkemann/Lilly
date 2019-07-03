import grpc
import src.grpc.pb.message_pb2_grpc as message_pb2_grpc
from src.grpc.pb.message_pb2 import MessageRequest


class Client:

    def __init__(self):
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = message_pb2_grpc.MessageStub(channel)

    def single_message(self, text, type='text'):
        request = MessageRequest(body=text, type=type)
        feature = self.stub.SingleRequest(request)
        return feature.body

    def stream_message(self, text_array):
        def gen_request(messages, origin):
            for text in messages:
                request = MessageRequest(body=text, origin=origin)
                yield request

        it = self.stub.StreamRequest(gen_request(text_array, 'was geht ab'))
        array = []
        for r in it:
            array.append(r.body)
        return array
