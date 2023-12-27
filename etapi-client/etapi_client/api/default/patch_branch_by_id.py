from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.branch import Branch
from typing import Dict


def _get_kwargs(
    branch_id: str,
    *,
    json_body: Branch,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": "/branches/{branchId}".format(
            branchId=branch_id,
        ),
        "json": json_json_body,
    }


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
    json_body: Branch,
) -> Response[Branch]:
    """patch a branch identified by the branchId with changes in the body. Only prefix and notePosition can
    be updated. If you want to update other properties, you need to delete the old branch and create a
    new one.

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
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    branch_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Branch,
) -> Optional[Branch]:
    """patch a branch identified by the branchId with changes in the body. Only prefix and notePosition can
    be updated. If you want to update other properties, you need to delete the old branch and create a
    new one.

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
    client: Union[AuthenticatedClient, Client],
    json_body: Branch,
) -> Response[Branch]:
    """patch a branch identified by the branchId with changes in the body. Only prefix and notePosition can
    be updated. If you want to update other properties, you need to delete the old branch and create a
    new one.

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
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    branch_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Branch,
) -> Optional[Branch]:
    """patch a branch identified by the branchId with changes in the body. Only prefix and notePosition can
    be updated. If you want to update other properties, you need to delete the old branch and create a
    new one.

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
