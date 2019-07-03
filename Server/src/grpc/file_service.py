import src.grpc.pb.file_pb2_grpc as file_pb2_grpc
from src.grpc.pb import file_pb2


class FileServicer(file_pb2_grpc.FileServicer):
    def UploadFile(self, request_iterator, context):
        arr = []
        for item in request_iterator:
            arr.append(arr)

        # save to file

        return file_pb2.FileResponse(success=True)
