import pytest

from evolutionapi.exceptions import EvolutionAPIError
from evolutionapi.resources.instances import Instance
from evolutionapi.schemas import ProxySettings


class TestInstance:
    def test_create_instance_minimal(
        self, mock_client, instance_success_response
    ) -> None:
        mock_client._post.return_value = instance_success_response
        instance = Instance(mock_client)

        result = instance.create(instance_name="teste-docs")

        mock_client._post.assert_called_once()
        assert result == instance_success_response

    def test_create_instance_with_token(
        self, mock_client, instance_success_response
    ) -> None:
        mock_client._post.return_value = instance_success_response
        instance = Instance(mock_client)

        result = instance.create(instance_name="teste-docs", token="my-custom-token")

        mock_client._post.assert_called_once()
        expected_data = {
            "instanceName": "teste-docs",
            "token": "my-custom-token",
            "qrcode": True,
            "integration": "WHATSAPP-BAILEYS",
            "webhook_by_events": False,
            "events": [],
            "reject_call": False,
            "groups_ignore": True,
            "always_online": False,
            "read_messages": False,
            "read_status": False,
            "websocket_enabled": False,
            "websocket_events": [],
            "rabbitmq_enabled": False,
            "rabbitmq_events": [],
            "sqs_enabled": False,
            "sqs_events": [],
            "typebot_listening_from_me": False,
            "chatwoot_sign_msg": False,
            "chatwoot_reopen_conversation": False,
            "chatwoot_conversation_pending": False,
        }
        mock_client._post.assert_called_with("/instance/create", json=expected_data)
        assert result == instance_success_response

    def test_create_instance_with_all_params(
        self, mock_client, instance_success_response
    ) -> None:
        mock_client._post.return_value = instance_success_response
        instance = Instance(mock_client)
        proxy = ProxySettings(
            host="127.0.0.1", port="8080", username="user", password="pass"
        )

        result = instance.create(
            instance_name="teste-docs",
            token="my-token",
            qrcode=False,
            number="1234567890",
            integration="CUSTOM-INTEGRATION",
            webhook="https://webhook.example.com",
            webhook_by_events=True,
            events=["message", "status"],
            reject_call=True,
            msg_call="I'm busy",
            groups_ignore=False,
            always_online=True,
            read_messages=True,
            read_status=True,
            websocket_enabled=True,
            websocket_events=["message", "status"],
            rabbitmq_enabled=True,
            rabbitmq_events=["message"],
            sqs_enabled=True,
            sqs_events=["message"],
            typebot_url="https://typebot.example.com",
            typebot="bot1",
            typebot_expire=3600,
            typebot_keyword_finish="end",
            typebot_delay_message=500,
            typebot_unknown_message="I don't understand",
            typebot_listening_from_me=True,
            proxy=proxy,
            chatwoot_account_id=12345,
            chatwoot_token="chatwoot-token",
            chatwoot_url="https://chatwoot.example.com",
            chatwoot_sign_msg=True,
            chatwoot_reopen_conversation=True,
            chatwoot_conversation_pending=True,
        )

        mock_client._post.assert_called_once()
        assert result == instance_success_response

    def test_create_instance_error(
        self, mock_client, instance_error_response: dict
    ) -> None:
        mock_client._post.side_effect = EvolutionAPIError(
            status_code=403, error_message="Forbidden", response=instance_error_response
        )

        instance = Instance(mock_client)

        with pytest.raises(EvolutionAPIError) as excinfo:
            instance.create(instance_name="instance-example-name")

        assert excinfo.value.status_code == 403
        assert "already in use" in str(excinfo.value.response["response"]["message"][0])

    def test_create_instance_with_none_params(
        self, mock_client, instance_success_response
    ) -> None:
        mock_client._post.return_value = instance_success_response
        instance = Instance(mock_client)

        result = instance.create(
            instance_name="teste-docs", token=None, webhook=None, msg_call=None
        )

        mock_client._post.assert_called_once()
        assert result == instance_success_response

    def test_create_instance_with_empty_events(
        self, mock_client, instance_success_response
    ) -> None:
        mock_client._post.return_value = instance_success_response
        instance = Instance(mock_client)

        result = instance.create(
            instance_name="teste-docs",
            events=[],
            websocket_events=[],
            rabbitmq_events=[],
            sqs_events=[],
        )

        mock_client._post.assert_called_once()
        assert result == instance_success_response

    def test_create_instance_network_error(self, mock_client) -> None:
        mock_client._post.side_effect = Exception("Network error")
        instance = Instance(mock_client)

        with pytest.raises(Exception) as excinfo:
            instance.create(instance_name="teste-docs")

        assert "Network error" in str(excinfo.value)

    def test_create_instance_with_proxy(
        self, mock_client, instance_success_response
    ) -> None:
        mock_client._post.return_value = instance_success_response
        instance = Instance(mock_client)
        proxy = ProxySettings(host="proxy.example.com", port="3128")

        result = instance.create(instance_name="teste-docs", proxy=proxy)

        mock_client._post.assert_called_once()
        assert result == instance_success_response

        called_args = mock_client._post.call_args[1]["json"]
        assert "proxy" in called_args
        assert called_args["proxy"] == proxy
