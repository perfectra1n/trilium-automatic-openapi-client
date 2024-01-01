from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.attribute import Attribute
from typing import Dict


def _get_kwargs(
    attribute_id: str,
    *,
    body: Attribute,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/attributes/{attributeId}".format(
            attributeId=attribute_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Attribute]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Attribute.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Attribute]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    attribute_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Attribute,
) -> Response[Attribute]:
    """patch a attribute identified by the attributeId with changes in the body. For labels, only value and
    position can be updated. For relations, only position can be updated. If you want to modify other
    properties, you need to delete the old attribute and create a new one.

    Args:
        attribute_id (str):  Example: evnnmvHTCgIn.
        body (Attribute): Attribute (Label, Relation) is a key-value record attached to a note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Attribute]
    """

    kwargs = _get_kwargs(
        attribute_id=attribute_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    attribute_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Attribute,
) -> Optional[Attribute]:
    """patch a attribute identified by the attributeId with changes in the body. For labels, only value and
    position can be updated. For relations, only position can be updated. If you want to modify other
    properties, you need to delete the old attribute and create a new one.

    Args:
        attribute_id (str):  Example: evnnmvHTCgIn.
        body (Attribute): Attribute (Label, Relation) is a key-value record attached to a note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Attribute
    """

    return sync_detailed(
        attribute_id=attribute_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    attribute_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Attribute,
) -> Response[Attribute]:
    """patch a attribute identified by the attributeId with changes in the body. For labels, only value and
    position can be updated. For relations, only position can be updated. If you want to modify other
    properties, you need to delete the old attribute and create a new one.

    Args:
        attribute_id (str):  Example: evnnmvHTCgIn.
        body (Attribute): Attribute (Label, Relation) is a key-value record attached to a note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Attribute]
    """

    kwargs = _get_kwargs(
        attribute_id=attribute_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    attribute_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Attribute,
) -> Optional[Attribute]:
    """patch a attribute identified by the attributeId with changes in the body. For labels, only value and
    position can be updated. For relations, only position can be updated. If you want to modify other
    properties, you need to delete the old attribute and create a new one.

    Args:
        attribute_id (str):  Example: evnnmvHTCgIn.
        body (Attribute): Attribute (Label, Relation) is a key-value record attached to a note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Attribute
    """

    return (
        await asyncio_detailed(
            attribute_id=attribute_id,
            client=client,
            body=body,
        )
    ).parsed
