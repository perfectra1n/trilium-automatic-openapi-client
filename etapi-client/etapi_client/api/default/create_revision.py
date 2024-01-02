from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_revision_format import CreateRevisionFormat
from ...types import UNSET, Unset
from typing import Union


def _get_kwargs(
    note_id: str,
    *,
    format_: Union[Unset, CreateRevisionFormat] = CreateRevisionFormat.HTML,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/notes/{noteId}/revision".format(
            noteId=note_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    format_: Union[Unset, CreateRevisionFormat] = CreateRevisionFormat.HTML,
) -> Response[Any]:
    """Create a note revision for the given note

    Args:
        note_id (str):  Example: evnnmvHTCgIn.
        format_ (Union[Unset, CreateRevisionFormat]):  Default: CreateRevisionFormat.HTML.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    format_: Union[Unset, CreateRevisionFormat] = CreateRevisionFormat.HTML,
) -> Response[Any]:
    """Create a note revision for the given note

    Args:
        note_id (str):  Example: evnnmvHTCgIn.
        format_ (Union[Unset, CreateRevisionFormat]):  Default: CreateRevisionFormat.HTML.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
