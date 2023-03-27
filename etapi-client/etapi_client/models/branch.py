from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Branch")


@attr.s(auto_attribs=True)
class Branch:
    """Branch places the note into the tree, it represents the relationship between a parent note and child note

    Attributes:
        note_id (str):  Example: evnnmvHTCgIn.
        parent_note_id (str):  Example: evnnmvHTCgIn.
        branch_id (Union[Unset, str]):  Example: evnnmvHTCgIn.
        prefix (Union[Unset, str]):
        note_position (Union[Unset, int]):
        is_expanded (Union[Unset, bool]):
        utc_date_modified (Union[Unset, str]):  Example: 2021-12-31 19:18:11.939000+00:00.
    """

    note_id: str
    parent_note_id: str
    branch_id: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    note_position: Union[Unset, int] = UNSET
    is_expanded: Union[Unset, bool] = UNSET
    utc_date_modified: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        note_id = self.note_id
        parent_note_id = self.parent_note_id
        branch_id = self.branch_id
        prefix = self.prefix
        note_position = self.note_position
        is_expanded = self.is_expanded
        utc_date_modified = self.utc_date_modified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "noteId": note_id,
                "parentNoteId": parent_note_id,
            }
        )
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
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
        note_id = d.pop("noteId")

        parent_note_id = d.pop("parentNoteId")

        branch_id = d.pop("branchId", UNSET)

        prefix = d.pop("prefix", UNSET)

        note_position = d.pop("notePosition", UNSET)

        is_expanded = d.pop("isExpanded", UNSET)

        utc_date_modified = d.pop("utcDateModified", UNSET)

        branch = cls(
            note_id=note_id,
            parent_note_id=parent_note_id,
            branch_id=branch_id,
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
