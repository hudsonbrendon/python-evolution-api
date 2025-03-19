from unittest.mock import MagicMock

import pytest

from evolutionapi.client import EvolutionAPI


@pytest.fixture
def mock_client() -> MagicMock:
    client = MagicMock(spec=EvolutionAPI)
    return client


@pytest.fixture
def instance_success_response():
    return {
        "instance": {
            "instanceName": "teste-docs",
            "instanceId": "af6c5b7c-ee27-4f94-9ea8-192393746ddd",
            "webhook_wa_business": None,
            "access_token_wa_business": "",
            "status": "created",
        },
        "hash": {"apikey": "123456"},
        "settings": {
            "reject_call": False,
            "msg_call": "",
            "groups_ignore": True,
            "always_online": False,
            "read_messages": False,
            "read_status": False,
            "sync_full_history": False,
        },
    }


@pytest.fixture
def instance_error_response() -> dict:
    return {
        "status": 403,
        "error": "Forbidden",
        "response": {
            "message": ['This name "instance-example-name" is already in use.']
        },
    }
