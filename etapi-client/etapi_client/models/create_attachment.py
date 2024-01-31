from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from ..types import UNSET, Unset


T = TypeVar("T", bound="CreateAttachment")


@_attrs_define
class CreateAttachment:
    """
    Attributes:
        owner_id (Union[Unset, str]):  Example: evnnmvHTCgIn.
        role (Union[Unset, str]):
        mime (Union[Unset, str]):
        title (Union[Unset, str]):
        content (Union[Unset, str]):
        position (Union[Unset, int]):
    """

    owner_id: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    mime: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owner_id = self.owner_id

        role = self.role

        mime = self.mime

        title = self.title

        content = self.content

        position = self.position

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if role is not UNSET:
            field_dict["role"] = role
        if mime is not UNSET:
            field_dict["mime"] = mime
        if title is not UNSET:
            field_dict["title"] = title
        if content is not UNSET:
            field_dict["content"] = content
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        owner_id = d.pop("ownerId", UNSET)

        role = d.pop("role", UNSET)

        mime = d.pop("mime", UNSET)

        title = d.pop("title", UNSET)

        content = d.pop("content", UNSET)

        position = d.pop("position", UNSET)

        create_attachment = cls(
            owner_id=owner_id,
            role=role,
            mime=mime,
            title=title,
            content=content,
            position=position,
        )

        create_attachment.additional_properties = d
        return create_attachment

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
