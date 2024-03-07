from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.branch import Branch


def _get_kwargs(
    branch_id: str,
    *,
    body: Branch,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/branches/{branch_id}".format(
            branch_id=branch_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Branch]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Branch.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Branch]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    branch_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Branch,
) -> Response[Branch]:
    """patch a branch identified by the branchId with changes in the body. Only prefix and notePosition can
    be updated. If you want to update other properties, you need to delete the old branch and create a
    new one.

    Args:
        branch_id (str):  Example: evnnmvHTCgIn.
        body (Branch): Branch places the note into the tree, it represents the relationship
            between a parent note and child note

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Branch]
    """

    kwargs = _get_kwargs(
        branch_id=branch_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    branch_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Branch,
) -> Optional[Branch]:
    """patch a branch identified by the branchId with changes in the body. Only prefix and notePosition can
    be updated. If you want to update other properties, you need to delete the old branch and create a
    new one.

    Args:
        branch_id (str):  Example: evnnmvHTCgIn.
        body (Branch): Branch places the note into the tree, it represents the relationship
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
        body=body,
    ).parsed


async def asyncio_detailed(
    branch_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Branch,
) -> Response[Branch]:
    """patch a branch identified by the branchId with changes in the body. Only prefix and notePosition can
    be updated. If you want to update other properties, you need to delete the old branch and create a
    new one.

    Args:
        branch_id (str):  Example: evnnmvHTCgIn.
        body (Branch): Branch places the note into the tree, it represents the relationship
            between a parent note and child note

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Branch]
    """

    kwargs = _get_kwargs(
        branch_id=branch_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    branch_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Branch,
) -> Optional[Branch]:
    """patch a branch identified by the branchId with changes in the body. Only prefix and notePosition can
    be updated. If you want to update other properties, you need to delete the old branch and create a
    new one.

    Args:
        branch_id (str):  Example: evnnmvHTCgIn.
        body (Branch): Branch places the note into the tree, it represents the relationship
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
            body=body,
        )
    ).parsed
