import grpc
import src.grpc.pb.message_pb2_grpc as message_pb2_grpc
import src.grpc.pb.file_pb2_grpc as file_pb2_grpc
from src.grpc.pb.file_pb2 import FileRequest
from src.grpc.pb.message_pb2 import MessageRequest


class Client:
    CHUNK_SIZE = 1024 * 1024

    def __init__(self):
        channel = grpc.insecure_channel('localhost:50051')
        self.message_stub = message_pb2_grpc.MessageStub(channel)
        self.file_stub = file_pb2_grpc.FileStub(channel)

    def single_message(self, text, type='text'):
        request = MessageRequest(body=text, type=type)
        feature = self.message_stub.SingleRequest(request)
        return feature.body

    def upload_file(self, filename):
        def chunk_file():
            with open(filename, 'rb') as file:
                piece = file.read(self.CHUNK_SIZE)
                if len(piece) == 0:
                    return
                yield FileRequest(buffer=piece)
        result = self.file_stub.UploadFile(chunk_file())
        return result.length

    def stream_message(self, text_array):
        def gen_request(messages, origin):
            for text in messages:
                request = MessageRequest(body=text, origin=origin)
                yield request

        it = self.message_stub.StreamRequest(gen_request(text_array, 'was geht ab'))
        array = []
        for r in it:
            array.append(r.body)
        return array
