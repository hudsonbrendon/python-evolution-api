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
from python_evolution_api import EvolutionAPI

# Initialize the client
client = EvolutionAPI("https://your-evolution-api-server.com")

# Get server information
info = client.get_server_info()
print(f"Server status: {info['status']}")
print(f"Server version: {info['version']}")
print(f"Documentation URL: {info['documentation']}")
```

## Available Features

- Server Information: Get details about the Evolution API server

## Coming Soon

- Instance management
- Message sending capabilities
- Media handling
- Group operations
- Contact management

## Resources

- [Evolution API Documentation](https://doc.evolution-api.com)
- [GitHub Repository](https://github.com/hudsonbrendon/python-evolution-api)
