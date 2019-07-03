# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from src.grpc.pb import file_pb2 as src_dot_grpc_dot_pb_dot_file__pb2


class FileStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UploadFile = channel.stream_unary(
        '/proto.src.grpc.pb.File/UploadFile',
        request_serializer=src_dot_grpc_dot_pb_dot_file__pb2.FileRequest.SerializeToString,
        response_deserializer=src_dot_grpc_dot_pb_dot_file__pb2.FileResponse.FromString,
        )


class FileServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def UploadFile(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FileServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UploadFile': grpc.stream_unary_rpc_method_handler(
          servicer.UploadFile,
          request_deserializer=src_dot_grpc_dot_pb_dot_file__pb2.FileRequest.FromString,
          response_serializer=src_dot_grpc_dot_pb_dot_file__pb2.FileResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.src.grpc.pb.File', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))