# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/grpc/pb/file.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from src.grpc.pb import message_pb2 as src_dot_grpc_dot_pb_dot_message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='src/grpc/pb/file.proto',
  package='proto.src.grpc.pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16src/grpc/pb/file.proto\x12\x11proto.src.grpc.pb\x1a\x19src/grpc/pb/message.proto\"~\n\x0b\x46ileRequest\x12\x10\n\x06\x62uffer\x18\x01 \x01(\x0cH\x00\x12\x0e\n\x04name\x18\x02 \x01(\tH\x00\x12\x32\n\x0b\x63lient_type\x18\x03 \x01(\x0b\x32\x1d.proto.src.grpc.pb.ClientType\x12\x11\n\tfile_mode\x18\x04 \x01(\tB\x06\n\x04type\"\x1c\n\x0c\x46ileResponse\x12\x0c\n\x04text\x18\x01 \x01(\t2T\n\x04\x46ile\x12L\n\nUploadFile\x12\x1e.proto.src.grpc.pb.FileRequest\x1a\x1a.proto.src.grpc.pb.Success\"\x00(\x01\x62\x06proto3')
  ,
  dependencies=[src_dot_grpc_dot_pb_dot_message__pb2.DESCRIPTOR,])




_FILEREQUEST = _descriptor.Descriptor(
  name='FileRequest',
  full_name='proto.src.grpc.pb.FileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buffer', full_name='proto.src.grpc.pb.FileRequest.buffer', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.src.grpc.pb.FileRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_type', full_name='proto.src.grpc.pb.FileRequest.client_type', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_mode', full_name='proto.src.grpc.pb.FileRequest.file_mode', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='proto.src.grpc.pb.FileRequest.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=72,
  serialized_end=198,
)


_FILERESPONSE = _descriptor.Descriptor(
  name='FileResponse',
  full_name='proto.src.grpc.pb.FileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='proto.src.grpc.pb.FileResponse.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=228,
)

_FILEREQUEST.fields_by_name['client_type'].message_type = src_dot_grpc_dot_pb_dot_message__pb2._CLIENTTYPE
_FILEREQUEST.oneofs_by_name['type'].fields.append(
  _FILEREQUEST.fields_by_name['buffer'])
_FILEREQUEST.fields_by_name['buffer'].containing_oneof = _FILEREQUEST.oneofs_by_name['type']
_FILEREQUEST.oneofs_by_name['type'].fields.append(
  _FILEREQUEST.fields_by_name['name'])
_FILEREQUEST.fields_by_name['name'].containing_oneof = _FILEREQUEST.oneofs_by_name['type']
DESCRIPTOR.message_types_by_name['FileRequest'] = _FILEREQUEST
DESCRIPTOR.message_types_by_name['FileResponse'] = _FILERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileRequest = _reflection.GeneratedProtocolMessageType('FileRequest', (_message.Message,), dict(
  DESCRIPTOR = _FILEREQUEST,
  __module__ = 'src.grpc.pb.file_pb2'
  # @@protoc_insertion_point(class_scope:proto.src.grpc.pb.FileRequest)
  ))
_sym_db.RegisterMessage(FileRequest)

FileResponse = _reflection.GeneratedProtocolMessageType('FileResponse', (_message.Message,), dict(
  DESCRIPTOR = _FILERESPONSE,
  __module__ = 'src.grpc.pb.file_pb2'
  # @@protoc_insertion_point(class_scope:proto.src.grpc.pb.FileResponse)
  ))
_sym_db.RegisterMessage(FileResponse)



_FILE = _descriptor.ServiceDescriptor(
  name='File',
  full_name='proto.src.grpc.pb.File',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=230,
  serialized_end=314,
  methods=[
  _descriptor.MethodDescriptor(
    name='UploadFile',
    full_name='proto.src.grpc.pb.File.UploadFile',
    index=0,
    containing_service=None,
    input_type=_FILEREQUEST,
    output_type=src_dot_grpc_dot_pb_dot_message__pb2._SUCCESS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILE)

DESCRIPTOR.services_by_name['File'] = _FILE

# @@protoc_insertion_point(module_scope)
