from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from typing import Dict
from ...models.branch import Branch


def _get_kwargs(
    branch_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/branches/{branchId}".format(
            branchId=branch_id,
        ),
    }

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
) -> Response[Branch]:
    """Returns a branch identified by its ID

    Args:
        branch_id (str):  Example: evnnmvHTCgIn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Branch]
    """

    kwargs = _get_kwargs(
        branch_id=branch_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    branch_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Branch]:
    """Returns a branch identified by its ID

    Args:
        branch_id (str):  Example: evnnmvHTCgIn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Branch
    """

    return sync_detailed(
        branch_id=branch_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    branch_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Branch]:
    """Returns a branch identified by its ID

    Args:
        branch_id (str):  Example: evnnmvHTCgIn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Branch]
    """

    kwargs = _get_kwargs(
        branch_id=branch_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    branch_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Branch]:
    """Returns a branch identified by its ID

    Args:
        branch_id (str):  Example: evnnmvHTCgIn.

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
        )
    ).parsed
