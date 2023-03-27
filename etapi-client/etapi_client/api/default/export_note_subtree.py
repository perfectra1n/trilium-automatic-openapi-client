from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.export_note_subtree_format import ExportNoteSubtreeFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    note_id: str,
    *,
    client: Client,
    format_: Union[Unset, None, ExportNoteSubtreeFormat] = ExportNoteSubtreeFormat.HTML,
) -> Dict[str, Any]:
    url = "{}/notes/{noteId}/export".format(client.base_url, noteId=note_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
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
    format_: Union[Unset, None, ExportNoteSubtreeFormat] = ExportNoteSubtreeFormat.HTML,
) -> Response[Any]:
    r"""Exports ZIP file export of a given note subtree. To export whole document, use \"root\" for noteId

    Args:
        note_id (str):  Example: evnnmvHTCgIn.
        format_ (Union[Unset, None, ExportNoteSubtreeFormat]):  Default:
            ExportNoteSubtreeFormat.HTML.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
        client=client,
        format_=format_,
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
    format_: Union[Unset, None, ExportNoteSubtreeFormat] = ExportNoteSubtreeFormat.HTML,
) -> Response[Any]:
    r"""Exports ZIP file export of a given note subtree. To export whole document, use \"root\" for noteId

    Args:
        note_id (str):  Example: evnnmvHTCgIn.
        format_ (Union[Unset, None, ExportNoteSubtreeFormat]):  Default:
            ExportNoteSubtreeFormat.HTML.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
        client=client,
        format_=format_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
