from typing import Any, Dict, List, Optional

from evolutionapi.schemas import ProxySettings


class Instance:
    """Resource for managing WhatsApp instances."""

    def __init__(self, client) -> None:
        """
        Initialize the instance resource.

        Args:
            client: Evolution API client
        """
        self.client = client

    def create(
        self,
        instance_name: str,
        token: Optional[str] = None,
        qrcode: bool = True,
        number: Optional[str] = None,
        integration: str = "WHATSAPP-BAILEYS",
        webhook: Optional[str] = None,
        webhook_by_events: bool = False,
        events: Optional[List[str]] = None,
        reject_call: bool = False,
        msg_call: Optional[str] = None,
        groups_ignore: bool = True,
        always_online: bool = False,
        read_messages: bool = False,
        read_status: bool = False,
        websocket_enabled: bool = False,
        websocket_events: Optional[List[str]] = None,
        rabbitmq_enabled: bool = False,
        rabbitmq_events: Optional[List[str]] = None,
        sqs_enabled: bool = False,
        sqs_events: Optional[List[str]] = None,
        typebot_url: Optional[str] = None,
        typebot: Optional[str] = None,
        typebot_expire: Optional[int] = None,
        typebot_keyword_finish: Optional[str] = None,
        typebot_delay_message: Optional[int] = None,
        typebot_unknown_message: Optional[str] = None,
        typebot_listening_from_me: bool = False,
        proxy: Optional[ProxySettings] = None,
        chatwoot_account_id: Optional[int] = None,
        chatwoot_token: Optional[str] = None,
        chatwoot_url: Optional[str] = None,
        chatwoot_sign_msg: bool = False,
        chatwoot_reopen_conversation: bool = False,
        chatwoot_conversation_pending: bool = False,
    ) -> Dict[str, Any]:
        """
        Create a new WhatsApp instance, for more information check the API documentation:

        https://doc.evolution-api.com/v1/api-reference/instance-controller/create-instance-basic

        Args:
            instance_name: The name of the instance to create
            token: Authentication token for the instance
            qrcode: Whether to enable QR code authentication
            number: Phone number associated with the instance
            integration: Type of integration. Default is "WHATSAPP-BAILEYS"
            webhook: Webhook URL for receiving events
            webhook_by_events: Whether to send events through webhook
            events: List of events to listen for
            reject_call: Whether to reject incoming calls
            msg_call: Message to send when rejecting calls
            groups_ignore: Whether to ignore group messages
            always_online: Whether to keep the instance always online
            read_messages: Whether to mark messages as read automatically
            read_status: Whether to read status updates
            websocket_enabled: Whether to enable websocket connection
            websocket_events: List of events to send through websocket
            rabbitmq_enabled: Whether to enable RabbitMQ integration
            rabbitmq_events: List of events to send through RabbitMQ
            sqs_enabled: Whether to enable AWS SQS integration
            sqs_events: List of events to send through SQS
            typebot_url: URL for Typebot integration
            typebot: Typebot configuration
            typebot_expire: Typebot expiration time in seconds
            typebot_keyword_finish: Keyword to finish Typebot conversation
            typebot_delay_message: Delay between Typebot messages in ms
            typebot_unknown_message: Message to send for unknown commands
            typebot_listening_from_me: Whether to process messages from me
            proxy: Proxy configuration dictionary
            chatwoot_account_id: Chatwoot account ID
            chatwoot_token: Chatwoot token
            chatwoot_url: Chatwoot URL
            chatwoot_sign_msg: Whether to sign Chatwoot messages
            chatwoot_reopen_conversation: Whether to reopen Chatwoot conversations
            chatwoot_conversation_pending: Whether to mark Chatwoot conversations as pending

        Returns:
            Dictionary containing instance information.

        Raises:
            EvolutionAPIError: If the API returns an error
        """
        data = {
            "instanceName": instance_name,
            "token": token,
            "qrcode": qrcode,
            "number": number,
            "integration": integration,
            "webhook": webhook,
            "webhook_by_events": webhook_by_events,
            "events": events or [],
            "reject_call": reject_call,
            "msg_call": msg_call,
            "groups_ignore": groups_ignore,
            "always_online": always_online,
            "read_messages": read_messages,
            "read_status": read_status,
            "websocket_enabled": websocket_enabled,
            "websocket_events": websocket_events or [],
            "rabbitmq_enabled": rabbitmq_enabled,
            "rabbitmq_events": rabbitmq_events or [],
            "sqs_enabled": sqs_enabled,
            "sqs_events": sqs_events or [],
            "typebot_url": typebot_url,
            "typebot": typebot,
            "typebot_expire": typebot_expire,
            "typebot_keyword_finish": typebot_keyword_finish,
            "typebot_delay_message": typebot_delay_message,
            "typebot_unknown_message": typebot_unknown_message,
            "typebot_listening_from_me": typebot_listening_from_me,
            "chatwoot_account_id": chatwoot_account_id,
            "chatwoot_token": chatwoot_token,
            "chatwoot_url": chatwoot_url,
            "chatwoot_sign_msg": chatwoot_sign_msg,
            "chatwoot_reopen_conversation": chatwoot_reopen_conversation,
            "chatwoot_conversation_pending": chatwoot_conversation_pending,
        }

        if proxy:
            data["proxy"] = proxy

        clean_data = {k: v for k, v in data.items() if v is not None}

        return self.client._post("/instance/create", json=clean_data)
