from typing import Any, Dict

import requests

from evolutionapi.exceptions import EvolutionAPIError
from evolutionapi.resources.instances import Instance


class EvolutionAPI:
    """Client for Evolution API."""

    def __init__(self, base_url: str, api_key: str) -> None:
        """
        Initialize the Evolution API client.

        Args:
            base_url: Base URL for the Evolution API
            api_key: API key for authentication
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update(
            {"Content-Type": "application/json", "apikey": api_key}
        )

        # Register resources
        self.instances = Instance(self)

    def _request(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"

        response = self.session.request(method, url, **kwargs)

        if response.status_code >= 400:
            error_message = "Unknown error"
            error_response = None

            try:
                error_data = response.json()
                error_message = error_data.get("error", "Unknown error")
                error_response = error_data
            except Exception:
                error_message = "Failed to parse error response"
                error_response = None

            raise EvolutionAPIError(
                status_code=response.status_code,
                error_message=error_message,
                response=error_response,
            )

        return response.json()

    def _get(self, path: str, **kwargs) -> Dict[str, Any]:
        return self._request("GET", path, **kwargs)

    def _post(self, path: str, **kwargs) -> Dict[str, Any]:
        return self._request("POST", path, **kwargs)

    def _put(self, path: str, **kwargs) -> Dict[str, Any]:
        return self._request("PUT", path, **kwargs)

    def _delete(self, path: str, **kwargs) -> Dict[str, Any]:
        return self._request("DELETE", path, **kwargs)
