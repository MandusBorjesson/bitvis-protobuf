from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceInfo(_message.Message):
    __slots__ = ("mac_address", "model_name", "sw_version", "hw_revision")
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    SW_VERSION_FIELD_NUMBER: _ClassVar[int]
    HW_REVISION_FIELD_NUMBER: _ClassVar[int]
    mac_address: bytes
    model_name: str
    sw_version: str
    hw_revision: int
    def __init__(self, mac_address: _Optional[bytes] = ..., model_name: _Optional[str] = ..., sw_version: _Optional[str] = ..., hw_revision: _Optional[int] = ...) -> None: ...
