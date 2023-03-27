from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.create_note_def_type import CreateNoteDefType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateNoteDef")


@attr.s(auto_attribs=True)
class CreateNoteDef:
    """
    Attributes:
        parent_note_id (str):  Example: evnnmvHTCgIn.
        title (str):
        type (CreateNoteDefType):
        content (str):
        mime (Union[Unset, str]): this needs to be specified only for note types 'code', 'file', 'image'. Example:
            application/json.
        note_position (Union[Unset, int]): Position of the note in the parent. Normal ordering is 10, 20, 30 ...  So if
            you want to create a note on the first position, use e.g. 5, for second position 15, for last e.g. 1000000
        prefix (Union[Unset, str]): Prefix is branch (placement) specific title prefix for the note.  Let's say you have
            your note placed into two different places in the tree,  but you want to change the title a bit in one of the
            placements. For this you can use prefix.
        is_expanded (Union[Unset, bool]): true if this note (as a folder) should appear expanded
        note_id (Union[Unset, str]):  Example: evnnmvHTCgIn.
        branch_id (Union[Unset, str]):  Example: evnnmvHTCgIn.
    """

    parent_note_id: str
    title: str
    type: CreateNoteDefType
    content: str
    mime: Union[Unset, str] = UNSET
    note_position: Union[Unset, int] = UNSET
    prefix: Union[Unset, str] = UNSET
    is_expanded: Union[Unset, bool] = UNSET
    note_id: Union[Unset, str] = UNSET
    branch_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parent_note_id = self.parent_note_id
        title = self.title
        type = self.type.value

        content = self.content
        mime = self.mime
        note_position = self.note_position
        prefix = self.prefix
        is_expanded = self.is_expanded
        note_id = self.note_id
        branch_id = self.branch_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parentNoteId": parent_note_id,
                "title": title,
                "type": type,
                "content": content,
            }
        )
        if mime is not UNSET:
            field_dict["mime"] = mime
        if note_position is not UNSET:
            field_dict["notePosition"] = note_position
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if is_expanded is not UNSET:
            field_dict["isExpanded"] = is_expanded
        if note_id is not UNSET:
            field_dict["noteId"] = note_id
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        parent_note_id = d.pop("parentNoteId")

        title = d.pop("title")

        type = CreateNoteDefType(d.pop("type"))

        content = d.pop("content")

        mime = d.pop("mime", UNSET)

        note_position = d.pop("notePosition", UNSET)

        prefix = d.pop("prefix", UNSET)

        is_expanded = d.pop("isExpanded", UNSET)

        note_id = d.pop("noteId", UNSET)

        branch_id = d.pop("branchId", UNSET)

        create_note_def = cls(
            parent_note_id=parent_note_id,
            title=title,
            type=type,
            content=content,
            mime=mime,
            note_position=note_position,
            prefix=prefix,
            is_expanded=is_expanded,
            note_id=note_id,
            branch_id=branch_id,
        )

        create_note_def.additional_properties = d
        return create_note_def

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
