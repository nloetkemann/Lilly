# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from src.grpc.pb import message_pb2 as src_dot_grpc_dot_pb_dot_message__pb2


class MessageStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SingleRequest = channel.unary_unary(
        '/proto.src.grpc.pb.Message/SingleRequest',
        request_serializer=src_dot_grpc_dot_pb_dot_message__pb2.MessageRequest.SerializeToString,
        response_deserializer=src_dot_grpc_dot_pb_dot_message__pb2.Success.FromString,
        )
    self.StreamRequest = channel.unary_stream(
        '/proto.src.grpc.pb.Message/StreamRequest',
        request_serializer=src_dot_grpc_dot_pb_dot_message__pb2.Empty.SerializeToString,
        response_deserializer=src_dot_grpc_dot_pb_dot_message__pb2.MessageResponse.FromString,
        )


class MessageServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SingleRequest(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamRequest(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MessageServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SingleRequest': grpc.unary_unary_rpc_method_handler(
          servicer.SingleRequest,
          request_deserializer=src_dot_grpc_dot_pb_dot_message__pb2.MessageRequest.FromString,
          response_serializer=src_dot_grpc_dot_pb_dot_message__pb2.Success.SerializeToString,
      ),
      'StreamRequest': grpc.unary_stream_rpc_method_handler(
          servicer.StreamRequest,
          request_deserializer=src_dot_grpc_dot_pb_dot_message__pb2.Empty.FromString,
          response_serializer=src_dot_grpc_dot_pb_dot_message__pb2.MessageResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.src.grpc.pb.Message', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
