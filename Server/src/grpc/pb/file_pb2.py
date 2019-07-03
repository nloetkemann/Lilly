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




DESCRIPTOR = _descriptor.FileDescriptor(
  name='src/grpc/pb/file.proto',
  package='proto.src.grpc.pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16src/grpc/pb/file.proto\x12\x11proto.src.grpc.pb\"\x1b\n\x0b\x46ileRequest\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t\"\x1c\n\x0c\x46ileResponse\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t2Y\n\x04\x46ile\x12Q\n\nUploadFile\x12\x1e.proto.src.grpc.pb.FileRequest\x1a\x1f.proto.src.grpc.pb.FileResponse\"\x00(\x01\x62\x06proto3')
)




_FILEREQUEST = _descriptor.Descriptor(
  name='FileRequest',
  full_name='proto.src.grpc.pb.FileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='body', full_name='proto.src.grpc.pb.FileRequest.body', index=0,
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
  serialized_start=45,
  serialized_end=72,
)


_FILERESPONSE = _descriptor.Descriptor(
  name='FileResponse',
  full_name='proto.src.grpc.pb.FileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='body', full_name='proto.src.grpc.pb.FileResponse.body', index=0,
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
  serialized_start=74,
  serialized_end=102,
)

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
  serialized_start=104,
  serialized_end=193,
  methods=[
  _descriptor.MethodDescriptor(
    name='UploadFile',
    full_name='proto.src.grpc.pb.File.UploadFile',
    index=0,
    containing_service=None,
    input_type=_FILEREQUEST,
    output_type=_FILERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILE)

DESCRIPTOR.services_by_name['File'] = _FILE

# @@protoc_insertion_point(module_scope)