import os

import grpc
import src.grpc.pb.message_pb2_grpc as message_pb2_grpc
import src.grpc.pb.file_pb2_grpc as file_pb2_grpc
from src.grpc.pb.file_pb2 import FileRequest
from src.grpc.pb.message_pb2 import MessageRequest, Empty, ClientType


class Client:
    CHUNK_SIZE = 1024 * 512

    def __init__(self):
        channel = grpc.insecure_channel('localhost:50051')
        self.message_stub = message_pb2_grpc.MessageStub(channel)
        self.file_stub = file_pb2_grpc.FileStub(channel)

    def single_message(self, text, chat_id, type='text'):
        client_type = ClientType(telegramm=ClientType.Telegramm(chat_id=chat_id))
        request = MessageRequest(body=text, type=type, client_type=client_type)
        feature = self.message_stub.SingleRequest(request)
        return feature.success

    def upload_file(self, filename):
        def chunk_file():
            yield FileRequest(name=filename)
            with open(filename, 'rb') as file:
                while True:
                    piece = file.read(self.CHUNK_SIZE)
                    if len(piece) == 0:
                        return
                    yield FileRequest(buffer=piece)

        result = self.file_stub.UploadFile(chunk_file())
        os.remove(filename)
        return result.text

    def stream_message(self):
        for r in self.message_stub.StreamRequest(Empty()):
            yield (r.body, r.client_type)
