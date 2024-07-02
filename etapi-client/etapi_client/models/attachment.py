from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Attachment")


@_attrs_define
class Attachment:
    """Attachment is owned by a note, has title and content

    Attributes:
        attachment_id (Union[Unset, str]):  Example: evnnmvHTCgIn.
        owner_id (Union[Unset, str]):  Example: evnnmvHTCgIn.
        role (Union[Unset, str]):
        mime (Union[Unset, str]):
        title (Union[Unset, str]):
        position (Union[Unset, int]):
        blob_id (Union[Unset, str]): ID of the blob object which effectively serves as a content hash
        date_modified (Union[Unset, str]):  Example: 2021-12-31 20:18:11.930+0100.
        utc_date_modified (Union[Unset, str]):  Example: 2021-12-31 19:18:11.930000+00:00.
        utc_date_scheduled_for_erasure_since (Union[Unset, str]):  Example: 2021-12-31 19:18:11.930000+00:00.
        content_length (Union[Unset, int]):
    """

    attachment_id: Union[Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    mime: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET
    blob_id: Union[Unset, str] = UNSET
    date_modified: Union[Unset, str] = UNSET
    utc_date_modified: Union[Unset, str] = UNSET
    utc_date_scheduled_for_erasure_since: Union[Unset, str] = UNSET
    content_length: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attachment_id = self.attachment_id

        owner_id = self.owner_id

        role = self.role

        mime = self.mime

        title = self.title

        position = self.position

        blob_id = self.blob_id

        date_modified = self.date_modified

        utc_date_modified = self.utc_date_modified

        utc_date_scheduled_for_erasure_since = self.utc_date_scheduled_for_erasure_since

        content_length = self.content_length

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachment_id is not UNSET:
            field_dict["attachmentId"] = attachment_id
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if role is not UNSET:
            field_dict["role"] = role
        if mime is not UNSET:
            field_dict["mime"] = mime
        if title is not UNSET:
            field_dict["title"] = title
        if position is not UNSET:
            field_dict["position"] = position
        if blob_id is not UNSET:
            field_dict["blobId"] = blob_id
        if date_modified is not UNSET:
            field_dict["dateModified"] = date_modified
        if utc_date_modified is not UNSET:
            field_dict["utcDateModified"] = utc_date_modified
        if utc_date_scheduled_for_erasure_since is not UNSET:
            field_dict["utcDateScheduledForErasureSince"] = utc_date_scheduled_for_erasure_since
        if content_length is not UNSET:
            field_dict["contentLength"] = content_length

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attachment_id = d.pop("attachmentId", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        role = d.pop("role", UNSET)

        mime = d.pop("mime", UNSET)

        title = d.pop("title", UNSET)

        position = d.pop("position", UNSET)

        blob_id = d.pop("blobId", UNSET)

        date_modified = d.pop("dateModified", UNSET)

        utc_date_modified = d.pop("utcDateModified", UNSET)

        utc_date_scheduled_for_erasure_since = d.pop("utcDateScheduledForErasureSince", UNSET)

        content_length = d.pop("contentLength", UNSET)

        attachment = cls(
            attachment_id=attachment_id,
            owner_id=owner_id,
            role=role,
            mime=mime,
            title=title,
            position=position,
            blob_id=blob_id,
            date_modified=date_modified,
            utc_date_modified=utc_date_modified,
            utc_date_scheduled_for_erasure_since=utc_date_scheduled_for_erasure_since,
            content_length=content_length,
        )

        attachment.additional_properties = d
        return attachment

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
