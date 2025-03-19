from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ProxyProtocol(str, Enum):
    """Valid protocols for proxy connection."""

    HTTP = "http"
    HTTPS = "https"
    SOCKS4 = "socks4"
    SOCKS5 = "socks5"


class ProxySettings(BaseModel):
    """Pydantic model for proxy configuration validation."""

    host: str = Field(description="Proxy server hostname or IP address")
    port: str = Field(description="Proxy server port")
    protocol: ProxyProtocol = Field(
        default=ProxyProtocol.HTTP, description="Proxy protocol"
    )
    username: Optional[str] = Field(
        None, description="Username for proxy authentication"
    )
    password: Optional[str] = Field(
        None, description="Password for proxy authentication"
    )

    class Config:
        use_enum_values = True
