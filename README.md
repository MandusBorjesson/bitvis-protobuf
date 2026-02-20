# Bitvis Protobuf

Python protobuf definitions for Bitvis Power Hub communication.

## Description

This library contains the Protocol Buffer definitions and generated Python code for communicating with Bitvis Power Hub devices. It includes message definitions for:

- Device information
- Diagnostic data
- HAN port samples
- Power hub payloads

## Installation

```bash
pip install bitvis-protobuf
```

## Usage

```python
from bitvis_protobuf import powerhub_pb2, han_port_pb2, diagnostic_pb2

# Parse a payload
payload = powerhub_pb2.Payload()
payload.ParseFromString(data)

if payload.HasField("sample"):
    sample = payload.sample
    # Process HAN port sample data
    
elif payload.HasField("diagnostic"):
    diagnostic = payload.diagnostic
    # Process diagnostic data
```

## Development

### Building from source

```bash
# Install development dependencies
pip install -e ".[dev]"

# Generate protobuf code
python -m build_proto
```

### Regenerating protobuf code

```bash
python scripts/generate_proto.py
```

## License

Apache License 2.0
