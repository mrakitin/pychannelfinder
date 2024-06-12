from __future__ import annotations

import pytest

from pychannelfinder import Client


@pytest.fixture()
def client():
    c = Client(base_url="https://localhost:8443", verify_ssl=False)

    yield c

    c.get_httpx_client().close()
