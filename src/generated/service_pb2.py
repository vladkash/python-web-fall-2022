# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rservice.proto\"6\n\x0f\x43onsumptionInfo\x12\x13\n\x0b\x63\x61rd_number\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x02\"\"\n\x0fReceiptResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2B\n\x0bTestService\x12\x33\n\rCreateReceipt\x12\x10.ConsumptionInfo\x1a\x10.ReceiptResponseb\x06proto3'
)




_CONSUMPTIONINFO = _descriptor.Descriptor(
  name='ConsumptionInfo',
  full_name='ConsumptionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='card_number', full_name='ConsumptionInfo.card_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='ConsumptionInfo.amount', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=17,
  serialized_end=71,
)


_RECEIPTRESPONSE = _descriptor.Descriptor(
  name='ReceiptResponse',
  full_name='ReceiptResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='ReceiptResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=73,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['ConsumptionInfo'] = _CONSUMPTIONINFO
DESCRIPTOR.message_types_by_name['ReceiptResponse'] = _RECEIPTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConsumptionInfo = _reflection.GeneratedProtocolMessageType('ConsumptionInfo', (_message.Message,), {
  'DESCRIPTOR' : _CONSUMPTIONINFO,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:ConsumptionInfo)
  })
_sym_db.RegisterMessage(ConsumptionInfo)

ReceiptResponse = _reflection.GeneratedProtocolMessageType('ReceiptResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECEIPTRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:ReceiptResponse)
  })
_sym_db.RegisterMessage(ReceiptResponse)



_TESTSERVICE = _descriptor.ServiceDescriptor(
  name='TestService',
  full_name='TestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=109,
  serialized_end=175,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateReceipt',
    full_name='TestService.CreateReceipt',
    index=0,
    containing_service=None,
    input_type=_CONSUMPTIONINFO,
    output_type=_RECEIPTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name['TestService'] = _TESTSERVICE

# @@protoc_insertion_point(module_scope)
