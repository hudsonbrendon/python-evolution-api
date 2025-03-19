from typing import Any, Dict

import requests


class EvolutionAPI:
    """Client for the Evolution API.

    This class provides methods to interact with the Evolution API.
    """

    def __init__(self, base_url: str) -> None:
        """Initialize the Evolution API client.

        Args:
            base_url: The base URL of the Evolution API server.
        """
        self.__base_url = base_url.rstrip("/")

    @property
    def base_url(self) -> str:
        """Get the base URL of the Evolution API server."""
        return self.__base_url

    def get_server_info(self) -> Dict[str, Any]:
        """Get server information from the Evolution API.

        Returns:
            A dictionary containing server information including status,
            message, version, and links to documentation.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        response = requests.get(f"{self.base_url}/")
        response.raise_for_status()
        return response.json()
