import device_info_pb2 as _device_info_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVENT_TYPE_UNSPECIFIED: _ClassVar[EventType]
    EVENT_TYPE_TIMER: _ClassVar[EventType]
    EVENT_TYPE_PROVISIONING_REQUESTED: _ClassVar[EventType]
    EVENT_TYPE_MQTT_CONNECTED: _ClassVar[EventType]
    EVENT_TYPE_REBOOT_REQUESTED: _ClassVar[EventType]
    EVENT_TYPE_BOOT_UNKNOWN: _ClassVar[EventType]
    EVENT_TYPE_BOOT_SOFTWARE: _ClassVar[EventType]
    EVENT_TYPE_BOOT_POWER_ON: _ClassVar[EventType]
    EVENT_TYPE_BOOT_WATCHDOG: _ClassVar[EventType]
EVENT_TYPE_UNSPECIFIED: EventType
EVENT_TYPE_TIMER: EventType
EVENT_TYPE_PROVISIONING_REQUESTED: EventType
EVENT_TYPE_MQTT_CONNECTED: EventType
EVENT_TYPE_REBOOT_REQUESTED: EventType
EVENT_TYPE_BOOT_UNKNOWN: EventType
EVENT_TYPE_BOOT_SOFTWARE: EventType
EVENT_TYPE_BOOT_POWER_ON: EventType
EVENT_TYPE_BOOT_WATCHDOG: EventType

class Counters(_message.Message):
    __slots__ = ("hawkbit_status_connection_error", "hawkbit_status_unconfirmed_image", "hawkbit_status_metadata_error", "hawkbit_status_download_error", "hawkbit_status_already_updated", "hawkbit_status_update_downloaded", "hawkbit_status_no_update", "hawkbit_status_cancel_update", "hawkbit_status_probe_in_progress", "timeout_internet_unreachable", "timeout_hawkbit_connection", "han_msg_successfully_parsed", "han_msg_buffer_overflow")
    HAWKBIT_STATUS_CONNECTION_ERROR_FIELD_NUMBER: _ClassVar[int]
    HAWKBIT_STATUS_UNCONFIRMED_IMAGE_FIELD_NUMBER: _ClassVar[int]
    HAWKBIT_STATUS_METADATA_ERROR_FIELD_NUMBER: _ClassVar[int]
    HAWKBIT_STATUS_DOWNLOAD_ERROR_FIELD_NUMBER: _ClassVar[int]
    HAWKBIT_STATUS_ALREADY_UPDATED_FIELD_NUMBER: _ClassVar[int]
    HAWKBIT_STATUS_UPDATE_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    HAWKBIT_STATUS_NO_UPDATE_FIELD_NUMBER: _ClassVar[int]
    HAWKBIT_STATUS_CANCEL_UPDATE_FIELD_NUMBER: _ClassVar[int]
    HAWKBIT_STATUS_PROBE_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_INTERNET_UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_HAWKBIT_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    HAN_MSG_SUCCESSFULLY_PARSED_FIELD_NUMBER: _ClassVar[int]
    HAN_MSG_BUFFER_OVERFLOW_FIELD_NUMBER: _ClassVar[int]
    hawkbit_status_connection_error: int
    hawkbit_status_unconfirmed_image: int
    hawkbit_status_metadata_error: int
    hawkbit_status_download_error: int
    hawkbit_status_already_updated: int
    hawkbit_status_update_downloaded: int
    hawkbit_status_no_update: int
    hawkbit_status_cancel_update: int
    hawkbit_status_probe_in_progress: int
    timeout_internet_unreachable: int
    timeout_hawkbit_connection: int
    han_msg_successfully_parsed: int
    han_msg_buffer_overflow: int
    def __init__(self, hawkbit_status_connection_error: _Optional[int] = ..., hawkbit_status_unconfirmed_image: _Optional[int] = ..., hawkbit_status_metadata_error: _Optional[int] = ..., hawkbit_status_download_error: _Optional[int] = ..., hawkbit_status_already_updated: _Optional[int] = ..., hawkbit_status_update_downloaded: _Optional[int] = ..., hawkbit_status_no_update: _Optional[int] = ..., hawkbit_status_cancel_update: _Optional[int] = ..., hawkbit_status_probe_in_progress: _Optional[int] = ..., timeout_internet_unreachable: _Optional[int] = ..., timeout_hawkbit_connection: _Optional[int] = ..., han_msg_successfully_parsed: _Optional[int] = ..., han_msg_buffer_overflow: _Optional[int] = ...) -> None: ...

class Diagnostic(_message.Message):
    __slots__ = ("type", "uptime_s", "wifi_rssi_dbm", "device_info", "counters")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UPTIME_S_FIELD_NUMBER: _ClassVar[int]
    WIFI_RSSI_DBM_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    COUNTERS_FIELD_NUMBER: _ClassVar[int]
    type: EventType
    uptime_s: int
    wifi_rssi_dbm: int
    device_info: _device_info_pb2.DeviceInfo
    counters: Counters
    def __init__(self, type: _Optional[_Union[EventType, str]] = ..., uptime_s: _Optional[int] = ..., wifi_rssi_dbm: _Optional[int] = ..., device_info: _Optional[_Union[_device_info_pb2.DeviceInfo, _Mapping]] = ..., counters: _Optional[_Union[Counters, _Mapping]] = ...) -> None: ...
