import json
from unittest.mock import Mock, patch

import pytest

from evolutionapi.client import EvolutionAPI
from evolutionapi.exceptions import EvolutionAPIError


class TestEvolutionAPI:
    @pytest.fixture
    def mock_session(self):
        with patch("evolutionapi.client.requests.Session") as mock_session:
            session_instance = Mock()
            mock_session.return_value = session_instance
            yield session_instance

    @pytest.fixture
    def api_client(self, mock_session):
        client = EvolutionAPI("https://api.example.com", "test-api-key")
        return client

    def test_initialization(self, api_client, mock_session):
        """Test if the client is initialized correctly."""
        assert api_client.base_url == "https://api.example.com"
        assert api_client.api_key == "test-api-key"
        mock_session.headers.update.assert_called_once_with(
            {"Content-Type": "application/json", "apikey": "test-api-key"}
        )

    def test_url_trailing_slash_removal(self):
        """Test if trailing slash is removed from base_url."""
        client = EvolutionAPI("https://api.example.com/", "test-api-key")
        assert client.base_url == "https://api.example.com"

    def test_get_request(self, api_client, mock_session):
        """Test GET request method."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test_data"}
        mock_session.request.return_value = mock_response

        result = api_client._get("/test-path", params={"key": "value"})

        mock_session.request.assert_called_once_with(
            "GET", "https://api.example.com/test-path", params={"key": "value"}
        )
        assert result == {"data": "test_data"}

    def test_post_request(self, api_client, mock_session):
        """Test POST request method."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "created"}
        mock_session.request.return_value = mock_response

        data = {"name": "test"}
        result = api_client._post("/test-path", json=data)

        mock_session.request.assert_called_once_with(
            "POST", "https://api.example.com/test-path", json=data
        )
        assert result == {"data": "created"}

    def test_put_request(self, api_client, mock_session):
        """Test PUT request method."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "updated"}
        mock_session.request.return_value = mock_response

        data = {"name": "updated"}
        result = api_client._put("/test-path", json=data)

        mock_session.request.assert_called_once_with(
            "PUT", "https://api.example.com/test-path", json=data
        )
        assert result == {"data": "updated"}

    def test_delete_request(self, api_client, mock_session):
        """Test DELETE request method."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "deleted"}
        mock_session.request.return_value = mock_response

        result = api_client._delete("/test-path")

        mock_session.request.assert_called_once_with(
            "DELETE", "https://api.example.com/test-path"
        )
        assert result == {"data": "deleted"}

    def test_error_handling(self, api_client, mock_session):
        """Test error handling in requests."""
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"error": "Bad request"}
        mock_session.request.return_value = mock_response

        with pytest.raises(EvolutionAPIError) as excinfo:
            api_client._get("/test-path")

        assert excinfo.value.status_code == 400
        assert excinfo.value.error_message == "Bad request"
        assert excinfo.value.response == {"error": "Bad request"}

    def test_error_handling_parse_error(self, api_client, mock_session):
        """Test error handling when response cannot be parsed as JSON."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.side_effect = json.JSONDecodeError("Invalid JSON", "", 0)
        mock_session.request.return_value = mock_response

        with pytest.raises(EvolutionAPIError) as excinfo:
            api_client._get("/test-path")

        assert excinfo.value.status_code == 500
        assert excinfo.value.error_message == "Failed to parse error response"
        assert excinfo.value.response is None
