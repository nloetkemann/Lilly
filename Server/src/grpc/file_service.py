import os
import src.grpc.pb.file_pb2_grpc as file_pb2_grpc
from src.grpc.pb import file_pb2
import itertools


class FileServicer(file_pb2_grpc.FileServicer):
    temp_dir = '../../temp/'

    def UploadFile(self, request_iterator, context):
        def save_chunks_to_file(chunks):
            name = (list(itertools.islice(chunks, 1))[0]).name
            filename = self.temp_dir + name
            with open(filename, 'wb') as f:
                for chunk in chunks:
                    if not chunk.HasField('name'):
                        f.write(chunk.buffer)
            return filename

        filename = save_chunks_to_file(request_iterator)
        length = os.path.getsize(filename)
        return file_pb2.FileResponse(length=length)
