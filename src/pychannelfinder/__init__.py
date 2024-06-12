"""A client library for accessing OpenAPI definition"""

from __future__ import annotations

from .client import AuthenticatedClient, Client
from ._version import version as __version__

__all__ = (
    "AuthenticatedClient",
    "Client",
    "__version__"
)
