import os
import src.grpc.pb.file_pb2_grpc as file_pb2_grpc
from src.grpc.pb import file_pb2


class FileServicer(file_pb2_grpc.FileServicer):
    temp_file = '../../temp/temp_file'

    def UploadFile(self, request_iterator, context):
        def save_chunks_to_file(chunks, filename):
            with open(filename, 'wb') as f:
                for chunk in chunks:
                    print(chunk)
                    f.write(chunk.buffer)

        print('File incomming')
        save_chunks_to_file(request_iterator, self.temp_file)
        length = os.path.getsize(self.temp_file)
        print('fertig')
        return file_pb2.FileResponse(length=length)
