# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FrsPageResIdl.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import ForumInfo_pb2 as ForumInfo__pb2
from . import Page_pb2 as Page__pb2
from . import ThreadInfo_pb2 as ThreadInfo__pb2
from . import User_pb2 as User__pb2
from . import Error_pb2 as Error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x46rsPageResIdl.proto\x1a\x0f\x46orumInfo.proto\x1a\nPage.proto\x1a\x10ThreadInfo.proto\x1a\nUser.proto\x1a\x0b\x45rror.proto\"\xc3\x01\n\rFrsPageResIdl\x12\x15\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x06.Error\x12$\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x16.FrsPageResIdl.DataRes\x1au\n\x07\x44\x61taRes\x12\x19\n\x05\x66orum\x18\x02 \x01(\x0b\x32\n.ForumInfo\x12\x13\n\x04page\x18\x04 \x01(\x0b\x32\x05.Page\x12 \n\x0bthread_list\x18\x07 \x03(\x0b\x32\x0b.ThreadInfo\x12\x18\n\tuser_list\x18\x11 \x03(\x0b\x32\x05.Userb\x06proto3')



_FRSPAGERESIDL = DESCRIPTOR.message_types_by_name['FrsPageResIdl']
_FRSPAGERESIDL_DATARES = _FRSPAGERESIDL.nested_types_by_name['DataRes']
FrsPageResIdl = _reflection.GeneratedProtocolMessageType('FrsPageResIdl', (_message.Message,), {

  'DataRes' : _reflection.GeneratedProtocolMessageType('DataRes', (_message.Message,), {
    'DESCRIPTOR' : _FRSPAGERESIDL_DATARES,
    '__module__' : 'FrsPageResIdl_pb2'
    # @@protoc_insertion_point(class_scope:FrsPageResIdl.DataRes)
    })
  ,
  'DESCRIPTOR' : _FRSPAGERESIDL,
  '__module__' : 'FrsPageResIdl_pb2'
  # @@protoc_insertion_point(class_scope:FrsPageResIdl)
  })
_sym_db.RegisterMessage(FrsPageResIdl)
_sym_db.RegisterMessage(FrsPageResIdl.DataRes)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FRSPAGERESIDL._serialized_start=96
  _FRSPAGERESIDL._serialized_end=291
  _FRSPAGERESIDL_DATARES._serialized_start=174
  _FRSPAGERESIDL_DATARES._serialized_end=291
# @@protoc_insertion_point(module_scope)
