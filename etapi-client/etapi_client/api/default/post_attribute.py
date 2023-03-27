from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.attribute import Attribute
from ...types import Response


def _get_kwargs(
    attribute_id: str,
    *,
    client: Client,
    json_body: Attribute,
) -> Dict[str, Any]:
    url = "{}/attributes/{attributeId}".format(client.base_url, attributeId=attribute_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Attribute]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Attribute.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Attribute]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    attribute_id: str,
    *,
    client: Client,
    json_body: Attribute,
) -> Response[Attribute]:
    """create an attribute for a given note

    Args:
        attribute_id (str):  Example: evnnmvHTCgIn.
        json_body (Attribute): Attribute (Label, Relation) is a key-value record attached to a
            note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Attribute]
    """

    kwargs = _get_kwargs(
        attribute_id=attribute_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    attribute_id: str,
    *,
    client: Client,
    json_body: Attribute,
) -> Optional[Attribute]:
    """create an attribute for a given note

    Args:
        attribute_id (str):  Example: evnnmvHTCgIn.
        json_body (Attribute): Attribute (Label, Relation) is a key-value record attached to a
            note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Attribute]
    """

    return sync_detailed(
        attribute_id=attribute_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    attribute_id: str,
    *,
    client: Client,
    json_body: Attribute,
) -> Response[Attribute]:
    """create an attribute for a given note

    Args:
        attribute_id (str):  Example: evnnmvHTCgIn.
        json_body (Attribute): Attribute (Label, Relation) is a key-value record attached to a
            note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Attribute]
    """

    kwargs = _get_kwargs(
        attribute_id=attribute_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    attribute_id: str,
    *,
    client: Client,
    json_body: Attribute,
) -> Optional[Attribute]:
    """create an attribute for a given note

    Args:
        attribute_id (str):  Example: evnnmvHTCgIn.
        json_body (Attribute): Attribute (Label, Relation) is a key-value record attached to a
            note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Attribute]
    """

    return (
        await asyncio_detailed(
            attribute_id=attribute_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
