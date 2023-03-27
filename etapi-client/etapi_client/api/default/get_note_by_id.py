from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.note import Note
from ...types import Response


def _get_kwargs(
    note_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/notes/{noteId}".format(client.base_url, noteId=note_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Note]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Note.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Note]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    note_id: str,
    *,
    client: Client,
) -> Response[Note]:
    """Returns a note identified by its ID

    Args:
        note_id (str):  Example: evnnmvHTCgIn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Note]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    note_id: str,
    *,
    client: Client,
) -> Optional[Note]:
    """Returns a note identified by its ID

    Args:
        note_id (str):  Example: evnnmvHTCgIn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Note]
    """

    return sync_detailed(
        note_id=note_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    note_id: str,
    *,
    client: Client,
) -> Response[Note]:
    """Returns a note identified by its ID

    Args:
        note_id (str):  Example: evnnmvHTCgIn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Note]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    note_id: str,
    *,
    client: Client,
) -> Optional[Note]:
    """Returns a note identified by its ID

    Args:
        note_id (str):  Example: evnnmvHTCgIn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Note]
    """

    return (
        await asyncio_detailed(
            note_id=note_id,
            client=client,
        )
    ).parsed
