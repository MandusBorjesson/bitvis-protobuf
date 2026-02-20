from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HanPortSample(_message.Message):
    __slots__ = ("timestamp_utc_meter_s", "timestamp_utc_ntp_s", "energy_active_delivered_to_client_kwh", "energy_active_delivered_by_client_kwh", "energy_reactive_delivered_to_client_kvarh", "energy_reactive_delivered_by_client_kvarh", "power_active_delivered_to_client_kw", "power_active_delivered_by_client_kw", "power_reactive_delivered_to_client_kvar", "power_reactive_delivered_by_client_kvar", "power_active_l1_delivered_to_client_kw", "power_active_l1_delivered_by_client_kw", "power_active_l2_delivered_to_client_kw", "power_active_l2_delivered_by_client_kw", "power_active_l3_delivered_to_client_kw", "power_active_l3_delivered_by_client_kw", "power_reactive_l1_delivered_to_client_kvar", "power_reactive_l1_delivered_by_client_kvar", "power_reactive_l2_delivered_to_client_kvar", "power_reactive_l2_delivered_by_client_kvar", "power_reactive_l3_delivered_to_client_kvar", "power_reactive_l3_delivered_by_client_kvar", "phase_voltage_l1_v", "phase_voltage_l2_v", "phase_voltage_l3_v", "phase_current_l1_a", "phase_current_l2_a", "phase_current_l3_a")
    TIMESTAMP_UTC_METER_S_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_UTC_NTP_S_FIELD_NUMBER: _ClassVar[int]
    ENERGY_ACTIVE_DELIVERED_TO_CLIENT_KWH_FIELD_NUMBER: _ClassVar[int]
    ENERGY_ACTIVE_DELIVERED_BY_CLIENT_KWH_FIELD_NUMBER: _ClassVar[int]
    ENERGY_REACTIVE_DELIVERED_TO_CLIENT_KVARH_FIELD_NUMBER: _ClassVar[int]
    ENERGY_REACTIVE_DELIVERED_BY_CLIENT_KVARH_FIELD_NUMBER: _ClassVar[int]
    POWER_ACTIVE_DELIVERED_TO_CLIENT_KW_FIELD_NUMBER: _ClassVar[int]
    POWER_ACTIVE_DELIVERED_BY_CLIENT_KW_FIELD_NUMBER: _ClassVar[int]
    POWER_REACTIVE_DELIVERED_TO_CLIENT_KVAR_FIELD_NUMBER: _ClassVar[int]
    POWER_REACTIVE_DELIVERED_BY_CLIENT_KVAR_FIELD_NUMBER: _ClassVar[int]
    POWER_ACTIVE_L1_DELIVERED_TO_CLIENT_KW_FIELD_NUMBER: _ClassVar[int]
    POWER_ACTIVE_L1_DELIVERED_BY_CLIENT_KW_FIELD_NUMBER: _ClassVar[int]
    POWER_ACTIVE_L2_DELIVERED_TO_CLIENT_KW_FIELD_NUMBER: _ClassVar[int]
    POWER_ACTIVE_L2_DELIVERED_BY_CLIENT_KW_FIELD_NUMBER: _ClassVar[int]
    POWER_ACTIVE_L3_DELIVERED_TO_CLIENT_KW_FIELD_NUMBER: _ClassVar[int]
    POWER_ACTIVE_L3_DELIVERED_BY_CLIENT_KW_FIELD_NUMBER: _ClassVar[int]
    POWER_REACTIVE_L1_DELIVERED_TO_CLIENT_KVAR_FIELD_NUMBER: _ClassVar[int]
    POWER_REACTIVE_L1_DELIVERED_BY_CLIENT_KVAR_FIELD_NUMBER: _ClassVar[int]
    POWER_REACTIVE_L2_DELIVERED_TO_CLIENT_KVAR_FIELD_NUMBER: _ClassVar[int]
    POWER_REACTIVE_L2_DELIVERED_BY_CLIENT_KVAR_FIELD_NUMBER: _ClassVar[int]
    POWER_REACTIVE_L3_DELIVERED_TO_CLIENT_KVAR_FIELD_NUMBER: _ClassVar[int]
    POWER_REACTIVE_L3_DELIVERED_BY_CLIENT_KVAR_FIELD_NUMBER: _ClassVar[int]
    PHASE_VOLTAGE_L1_V_FIELD_NUMBER: _ClassVar[int]
    PHASE_VOLTAGE_L2_V_FIELD_NUMBER: _ClassVar[int]
    PHASE_VOLTAGE_L3_V_FIELD_NUMBER: _ClassVar[int]
    PHASE_CURRENT_L1_A_FIELD_NUMBER: _ClassVar[int]
    PHASE_CURRENT_L2_A_FIELD_NUMBER: _ClassVar[int]
    PHASE_CURRENT_L3_A_FIELD_NUMBER: _ClassVar[int]
    timestamp_utc_meter_s: int
    timestamp_utc_ntp_s: int
    energy_active_delivered_to_client_kwh: float
    energy_active_delivered_by_client_kwh: float
    energy_reactive_delivered_to_client_kvarh: float
    energy_reactive_delivered_by_client_kvarh: float
    power_active_delivered_to_client_kw: float
    power_active_delivered_by_client_kw: float
    power_reactive_delivered_to_client_kvar: float
    power_reactive_delivered_by_client_kvar: float
    power_active_l1_delivered_to_client_kw: float
    power_active_l1_delivered_by_client_kw: float
    power_active_l2_delivered_to_client_kw: float
    power_active_l2_delivered_by_client_kw: float
    power_active_l3_delivered_to_client_kw: float
    power_active_l3_delivered_by_client_kw: float
    power_reactive_l1_delivered_to_client_kvar: float
    power_reactive_l1_delivered_by_client_kvar: float
    power_reactive_l2_delivered_to_client_kvar: float
    power_reactive_l2_delivered_by_client_kvar: float
    power_reactive_l3_delivered_to_client_kvar: float
    power_reactive_l3_delivered_by_client_kvar: float
    phase_voltage_l1_v: float
    phase_voltage_l2_v: float
    phase_voltage_l3_v: float
    phase_current_l1_a: float
    phase_current_l2_a: float
    phase_current_l3_a: float
    def __init__(self, timestamp_utc_meter_s: _Optional[int] = ..., timestamp_utc_ntp_s: _Optional[int] = ..., energy_active_delivered_to_client_kwh: _Optional[float] = ..., energy_active_delivered_by_client_kwh: _Optional[float] = ..., energy_reactive_delivered_to_client_kvarh: _Optional[float] = ..., energy_reactive_delivered_by_client_kvarh: _Optional[float] = ..., power_active_delivered_to_client_kw: _Optional[float] = ..., power_active_delivered_by_client_kw: _Optional[float] = ..., power_reactive_delivered_to_client_kvar: _Optional[float] = ..., power_reactive_delivered_by_client_kvar: _Optional[float] = ..., power_active_l1_delivered_to_client_kw: _Optional[float] = ..., power_active_l1_delivered_by_client_kw: _Optional[float] = ..., power_active_l2_delivered_to_client_kw: _Optional[float] = ..., power_active_l2_delivered_by_client_kw: _Optional[float] = ..., power_active_l3_delivered_to_client_kw: _Optional[float] = ..., power_active_l3_delivered_by_client_kw: _Optional[float] = ..., power_reactive_l1_delivered_to_client_kvar: _Optional[float] = ..., power_reactive_l1_delivered_by_client_kvar: _Optional[float] = ..., power_reactive_l2_delivered_to_client_kvar: _Optional[float] = ..., power_reactive_l2_delivered_by_client_kvar: _Optional[float] = ..., power_reactive_l3_delivered_to_client_kvar: _Optional[float] = ..., power_reactive_l3_delivered_by_client_kvar: _Optional[float] = ..., phase_voltage_l1_v: _Optional[float] = ..., phase_voltage_l2_v: _Optional[float] = ..., phase_voltage_l3_v: _Optional[float] = ..., phase_current_l1_a: _Optional[float] = ..., phase_current_l2_a: _Optional[float] = ..., phase_current_l3_a: _Optional[float] = ...) -> None: ...
