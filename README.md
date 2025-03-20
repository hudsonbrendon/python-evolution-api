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

## Features Checklist

### Instances
- ✅ Create Instance Basic
- ✅ Fetch Instances
- Instance Connect
- Restart Instance
- Connection State
- Logout Instance
- Delete Instance
- Set Presence

### Webhook
- Set Webhook
- Find Webhook

### Settings
- Set Settings
- Find Settings

### Send Message
- Send Template
- Send Plain Text
- Send Status
- Send Media
- Send WhatsApp Audio
- Send Sticker
- Send Location
- Send Contact
- Send Reaction
- Send Poll
- Send List

### Chat Controller
- Check is WhatsApp
- Mark Message As Read
- Archive Chat
- Delete Message for Everyone
- Send Presence
- Fetch Profile Picture URL
- Find Contacts
- Find Messages
- Find Status Message
- Update Message
- Find Chats

### Profile Settings
- Fetch Business Profile
- Fetch Profile
- Update Profile Name
- Update Profile Status
- Update Profile Picture
- Remove Profile Picture
- Fetch Privacy Settings
- Update Privacy Settings

### Group Controller
- Create Group
- Update Group Picture
- Update Group Subject
- Update Group Description
- Fetch Invite Code
- Accept Invite Code
- Revoke Invite Code
- Send Group Invite
- Find Group by Invite Code
- Find Group by JID
- Fetch All Groups
- Find Group Members
- Update Group Members
- Update Group Setting
- Toggle Ephemeral
- Leave Group

### Integrations
- Typebot
- Chatwoot
- SQS
- RabbitMQ
- WebSocket

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
