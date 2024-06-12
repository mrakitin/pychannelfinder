"""A client library for accessing OpenAPI definition"""

from __future__ import annotations

from ._version import version as __version__
from .client import AuthenticatedClient, Client

__all__ = ("AuthenticatedClient", "Client", "__version__")
