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
) -> Dict[str, Any]:
    url = "{}/branches/{branchId}".format(client.base_url, branchId=branch_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Branch]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Branch.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
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
        client=client,
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
) -> Optional[Branch]:
    """Returns a branch identified by its ID

    Args:
        branch_id (str):  Example: evnnmvHTCgIn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Branch]
    """

    return sync_detailed(
        branch_id=branch_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    branch_id: str,
    *,
    client: Client,
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
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    branch_id: str,
    *,
    client: Client,
) -> Optional[Branch]:
    """Returns a branch identified by its ID

    Args:
        branch_id (str):  Example: evnnmvHTCgIn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Branch]
    """

    return (
        await asyncio_detailed(
            branch_id=branch_id,
            client=client,
        )
    ).parsed
