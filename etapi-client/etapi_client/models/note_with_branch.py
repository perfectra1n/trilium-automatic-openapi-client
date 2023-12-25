from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import Dict
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.branch import Branch
    from ..models.note import Note


T = TypeVar("T", bound="NoteWithBranch")


@_attrs_define
class NoteWithBranch:
    """
    Attributes:
        note (Union[Unset, Note]):
        branch (Union[Unset, Branch]): Branch places the note into the tree, it represents the relationship between a
            parent note and child note
    """

    note: Union[Unset, "Note"] = UNSET
    branch: Union[Unset, "Branch"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        note: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.note, Unset):
            note = self.note.to_dict()

        branch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.branch, Unset):
            branch = self.branch.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note is not UNSET:
            field_dict["note"] = note
        if branch is not UNSET:
            field_dict["branch"] = branch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.branch import Branch
        from ..models.note import Note

        d = src_dict.copy()
        _note = d.pop("note", UNSET)
        note: Union[Unset, Note]
        if isinstance(_note, Unset):
            note = UNSET
        else:
            note = Note.from_dict(_note)

        _branch = d.pop("branch", UNSET)
        branch: Union[Unset, Branch]
        if isinstance(_branch, Unset):
            branch = UNSET
        else:
            branch = Branch.from_dict(_branch)

        note_with_branch = cls(
            note=note,
            branch=branch,
        )

        note_with_branch.additional_properties = d
        return note_with_branch

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
