from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.export_note_subtree_format import ExportNoteSubtreeFormat
from typing import Union
from ...types import UNSET, Unset


def _get_kwargs(
    note_id: str,
    *,
    format_: Union[Unset, ExportNoteSubtreeFormat] = ExportNoteSubtreeFormat.HTML,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/notes/{noteId}/export".format(
            noteId=note_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
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
    format_: Union[Unset, ExportNoteSubtreeFormat] = ExportNoteSubtreeFormat.HTML,
) -> Response[Any]:
    r"""Exports ZIP file export of a given note subtree. To export whole document, use \"root\" for noteId

    Args:
        note_id (str):  Example: evnnmvHTCgIn.
        format_ (Union[Unset, ExportNoteSubtreeFormat]):  Default: ExportNoteSubtreeFormat.HTML.

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
    format_: Union[Unset, ExportNoteSubtreeFormat] = ExportNoteSubtreeFormat.HTML,
) -> Response[Any]:
    r"""Exports ZIP file export of a given note subtree. To export whole document, use \"root\" for noteId

    Args:
        note_id (str):  Example: evnnmvHTCgIn.
        format_ (Union[Unset, ExportNoteSubtreeFormat]):  Default: ExportNoteSubtreeFormat.HTML.

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
