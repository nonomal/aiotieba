# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FrsPageReqIdl.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import CommonReq_pb2 as CommonReq__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x46rsPageReqIdl.proto\x1a\x0f\x43ommonReq.proto\"\xfb\x01\n\rFrsPageReqIdl\x12$\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x16.FrsPageReqIdl.DataReq\x1a\xc3\x01\n\x07\x44\x61taReq\x12\x1a\n\x06\x63ommon\x18\' \x01(\x0b\x32\n.CommonReq\x12\x12\n\nforum_name\x18\x15 \x01(\t\x12\n\n\x02kw\x18\x01 \x01(\t\x12\n\n\x02pn\x18\x0f \x01(\x05\x12\n\n\x02rn\x18\x02 \x01(\x05\x12\x0f\n\x07rn_need\x18\x03 \x01(\x05\x12\x0b\n\x03\x63id\x18\x05 \x01(\x05\x12\x0f\n\x07is_good\x18\x04 \x01(\x05\x12\x0e\n\x06q_type\x18\x0e \x01(\x05\x12\x11\n\tsort_type\x18/ \x01(\x05\x12\x12\n\nwith_group\x18\x08 \x01(\x05\x62\x06proto3')



_FRSPAGEREQIDL = DESCRIPTOR.message_types_by_name['FrsPageReqIdl']
_FRSPAGEREQIDL_DATAREQ = _FRSPAGEREQIDL.nested_types_by_name['DataReq']
FrsPageReqIdl = _reflection.GeneratedProtocolMessageType('FrsPageReqIdl', (_message.Message,), {

  'DataReq' : _reflection.GeneratedProtocolMessageType('DataReq', (_message.Message,), {
    'DESCRIPTOR' : _FRSPAGEREQIDL_DATAREQ,
    '__module__' : 'FrsPageReqIdl_pb2'
    # @@protoc_insertion_point(class_scope:FrsPageReqIdl.DataReq)
    })
  ,
  'DESCRIPTOR' : _FRSPAGEREQIDL,
  '__module__' : 'FrsPageReqIdl_pb2'
  # @@protoc_insertion_point(class_scope:FrsPageReqIdl)
  })
_sym_db.RegisterMessage(FrsPageReqIdl)
_sym_db.RegisterMessage(FrsPageReqIdl.DataReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FRSPAGEREQIDL._serialized_start=41
  _FRSPAGEREQIDL._serialized_end=292
  _FRSPAGEREQIDL_DATAREQ._serialized_start=97
  _FRSPAGEREQIDL_DATAREQ._serialized_end=292
# @@protoc_insertion_point(module_scope)
