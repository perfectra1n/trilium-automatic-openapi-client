from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.branch import Branch
from ...types import Response


def _get_kwargs(
    branch_id: str,
    *,
    client: Client,
    json_body: Branch,
) -> Dict[str, Any]:
    url = "{}/branches/{branchId}".format(client.base_url, branchId=branch_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Branch]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Branch.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Branch.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Branch]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    branch_id: str,
    *,
    client: Client,
    json_body: Branch,
) -> Response[Branch]:
    """Create a branch (clone a note to a different location in the tree). In case there is a branch
    between parent note and child note already,  then this will update the existing branch with prefix,
    notePosition and isExpanded.

    Args:
        branch_id (str):  Example: evnnmvHTCgIn.
        json_body (Branch): Branch places the note into the tree, it represents the relationship
            between a parent note and child note

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Branch]
    """

    kwargs = _get_kwargs(
        branch_id=branch_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    branch_id: str,
    *,
    client: Client,
    json_body: Branch,
) -> Optional[Branch]:
    """Create a branch (clone a note to a different location in the tree). In case there is a branch
    between parent note and child note already,  then this will update the existing branch with prefix,
    notePosition and isExpanded.

    Args:
        branch_id (str):  Example: evnnmvHTCgIn.
        json_body (Branch): Branch places the note into the tree, it represents the relationship
            between a parent note and child note

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Branch
    """

    return sync_detailed(
        branch_id=branch_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    branch_id: str,
    *,
    client: Client,
    json_body: Branch,
) -> Response[Branch]:
    """Create a branch (clone a note to a different location in the tree). In case there is a branch
    between parent note and child note already,  then this will update the existing branch with prefix,
    notePosition and isExpanded.

    Args:
        branch_id (str):  Example: evnnmvHTCgIn.
        json_body (Branch): Branch places the note into the tree, it represents the relationship
            between a parent note and child note

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Branch]
    """

    kwargs = _get_kwargs(
        branch_id=branch_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    branch_id: str,
    *,
    client: Client,
    json_body: Branch,
) -> Optional[Branch]:
    """Create a branch (clone a note to a different location in the tree). In case there is a branch
    between parent note and child note already,  then this will update the existing branch with prefix,
    notePosition and isExpanded.

    Args:
        branch_id (str):  Example: evnnmvHTCgIn.
        json_body (Branch): Branch places the note into the tree, it represents the relationship
            between a parent note and child note

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Branch
    """

    return (
        await asyncio_detailed(
            branch_id=branch_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
