from typing import Any, Dict, Optional


class EvolutionAPIError(Exception):
    """Error raised by the Evolution API client."""

    def __init__(
        self,
        status_code: int,
        error_message: str,
        response: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Initialize the error.

        Args:
            status_code: The HTTP status code
            error_message: The error message
            response: The full response from the server
        """
        self.status_code = status_code
        self.error_message = error_message
        self.response = response

        super().__init__(f"HTTP {status_code}: {error_message}")
