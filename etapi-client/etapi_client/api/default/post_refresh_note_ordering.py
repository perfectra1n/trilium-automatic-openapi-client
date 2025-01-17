from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    parent_note_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/refresh-note-ordering/{parent_note_id}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 204:
        return None
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
    parent_note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    r"""notePositions in branches are not automatically pushed to connected clients and need a specific
    instruction.  If you want your changes to be in effect immediately, call this service after setting
    branches' notePosition.  Note that you need to supply \"parentNoteId\" of branch(es) with changed
    positions.

    Args:
        parent_note_id (str):  Example: evnnmvHTCgIn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        parent_note_id=parent_note_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    parent_note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    r"""notePositions in branches are not automatically pushed to connected clients and need a specific
    instruction.  If you want your changes to be in effect immediately, call this service after setting
    branches' notePosition.  Note that you need to supply \"parentNoteId\" of branch(es) with changed
    positions.

    Args:
        parent_note_id (str):  Example: evnnmvHTCgIn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        parent_note_id=parent_note_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
