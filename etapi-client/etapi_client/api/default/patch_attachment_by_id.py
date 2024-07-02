from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attachment import Attachment
from ...types import Response


def _get_kwargs(
    attachment_id: str,
    *,
    body: Attachment,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/attachments/{attachment_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Attachment]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Attachment.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Attachment]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Attachment,
) -> Response[Attachment]:
    """patch an attachment identified by the attachmentId with changes in the body. Only role, mime, title,
    and position are patchable.

    Args:
        attachment_id (str):  Example: evnnmvHTCgIn.
        body (Attachment): Attachment is owned by a note, has title and content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Attachment]
    """

    kwargs = _get_kwargs(
        attachment_id=attachment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Attachment,
) -> Optional[Attachment]:
    """patch an attachment identified by the attachmentId with changes in the body. Only role, mime, title,
    and position are patchable.

    Args:
        attachment_id (str):  Example: evnnmvHTCgIn.
        body (Attachment): Attachment is owned by a note, has title and content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Attachment
    """

    return sync_detailed(
        attachment_id=attachment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Attachment,
) -> Response[Attachment]:
    """patch an attachment identified by the attachmentId with changes in the body. Only role, mime, title,
    and position are patchable.

    Args:
        attachment_id (str):  Example: evnnmvHTCgIn.
        body (Attachment): Attachment is owned by a note, has title and content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Attachment]
    """

    kwargs = _get_kwargs(
        attachment_id=attachment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Attachment,
) -> Optional[Attachment]:
    """patch an attachment identified by the attachmentId with changes in the body. Only role, mime, title,
    and position are patchable.

    Args:
        attachment_id (str):  Example: evnnmvHTCgIn.
        body (Attachment): Attachment is owned by a note, has title and content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Attachment
    """

    return (
        await asyncio_detailed(
            attachment_id=attachment_id,
            client=client,
            body=body,
        )
    ).parsed
