# Python Evolution API

A Python wrapper for Evolution API, providing WhatsApp integration capabilities.

## Installation

This package requires Python 3.11+. You can install it using pip:

```bash
pip install python_evolution_api
```

## Quick Start

```python
from evolutionapi import EvolutionAPI

# Initialize the client
api = EvolutionAPI("https://evolution-api.example.com", "your-api-key")

# Create a WhatsApp instance
response = api.instances.create(
    instance_name="my-whatsapp",
    webhook="https://my-webhook.example.com"
)
print(f"Instance created: {response['instance']['instanceName']}")
```

## Features

- **Instance Management**: Create and manage WhatsApp instances
- **Proxy Support**: Connect through proxies with full authentication support
- **Configuration Options**: Extensive customization with webhook, websocket, message handling settings

## Development Setup

We use [uv](https://github.com/astral-sh/uv) for dependency management and virtual environments.

### Install uv

```bash
# MacOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows PowerShell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Create and activate virtual environment

```bash
# Create a virtual environment
uv venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

### Install dependencies

```bash
# Install the project in development mode with all dependencies
uv sync
```

## Testing

Run tests with pytest:

```bash
pytest
```

For test coverage:

```bash
pytest --cov=evolutionapi --cov-report=html
```

## Documentation

Build the documentation:

```bash
mkdocs build
```

Serve the documentation locally:

```bash
mkdocs serve
```

## Advanced Usage

### Creating an Instance with Custom Configuration

```python
from evolutionapi import EvolutionAPI
from evolutionapi.schemas import ProxySettings

# Initialize client
api = EvolutionAPI("https://evolution-api.example.com", "your-api-key")

# Configure a proxy
proxy = ProxySettings(
    host="proxy.example.com",
    port="8080",
    protocol="http",
    username="proxyuser",
    password="proxypass"
)

# Create an instance with advanced settings
response = api.instances.create(
    instance_name="business-whatsapp",
    webhook="https://webhook.example.com/events",
    webhook_by_events=True,
    events=["message", "status"],
    reject_call=True,
    msg_call="I'm busy at the moment",
    always_online=True,
    proxy=proxy
)
```

## Error Handling

```python
from evolutionapi import EvolutionAPI
from evolutionapi.exceptions import EvolutionAPIError

api = EvolutionAPI("https://evolution-api.example.com", "your-api-key")

try:
    response = api.instances.create(instance_name="my-whatsapp")
except EvolutionAPIError as e:
    print(f"Error {e.status_code}: {e.error_message}")
    if e.response:
        print(f"Response details: {e.response}")
```
