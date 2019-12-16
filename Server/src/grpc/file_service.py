import src.grpc.pb.file_pb2_grpc as file_pb2_grpc
from src.grpc.pb import message_pb2
import itertools
from src.logic.handler import MessageHandler
from src.logic.message_queue import MessageQueue
from src.reponse import Response
from src.wit.wit import send_audio_file


class FileServicer(file_pb2_grpc.FileServicer):
    temp_dir = '../../temp/'

    def UploadFile(self, request_iterator, context):
        def save_chunks_to_file(parts):
            first_part = (list(itertools.islice(parts, 1))[0])
            name = first_part.name
            filename = self.temp_dir + name
            client_type = first_part.client_type
            file_mode = first_part.file_mode
            print(filename)
            with open(filename, 'wb') as f:
                for single_part in parts:
                    if not single_part.HasField('name'):
                        f.write(single_part.buffer)
            return filename, client_type, file_mode

        filename, client_type, file_mode = save_chunks_to_file(request_iterator)
        result = send_audio_file(filename)
        if file_mode == 'command':
            response = MessageHandler(result, client_type).handle_message()
            MessageQueue.add(response, client_type)
        elif file_mode == 'translate':
            MessageQueue.add(Response(result.text), client_type)
        return message_pb2.Success(success=True)
