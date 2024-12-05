# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ml_services.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'ml_services.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11ml_services.proto\"\"\n\x0cImageRequest\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\"\x1f\n\rImageResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"?\n\x10NutritionRequest\x12\x0e\n\x06height\x18\x01 \x01(\x02\x12\x0e\n\x06weight\x18\x02 \x01(\x02\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\"-\n\x11NutritionResponse\x12\x18\n\x10nutrition_status\x18\x01 \x01(\t\"\xa9\x01\n\x0fStuntingRequest\x12\x0b\n\x03\x61ge\x18\x01 \x01(\x05\x12\x14\n\x0c\x62irth_weight\x18\x02 \x01(\x02\x12\x14\n\x0c\x62irth_length\x18\x03 \x01(\x05\x12\x13\n\x0b\x62ody_weight\x18\x04 \x01(\x02\x12\x13\n\x0b\x62ody_length\x18\x05 \x01(\x02\x12\x1a\n\x12is_sanitized_place\x18\x06 \x01(\x05\x12\x17\n\x0fis_healthy_food\x18\x07 \x01(\x05\"+\n\x10StuntingResponse\x12\x17\n\x0fstunting_status\x18\x01 \x01(\t\"\x07\n\x05\x45mpty\" \n\x0eHealthResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\xd7\x01\n\tMLService\x12/\n\x0eImageDetection\x12\r.ImageRequest\x1a\x0e.ImageResponse\x12\x39\n\x10PredictNutrition\x12\x11.NutritionRequest\x1a\x12.NutritionResponse\x12\x36\n\x0fPredictStunting\x12\x10.StuntingRequest\x1a\x11.StuntingResponse\x12&\n\x0bHealthCheck\x12\x06.Empty\x1a\x0f.HealthResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ml_services_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_IMAGEREQUEST']._serialized_start=21
  _globals['_IMAGEREQUEST']._serialized_end=55
  _globals['_IMAGERESPONSE']._serialized_start=57
  _globals['_IMAGERESPONSE']._serialized_end=88
  _globals['_NUTRITIONREQUEST']._serialized_start=90
  _globals['_NUTRITIONREQUEST']._serialized_end=153
  _globals['_NUTRITIONRESPONSE']._serialized_start=155
  _globals['_NUTRITIONRESPONSE']._serialized_end=200
  _globals['_STUNTINGREQUEST']._serialized_start=203
  _globals['_STUNTINGREQUEST']._serialized_end=372
  _globals['_STUNTINGRESPONSE']._serialized_start=374
  _globals['_STUNTINGRESPONSE']._serialized_end=417
  _globals['_EMPTY']._serialized_start=419
  _globals['_EMPTY']._serialized_end=426
  _globals['_HEALTHRESPONSE']._serialized_start=428
  _globals['_HEALTHRESPONSE']._serialized_end=460
  _globals['_MLSERVICE']._serialized_start=463
  _globals['_MLSERVICE']._serialized_end=678
# @@protoc_insertion_point(module_scope)