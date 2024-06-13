from __future__ import annotations

import json

import pandas as pd

from pychannelfinder.api.channel_manager import query_2
from pychannelfinder.models.multi_value_map_string_string_all import (
    MultiValueMapStringStringAll,
)


def find_my_field(df, field_name):
    return df.loc[df.name.str.contains(field_name)]


def test_api_query_2(client):
    mvmssa = MultiValueMapStringStringAll.from_dict({"~name": "SR*"})
    resp = query_2.sync_detailed(client=client, all_request_params=mvmssa)
    data = json.loads(resp.content)

    df_channels = pd.DataFrame(data=data)
    filtered = find_my_field(df_channels, "SR:C001-BI")

    filtered_first = filtered.loc[1]

    assert filtered_first["name"] == "SR:C001-BI:1{BHS}Pos:X-RB"

    df_properties = pd.DataFrame(data=filtered_first["properties"])
    assert df_properties.shape == (39, 4)
    assert find_my_field(df_properties, "family|prop2").shape == (11, 4)
