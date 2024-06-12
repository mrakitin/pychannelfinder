from __future__ import annotations

import json
from pprint import pprint

from pychannelfinder import Client
from pychannelfinder.api.info_manager import info


def test_api_info():
    client = Client(base_url="https://localhost:8443", verify_ssl=False)
    print(f"{client = }")
    resp = info.sync_detailed(client=client)
    data = json.loads(resp.content)
    pprint(data)
    assert data["name"] == "ChannelFinder Service"
    assert "elastic" in data
