"""A client library for accessing OpenAPI definition"""

from __future__ import annotations

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
