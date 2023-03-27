from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.search_notes_order_direction import SearchNotesOrderDirection
from ...models.search_response import SearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    search: str,
    fast_search: Union[Unset, None, bool] = False,
    include_archived_notes: Union[Unset, None, bool] = False,
    ancestor_note_id: Union[Unset, None, str] = UNSET,
    ancestor_depth: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
    order_direction: Union[Unset, None, SearchNotesOrderDirection] = SearchNotesOrderDirection.ASC,
    limit: Union[Unset, None, int] = UNSET,
    debug: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/notes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["search"] = search

    params["fastSearch"] = fast_search

    params["includeArchivedNotes"] = include_archived_notes

    params["ancestorNoteId"] = ancestor_note_id

    params["ancestorDepth"] = ancestor_depth

    params["orderBy"] = order_by

    json_order_direction: Union[Unset, None, str] = UNSET
    if not isinstance(order_direction, Unset):
        json_order_direction = order_direction.value if order_direction else None

    params["orderDirection"] = json_order_direction

    params["limit"] = limit

    params["debug"] = debug

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[SearchResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SearchResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[SearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    search: str,
    fast_search: Union[Unset, None, bool] = False,
    include_archived_notes: Union[Unset, None, bool] = False,
    ancestor_note_id: Union[Unset, None, str] = UNSET,
    ancestor_depth: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
    order_direction: Union[Unset, None, SearchNotesOrderDirection] = SearchNotesOrderDirection.ASC,
    limit: Union[Unset, None, int] = UNSET,
    debug: Union[Unset, None, bool] = False,
) -> Response[SearchResponse]:
    """Search notes

    Args:
        search (str):
        fast_search (Union[Unset, None, bool]):
        include_archived_notes (Union[Unset, None, bool]):
        ancestor_note_id (Union[Unset, None, str]):  Example: evnnmvHTCgIn.
        ancestor_depth (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):
        order_direction (Union[Unset, None, SearchNotesOrderDirection]):  Default:
            SearchNotesOrderDirection.ASC.
        limit (Union[Unset, None, int]):
        debug (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponse]
    """

    kwargs = _get_kwargs(
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

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    search: str,
    fast_search: Union[Unset, None, bool] = False,
    include_archived_notes: Union[Unset, None, bool] = False,
    ancestor_note_id: Union[Unset, None, str] = UNSET,
    ancestor_depth: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
    order_direction: Union[Unset, None, SearchNotesOrderDirection] = SearchNotesOrderDirection.ASC,
    limit: Union[Unset, None, int] = UNSET,
    debug: Union[Unset, None, bool] = False,
) -> Optional[SearchResponse]:
    """Search notes

    Args:
        search (str):
        fast_search (Union[Unset, None, bool]):
        include_archived_notes (Union[Unset, None, bool]):
        ancestor_note_id (Union[Unset, None, str]):  Example: evnnmvHTCgIn.
        ancestor_depth (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):
        order_direction (Union[Unset, None, SearchNotesOrderDirection]):  Default:
            SearchNotesOrderDirection.ASC.
        limit (Union[Unset, None, int]):
        debug (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponse]
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
    client: Client,
    search: str,
    fast_search: Union[Unset, None, bool] = False,
    include_archived_notes: Union[Unset, None, bool] = False,
    ancestor_note_id: Union[Unset, None, str] = UNSET,
    ancestor_depth: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
    order_direction: Union[Unset, None, SearchNotesOrderDirection] = SearchNotesOrderDirection.ASC,
    limit: Union[Unset, None, int] = UNSET,
    debug: Union[Unset, None, bool] = False,
) -> Response[SearchResponse]:
    """Search notes

    Args:
        search (str):
        fast_search (Union[Unset, None, bool]):
        include_archived_notes (Union[Unset, None, bool]):
        ancestor_note_id (Union[Unset, None, str]):  Example: evnnmvHTCgIn.
        ancestor_depth (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):
        order_direction (Union[Unset, None, SearchNotesOrderDirection]):  Default:
            SearchNotesOrderDirection.ASC.
        limit (Union[Unset, None, int]):
        debug (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponse]
    """

    kwargs = _get_kwargs(
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

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    search: str,
    fast_search: Union[Unset, None, bool] = False,
    include_archived_notes: Union[Unset, None, bool] = False,
    ancestor_note_id: Union[Unset, None, str] = UNSET,
    ancestor_depth: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
    order_direction: Union[Unset, None, SearchNotesOrderDirection] = SearchNotesOrderDirection.ASC,
    limit: Union[Unset, None, int] = UNSET,
    debug: Union[Unset, None, bool] = False,
) -> Optional[SearchResponse]:
    """Search notes

    Args:
        search (str):
        fast_search (Union[Unset, None, bool]):
        include_archived_notes (Union[Unset, None, bool]):
        ancestor_note_id (Union[Unset, None, str]):  Example: evnnmvHTCgIn.
        ancestor_depth (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):
        order_direction (Union[Unset, None, SearchNotesOrderDirection]):  Default:
            SearchNotesOrderDirection.ASC.
        limit (Union[Unset, None, int]):
        debug (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponse]
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
