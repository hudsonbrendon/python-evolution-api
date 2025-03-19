# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

# Python Evolution API

A Python wrapper for the Evolution API, which provides WhatsApp integration capabilities.

## Installation

```bash
pip install python_evolution_api
```

## Basic Usage

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

## API Reference

### EvolutionAPI Client

The main client class that handles communication with the Evolution API.

```python
from evolutionapi import EvolutionAPI

# Initialize with your server URL and API key
api = EvolutionAPI(base_url="https://evolution-api.example.com", api_key="your-api-key")
```

The client automatically handles:
- Authentication with your API key
- JSON request and response formatting
- Error handling and exceptions
- Resource management for different API endpoints

### Instance Management

The `instances` resource allows you to create and manage WhatsApp instances.

#### Creating an Instance

```python
# Create a basic instance
response = api.instances.create(instance_name="my-whatsapp")

# Create an instance with a QR code for authentication
response = api.instances.create(
    instance_name="my-whatsapp",
    qrcode=True
)

# Create an instance with a custom token
response = api.instances.create(
    instance_name="my-whatsapp",
    token="my-custom-token"
)
```

#### Advanced Instance Configuration

The `create` method accepts numerous parameters to customize your WhatsApp instance:

```python
from evolutionapi.schemas import ProxySettings

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
    token="custom-token",
    qrcode=True,
    number="1234567890",
    integration="WHATSAPP-BAILEYS",
    webhook="https://webhook.example.com/events",
    webhook_by_events=True,
    events=["message", "status"],
    reject_call=True,
    msg_call="I'm busy at the moment",
    groups_ignore=False,
    always_online=True,
    read_messages=True,
    read_status=True,

    # Websocket configuration
    websocket_enabled=True,
    websocket_events=["message", "status"],

    # Message queue configuration
    rabbitmq_enabled=True,
    rabbitmq_events=["message"],
    sqs_enabled=True,
    sqs_events=["message"],

    # Typebot integration
    typebot_url="https://typebot.example.com",
    typebot="bot1",
    typebot_expire=3600,
    typebot_keyword_finish="end",
    typebot_delay_message=500,
    typebot_unknown_message="I don't understand",
    typebot_listening_from_me=True,

    # Proxy configuration
    proxy=proxy,

    # Chatwoot integration
    chatwoot_account_id=12345,
    chatwoot_token="chatwoot-token",
    chatwoot_url="https://chatwoot.example.com",
    chatwoot_sign_msg=True,
    chatwoot_reopen_conversation=True,
    chatwoot_conversation_pending=True
)
```

### Error Handling

The library throws `EvolutionAPIError` exceptions for API errors:

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

### Schemas

#### ProxySettings

Configures proxy settings for connections:

```python
from evolutionapi.schemas import ProxySettings

# Basic proxy
proxy = ProxySettings(
    host="proxy.example.com",
    port="8080"
)

# Authenticated proxy with protocol
proxy = ProxySettings(
    host="proxy.example.com",
    port="8080",
    protocol="socks5",  # Options: http, https, socks4, socks5
    username="proxyuser",
    password="proxypass"
)
```

## Resources

- [Evolution API Documentation](https://doc.evolution-api.com)
- [GitHub Repository](https://github.com/hudsonbrendon/python-evolution-api)
