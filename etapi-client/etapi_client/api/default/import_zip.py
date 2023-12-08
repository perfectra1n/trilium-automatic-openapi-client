from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.note_with_branch import NoteWithBranch
from typing import Dict


def _get_kwargs(
    note_id: str,
) -> Dict[str, Any]:
    return {
        "method": "post",
        "url": "/notes/{noteId}/import".format(
            noteId=note_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[NoteWithBranch]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = NoteWithBranch.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[NoteWithBranch]:
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
) -> Response[NoteWithBranch]:
    """Imports ZIP file into a given note.

    Args:
        note_id (str):  Example: evnnmvHTCgIn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NoteWithBranch]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[NoteWithBranch]:
    """Imports ZIP file into a given note.

    Args:
        note_id (str):  Example: evnnmvHTCgIn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NoteWithBranch
    """

    return sync_detailed(
        note_id=note_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[NoteWithBranch]:
    """Imports ZIP file into a given note.

    Args:
        note_id (str):  Example: evnnmvHTCgIn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NoteWithBranch]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[NoteWithBranch]:
    """Imports ZIP file into a given note.

    Args:
        note_id (str):  Example: evnnmvHTCgIn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NoteWithBranch
    """

    return (
        await asyncio_detailed(
            note_id=note_id,
            client=client,
        )
    ).parsed
