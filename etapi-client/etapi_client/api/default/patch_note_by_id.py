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
    json_body: Note,
) -> Dict[str, Any]:
    url = "{}/notes/{noteId}".format(client.base_url, noteId=note_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
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
    json_body: Note,
) -> Response[Any]:
    """patch a note identified by the noteId with changes in the body

    Args:
        note_id (str):  Example: evnnmvHTCgIn.
        json_body (Note):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    note_id: str,
    *,
    client: Client,
    json_body: Note,
) -> Response[Any]:
    """patch a note identified by the noteId with changes in the body

    Args:
        note_id (str):  Example: evnnmvHTCgIn.
        json_body (Note):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
