import pytest
import requests

from python_evolution_api import EvolutionAPI


class TestEvolutionAPI:
    def test_get_server_info(self, requests_mock, server_info: dict) -> None:
        base_url = "https://api.example.com"
        requests_mock.get(f"{base_url}/", json=server_info)

        client = EvolutionAPI(base_url)
        result = client.get_server_info()

        assert result == server_info
        assert result["status"] == 200
        assert "Welcome to the Evolution API" in result["message"]
        assert "version" in result
        assert "documentation" in result

    def test_get_server_info_error(self, requests_mock) -> None:
        base_url = "https://api.example.com"
        requests_mock.get(f"{base_url}/", status_code=500)

        client = EvolutionAPI(base_url)

        with pytest.raises(requests.HTTPError):
            client.get_server_info()
