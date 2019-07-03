import time
from concurrent import futures
import grpc
import src.grpc.pb.message_pb2_grpc as message_pb2_grpc
import src.grpc.pb.file_pb2_grpc as file_pb2_grpc
from src.grpc.message_service import MessageServicer
from src.grpc.file_service import FileServicer


class Server:
    def __init__(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        message_pb2_grpc.add_MessageServicer_to_server(MessageServicer(), self.server)
        file_pb2_grpc.add_FileServicer_to_server(FileServicer(), self.server)

    def start(self):
        print('Starting server. Listening on port 50051.')
        self.server.add_insecure_port('[::]:50051')
        self.server.start()
        try:
            while True:
                time.sleep(86400)
        except KeyboardInterrupt:
            self.server.stop(0)


server = Server()
server.start()
