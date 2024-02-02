from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union


T = TypeVar("T", bound="Branch")


@_attrs_define
class Branch:
    """Branch places the note into the tree, it represents the relationship between a parent note and child note

    Attributes:
        branch_id (Union[Unset, str]):  Example: evnnmvHTCgIn.
        note_id (Union[Unset, str]):  Example: evnnmvHTCgIn.
        parent_note_id (Union[Unset, str]):  Example: evnnmvHTCgIn.
        prefix (Union[Unset, str]):
        note_position (Union[Unset, int]):
        is_expanded (Union[Unset, bool]):
        utc_date_modified (Union[Unset, str]):  Example: 2021-12-31 19:18:11.930000+00:00.
    """

    branch_id: Union[Unset, str] = UNSET
    note_id: Union[Unset, str] = UNSET
    parent_note_id: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    note_position: Union[Unset, int] = UNSET
    is_expanded: Union[Unset, bool] = UNSET
    utc_date_modified: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        branch_id = self.branch_id

        note_id = self.note_id

        parent_note_id = self.parent_note_id

        prefix = self.prefix

        note_position = self.note_position

        is_expanded = self.is_expanded

        utc_date_modified = self.utc_date_modified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if note_id is not UNSET:
            field_dict["noteId"] = note_id
        if parent_note_id is not UNSET:
            field_dict["parentNoteId"] = parent_note_id
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if note_position is not UNSET:
            field_dict["notePosition"] = note_position
        if is_expanded is not UNSET:
            field_dict["isExpanded"] = is_expanded
        if utc_date_modified is not UNSET:
            field_dict["utcDateModified"] = utc_date_modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        branch_id = d.pop("branchId", UNSET)

        note_id = d.pop("noteId", UNSET)

        parent_note_id = d.pop("parentNoteId", UNSET)

        prefix = d.pop("prefix", UNSET)

        note_position = d.pop("notePosition", UNSET)

        is_expanded = d.pop("isExpanded", UNSET)

        utc_date_modified = d.pop("utcDateModified", UNSET)

        branch = cls(
            branch_id=branch_id,
            note_id=note_id,
            parent_note_id=parent_note_id,
            prefix=prefix,
            note_position=note_position,
            is_expanded=is_expanded,
            utc_date_modified=utc_date_modified,
        )

        branch.additional_properties = d
        return branch

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
