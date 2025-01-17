from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_type import AttributeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Attribute")


@_attrs_define
class Attribute:
    """Attribute (Label, Relation) is a key-value record attached to a note.

    Attributes:
        attribute_id (Union[Unset, str]):  Example: evnnmvHTCgIn.
        note_id (Union[Unset, Any]): identifies the child note
        type (Union[Unset, AttributeType]):
        name (Union[Unset, str]):  Example: shareCss.
        value (Union[Unset, str]):
        position (Union[Unset, int]):
        is_inheritable (Union[Unset, bool]):
        utc_date_modified (Union[Unset, str]):  Example: 2021-12-31 19:18:11.930000+00:00.
    """

    attribute_id: Union[Unset, str] = UNSET
    note_id: Union[Unset, Any] = UNSET
    type: Union[Unset, AttributeType] = UNSET
    name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET
    is_inheritable: Union[Unset, bool] = UNSET
    utc_date_modified: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_id = self.attribute_id

        note_id = self.note_id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        name = self.name

        value = self.value

        position = self.position

        is_inheritable = self.is_inheritable

        utc_date_modified = self.utc_date_modified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute_id is not UNSET:
            field_dict["attributeId"] = attribute_id
        if note_id is not UNSET:
            field_dict["noteId"] = note_id
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value
        if position is not UNSET:
            field_dict["position"] = position
        if is_inheritable is not UNSET:
            field_dict["isInheritable"] = is_inheritable
        if utc_date_modified is not UNSET:
            field_dict["utcDateModified"] = utc_date_modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute_id = d.pop("attributeId", UNSET)

        note_id = d.pop("noteId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AttributeType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AttributeType(_type)

        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        position = d.pop("position", UNSET)

        is_inheritable = d.pop("isInheritable", UNSET)

        utc_date_modified = d.pop("utcDateModified", UNSET)

        attribute = cls(
            attribute_id=attribute_id,
            note_id=note_id,
            type=type,
            name=name,
            value=value,
            position=position,
            is_inheritable=is_inheritable,
            utc_date_modified=utc_date_modified,
        )

        attribute.additional_properties = d
        return attribute

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
