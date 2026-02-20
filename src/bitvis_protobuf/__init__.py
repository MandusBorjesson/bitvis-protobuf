"""Bitvis Power Hub protobuf definitions."""

from __future__ import annotations

__version__ = "0.1.0"

# Re-export generated protobuf modules for convenience
from . import device_info_pb2, diagnostic_pb2, han_port_pb2, powerhub_pb2

__all__ = [
    "device_info_pb2",
    "diagnostic_pb2",
    "han_port_pb2",
    "powerhub_pb2",
]
