import os
import grpc
from urllib3.exceptions import ProtocolError
import src.grpc.pb.message_pb2_grpc as message_pb2_grpc
import src.grpc.pb.file_pb2_grpc as file_pb2_grpc
from src.grpc.pb.file_pb2 import FileRequest
from src.grpc.pb.message_pb2 import MessageRequest, Empty, ClientType
from src.logic.bot_handler import bothandler
from src.logic.thread import FunctionThread
from src.logic.command import CommandHandler

temp_dir = './temp/'


class Client:
    CHUNK_SIZE = 1024 * 512

    def __init__(self):
        print("Connect to " + os.getenv('SERVER') if os.getenv('SERVER') else 'localhost:50051')
        channel = grpc.insecure_channel(os.getenv('SERVER') if os.getenv('SERVER') else 'localhost:50051')
        self.message_stub = message_pb2_grpc.MessageStub(channel)
        self.file_stub = file_pb2_grpc.FileStub(channel)
        self.thread = FunctionThread(self._wait_for_response)
        self.thread.start()
        print('Bot is running')

    def single_message(self, text, chat_id, type='text'):
        client_type = ClientType(telegramm=ClientType.Telegramm(chat_id=chat_id))
        request = MessageRequest(body=text, type=type, client_type=client_type)
        feature = self.message_stub.SingleRequest(request)
        return feature.success

    def upload_file(self, filename, chat_id):
        def chunk_file():
            client_type = ClientType(telegramm=ClientType.Telegramm(chat_id=chat_id))
            yield FileRequest(name=filename, client_type=client_type, file_mode=CommandHandler.get_file_mode())
            with open(temp_dir + filename, 'rb') as file:
                while True:
                    piece = file.read(self.CHUNK_SIZE)
                    if len(piece) == 0:
                        return
                    yield FileRequest(buffer=piece)

        print(CommandHandler.get_file_mode())
        result = self.file_stub.UploadFile(chunk_file())
        os.remove(temp_dir + filename)
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
                try:
                    bothandler.bot.sendMessage(chat_id, response[0])
                except ProtocolError as e:
                    bothandler.restart()
                    bothandler.bot.sendMessage(chat_id, response[0])
