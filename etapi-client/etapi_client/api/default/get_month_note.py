from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.note import Note


def _get_kwargs(
    month: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/calendar/months/{month}".format(
            month=month,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Note]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Note.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Note]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    month: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Note]:
    """returns a week note for a given date. Gets created if doesn't exist.

    Args:
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Note]
    """

    kwargs = _get_kwargs(
        month=month,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    month: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Note]:
    """returns a week note for a given date. Gets created if doesn't exist.

    Args:
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Note
    """

    return sync_detailed(
        month=month,
        client=client,
    ).parsed


async def asyncio_detailed(
    month: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Note]:
    """returns a week note for a given date. Gets created if doesn't exist.

    Args:
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Note]
    """

    kwargs = _get_kwargs(
        month=month,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    month: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Note]:
    """returns a week note for a given date. Gets created if doesn't exist.

    Args:
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Note
    """

    return (
        await asyncio_detailed(
            month=month,
            client=client,
        )
    ).parsed
