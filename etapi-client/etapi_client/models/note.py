from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.note_type import NoteType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute import Attribute


T = TypeVar("T", bound="Note")


@attr.s(auto_attribs=True)
class Note:
    """
    Attributes:
        note_id (Union[Unset, str]):  Example: evnnmvHTCgIn.
        title (Union[Unset, str]):
        type (Union[Unset, NoteType]):
        mime (Union[Unset, str]):
        is_protected (Union[Unset, bool]):
        attributes (Union[Unset, List['Attribute']]):
        parent_note_ids (Union[Unset, List[str]]):
        child_note_ids (Union[Unset, List[str]]):
        parent_branch_ids (Union[Unset, List[str]]):
        child_branch_ids (Union[Unset, List[str]]):
        date_created (Union[Unset, str]):  Example: 2021-12-31 20:18:11.939+0100.
        date_modified (Union[Unset, str]):  Example: 2021-12-31 20:18:11.939+0100.
        utc_date_created (Union[Unset, str]):  Example: 2021-12-31 19:18:11.939000+00:00.
        utc_date_modified (Union[Unset, str]):  Example: 2021-12-31 19:18:11.939000+00:00.
    """

    note_id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type: Union[Unset, NoteType] = UNSET
    mime: Union[Unset, str] = UNSET
    is_protected: Union[Unset, bool] = UNSET
    attributes: Union[Unset, List["Attribute"]] = UNSET
    parent_note_ids: Union[Unset, List[str]] = UNSET
    child_note_ids: Union[Unset, List[str]] = UNSET
    parent_branch_ids: Union[Unset, List[str]] = UNSET
    child_branch_ids: Union[Unset, List[str]] = UNSET
    date_created: Union[Unset, str] = UNSET
    date_modified: Union[Unset, str] = UNSET
    utc_date_created: Union[Unset, str] = UNSET
    utc_date_modified: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        note_id = self.note_id
        title = self.title
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        mime = self.mime
        is_protected = self.is_protected
        attributes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for componentsschemas_attribute_list_item_data in self.attributes:
                componentsschemas_attribute_list_item = componentsschemas_attribute_list_item_data.to_dict()

                attributes.append(componentsschemas_attribute_list_item)

        parent_note_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.parent_note_ids, Unset):
            parent_note_ids = self.parent_note_ids

        child_note_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.child_note_ids, Unset):
            child_note_ids = self.child_note_ids

        parent_branch_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.parent_branch_ids, Unset):
            parent_branch_ids = self.parent_branch_ids

        child_branch_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.child_branch_ids, Unset):
            child_branch_ids = self.child_branch_ids

        date_created = self.date_created
        date_modified = self.date_modified
        utc_date_created = self.utc_date_created
        utc_date_modified = self.utc_date_modified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note_id is not UNSET:
            field_dict["noteId"] = note_id
        if title is not UNSET:
            field_dict["title"] = title
        if type is not UNSET:
            field_dict["type"] = type
        if mime is not UNSET:
            field_dict["mime"] = mime
        if is_protected is not UNSET:
            field_dict["isProtected"] = is_protected
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if parent_note_ids is not UNSET:
            field_dict["parentNoteIds"] = parent_note_ids
        if child_note_ids is not UNSET:
            field_dict["childNoteIds"] = child_note_ids
        if parent_branch_ids is not UNSET:
            field_dict["parentBranchIds"] = parent_branch_ids
        if child_branch_ids is not UNSET:
            field_dict["childBranchIds"] = child_branch_ids
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if date_modified is not UNSET:
            field_dict["dateModified"] = date_modified
        if utc_date_created is not UNSET:
            field_dict["utcDateCreated"] = utc_date_created
        if utc_date_modified is not UNSET:
            field_dict["utcDateModified"] = utc_date_modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute import Attribute

        d = src_dict.copy()
        note_id = d.pop("noteId", UNSET)

        title = d.pop("title", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, NoteType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = NoteType(_type)

        mime = d.pop("mime", UNSET)

        is_protected = d.pop("isProtected", UNSET)

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for componentsschemas_attribute_list_item_data in _attributes or []:
            componentsschemas_attribute_list_item = Attribute.from_dict(componentsschemas_attribute_list_item_data)

            attributes.append(componentsschemas_attribute_list_item)

        parent_note_ids = cast(List[str], d.pop("parentNoteIds", UNSET))

        child_note_ids = cast(List[str], d.pop("childNoteIds", UNSET))

        parent_branch_ids = cast(List[str], d.pop("parentBranchIds", UNSET))

        child_branch_ids = cast(List[str], d.pop("childBranchIds", UNSET))

        date_created = d.pop("dateCreated", UNSET)

        date_modified = d.pop("dateModified", UNSET)

        utc_date_created = d.pop("utcDateCreated", UNSET)

        utc_date_modified = d.pop("utcDateModified", UNSET)

        note = cls(
            note_id=note_id,
            title=title,
            type=type,
            mime=mime,
            is_protected=is_protected,
            attributes=attributes,
            parent_note_ids=parent_note_ids,
            child_note_ids=child_note_ids,
            parent_branch_ids=parent_branch_ids,
            child_branch_ids=child_branch_ids,
            date_created=date_created,
            date_modified=date_modified,
            utc_date_created=utc_date_created,
            utc_date_modified=utc_date_modified,
        )

        note.additional_properties = d
        return note

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
