from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_response import SearchResponse
from typing import Dict
from ...types import UNSET, Unset
from ...models.search_notes_order_direction import SearchNotesOrderDirection
from typing import Union


def _get_kwargs(
    *,
    search: str,
    fast_search: Union[Unset, bool] = False,
    include_archived_notes: Union[Unset, bool] = False,
    ancestor_note_id: Union[Unset, str] = UNSET,
    ancestor_depth: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    order_direction: Union[
        Unset, SearchNotesOrderDirection
    ] = SearchNotesOrderDirection.ASC,
    limit: Union[Unset, int] = UNSET,
    debug: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["search"] = search

    params["fastSearch"] = fast_search

    params["includeArchivedNotes"] = include_archived_notes

    params["ancestorNoteId"] = ancestor_note_id

    params["ancestorDepth"] = ancestor_depth

    params["orderBy"] = order_by

    json_order_direction: Union[Unset, str] = UNSET
    if not isinstance(order_direction, Unset):
        json_order_direction = order_direction.value

    params["orderDirection"] = json_order_direction

    params["limit"] = limit

    params["debug"] = debug

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/notes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SearchResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SearchResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    search: str,
    fast_search: Union[Unset, bool] = False,
    include_archived_notes: Union[Unset, bool] = False,
    ancestor_note_id: Union[Unset, str] = UNSET,
    ancestor_depth: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    order_direction: Union[
        Unset, SearchNotesOrderDirection
    ] = SearchNotesOrderDirection.ASC,
    limit: Union[Unset, int] = UNSET,
    debug: Union[Unset, bool] = False,
) -> Response[SearchResponse]:
    """Search notes

    Args:
        search (str):
        fast_search (Union[Unset, bool]):  Default: False.
        include_archived_notes (Union[Unset, bool]):  Default: False.
        ancestor_note_id (Union[Unset, str]):  Example: evnnmvHTCgIn.
        ancestor_depth (Union[Unset, str]):
        order_by (Union[Unset, str]):
        order_direction (Union[Unset, SearchNotesOrderDirection]):  Default:
            SearchNotesOrderDirection.ASC.
        limit (Union[Unset, int]):
        debug (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponse]
    """

    kwargs = _get_kwargs(
        search=search,
        fast_search=fast_search,
        include_archived_notes=include_archived_notes,
        ancestor_note_id=ancestor_note_id,
        ancestor_depth=ancestor_depth,
        order_by=order_by,
        order_direction=order_direction,
        limit=limit,
        debug=debug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    search: str,
    fast_search: Union[Unset, bool] = False,
    include_archived_notes: Union[Unset, bool] = False,
    ancestor_note_id: Union[Unset, str] = UNSET,
    ancestor_depth: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    order_direction: Union[
        Unset, SearchNotesOrderDirection
    ] = SearchNotesOrderDirection.ASC,
    limit: Union[Unset, int] = UNSET,
    debug: Union[Unset, bool] = False,
) -> Optional[SearchResponse]:
    """Search notes

    Args:
        search (str):
        fast_search (Union[Unset, bool]):  Default: False.
        include_archived_notes (Union[Unset, bool]):  Default: False.
        ancestor_note_id (Union[Unset, str]):  Example: evnnmvHTCgIn.
        ancestor_depth (Union[Unset, str]):
        order_by (Union[Unset, str]):
        order_direction (Union[Unset, SearchNotesOrderDirection]):  Default:
            SearchNotesOrderDirection.ASC.
        limit (Union[Unset, int]):
        debug (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResponse
    """

    return sync_detailed(
        client=client,
        search=search,
        fast_search=fast_search,
        include_archived_notes=include_archived_notes,
        ancestor_note_id=ancestor_note_id,
        ancestor_depth=ancestor_depth,
        order_by=order_by,
        order_direction=order_direction,
        limit=limit,
        debug=debug,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    search: str,
    fast_search: Union[Unset, bool] = False,
    include_archived_notes: Union[Unset, bool] = False,
    ancestor_note_id: Union[Unset, str] = UNSET,
    ancestor_depth: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    order_direction: Union[
        Unset, SearchNotesOrderDirection
    ] = SearchNotesOrderDirection.ASC,
    limit: Union[Unset, int] = UNSET,
    debug: Union[Unset, bool] = False,
) -> Response[SearchResponse]:
    """Search notes

    Args:
        search (str):
        fast_search (Union[Unset, bool]):  Default: False.
        include_archived_notes (Union[Unset, bool]):  Default: False.
        ancestor_note_id (Union[Unset, str]):  Example: evnnmvHTCgIn.
        ancestor_depth (Union[Unset, str]):
        order_by (Union[Unset, str]):
        order_direction (Union[Unset, SearchNotesOrderDirection]):  Default:
            SearchNotesOrderDirection.ASC.
        limit (Union[Unset, int]):
        debug (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponse]
    """

    kwargs = _get_kwargs(
        search=search,
        fast_search=fast_search,
        include_archived_notes=include_archived_notes,
        ancestor_note_id=ancestor_note_id,
        ancestor_depth=ancestor_depth,
        order_by=order_by,
        order_direction=order_direction,
        limit=limit,
        debug=debug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    search: str,
    fast_search: Union[Unset, bool] = False,
    include_archived_notes: Union[Unset, bool] = False,
    ancestor_note_id: Union[Unset, str] = UNSET,
    ancestor_depth: Union[Unset, str] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    order_direction: Union[
        Unset, SearchNotesOrderDirection
    ] = SearchNotesOrderDirection.ASC,
    limit: Union[Unset, int] = UNSET,
    debug: Union[Unset, bool] = False,
) -> Optional[SearchResponse]:
    """Search notes

    Args:
        search (str):
        fast_search (Union[Unset, bool]):  Default: False.
        include_archived_notes (Union[Unset, bool]):  Default: False.
        ancestor_note_id (Union[Unset, str]):  Example: evnnmvHTCgIn.
        ancestor_depth (Union[Unset, str]):
        order_by (Union[Unset, str]):
        order_direction (Union[Unset, SearchNotesOrderDirection]):  Default:
            SearchNotesOrderDirection.ASC.
        limit (Union[Unset, int]):
        debug (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            search=search,
            fast_search=fast_search,
            include_archived_notes=include_archived_notes,
            ancestor_note_id=ancestor_note_id,
            ancestor_depth=ancestor_depth,
            order_by=order_by,
            order_direction=order_direction,
            limit=limit,
            debug=debug,
        )
    ).parsed
