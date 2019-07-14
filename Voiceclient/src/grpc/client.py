import os
import grpc
import src.grpc.pb.message_pb2_grpc as message_pb2_grpc
import src.grpc.pb.file_pb2_grpc as file_pb2_grpc
from src.grpc.pb.file_pb2 import FileRequest
from src.grpc.pb.message_pb2 import MessageRequest, Empty, ClientType
# from src.logic.bot_handler import bothandler
from src.logic.text_to_voice import text_2_voice
from src.logic.thread import FunctionThread
from src.logic.voice_to_text import voice_2_text

temp_dir = './temp/'

class Client:
    CHUNK_SIZE = 1024 * 512

    def __init__(self):
        channel = grpc.insecure_channel('192.168.178.23:50051')
        self.message_stub = message_pb2_grpc.MessageStub(channel)
        self.file_stub = file_pb2_grpc.FileStub(channel)
        self.thread = FunctionThread(self._wait_for_response)
        self.thread.start()

    def upload_file(self, filename):
        def chunk_file():
            client_type = ClientType(la=ClientType.LA())
            yield FileRequest(name=filename, client_type=client_type)
            with open(temp_dir + filename, 'rb') as file:
                while True:
                    piece = file.read(self.CHUNK_SIZE)
                    if len(piece) == 0:
                        return
                    yield FileRequest(buffer=piece)

        result = self.file_stub.UploadFile(chunk_file())
        os.remove(temp_dir + filename)
        return result.success

    def _get_messages_from_server(self):
        for r in self.message_stub.StreamRequest(Empty()):
            yield (r.body, r.client_type)

    def _wait_for_response(self, stop_thread):  # todo muss noch stopthread einbauen
        responses = self._get_messages_from_server()
        print('waiting for response')
        for response in responses:
            client_type = response[1]
            print(response)
            if client_type.la is not None and client_type.la != '':
                text_2_voice(response[0])
