from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.multi_value_map_string_string import MultiValueMapStringString
from ...types import UNSET, Response


def _get_kwargs(
    scroll_id: str,
    *,
    search_parameters: "MultiValueMapStringString",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_search_parameters = search_parameters.to_dict()
    params.update(json_search_parameters)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/ChannelFinder/resources/scroll/{scroll_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scroll_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    search_parameters: "MultiValueMapStringString",
) -> Response[Any]:
    """
    Args:
        scroll_id (str):
        search_parameters (MultiValueMapStringString):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        scroll_id=scroll_id,
        search_parameters=search_parameters,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    scroll_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    search_parameters: "MultiValueMapStringString",
) -> Response[Any]:
    """
    Args:
        scroll_id (str):
        search_parameters (MultiValueMapStringString):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        scroll_id=scroll_id,
        search_parameters=search_parameters,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
