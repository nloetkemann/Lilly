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


class Client:
    CHUNK_SIZE = 1024 * 512

    def __init__(self):
        channel = grpc.insecure_channel('localhost:50051')
        self.message_stub = message_pb2_grpc.MessageStub(channel)
        self.file_stub = file_pb2_grpc.FileStub(channel)
        self.thread = FunctionThread(self._wait_for_response)
        self.thread.start()

    def upload_file(self, audio_data):
        def chunk_file():
            client_type = ClientType(telegramm=ClientType.LA())
            yield FileRequest(name='temp.wav', client_type=client_type)
            while True:
                # piece = file.read(self.CHUNK_SIZE)
                # if len(piece) == 0:
                #     return
                yield FileRequest(buffer=audio_data)

        result = self.file_stub.UploadFile(chunk_file())
        return result.success

    def _get_messages_from_server(self):
        for r in self.message_stub.StreamRequest(Empty()):
            yield (r.body, r.client_type)

    def _wait_for_response(self, stop_thread):  # todo muss noch stopthread einbauen
        responses = self._get_messages_from_server()
        for response in responses:
            client_type = response[1]
            if client_type.telegramm is not None and client_type.telegramm != '':
                chat_id = client_type.telegramm.chat_id
                # bothandler.bot.sendMessage(chat_id, response[0])
                text_2_voice(response[0])
