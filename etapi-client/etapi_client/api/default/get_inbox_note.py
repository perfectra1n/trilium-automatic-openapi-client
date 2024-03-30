from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

import datetime
from ...models.note import Note


def _get_kwargs(
    date: datetime.date,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/inbox/{date}".format(
            date=date,
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
    date: datetime.date,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Note]:
    r"""returns an \"inbox\" note, into which note can be created. Date will be used depending on whether
    the inbox is a fixed note (identified with #inbox label) or a day note in a journal.

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Note]
    """

    kwargs = _get_kwargs(
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    date: datetime.date,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Note]:
    r"""returns an \"inbox\" note, into which note can be created. Date will be used depending on whether
    the inbox is a fixed note (identified with #inbox label) or a day note in a journal.

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Note
    """

    return sync_detailed(
        date=date,
        client=client,
    ).parsed


async def asyncio_detailed(
    date: datetime.date,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Note]:
    r"""returns an \"inbox\" note, into which note can be created. Date will be used depending on whether
    the inbox is a fixed note (identified with #inbox label) or a day note in a journal.

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Note]
    """

    kwargs = _get_kwargs(
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    date: datetime.date,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Note]:
    r"""returns an \"inbox\" note, into which note can be created. Date will be used depending on whether
    the inbox is a fixed note (identified with #inbox label) or a day note in a journal.

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Note
    """

    return (
        await asyncio_detailed(
            date=date,
            client=client,
        )
    ).parsed
