from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.note import Note
    from ..models.search_response_debug_info import SearchResponseDebugInfo


T = TypeVar("T", bound="SearchResponse")


@attr.s(auto_attribs=True)
class SearchResponse:
    """
    Attributes:
        results (List['Note']):
        debug_info (Union[Unset, SearchResponseDebugInfo]): debugging info on parsing the search query enabled with
            &debug=true parameter
    """

    results: List["Note"]
    debug_info: Union[Unset, "SearchResponseDebugInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()

            results.append(results_item)

        debug_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.debug_info, Unset):
            debug_info = self.debug_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
            }
        )
        if debug_info is not UNSET:
            field_dict["debugInfo"] = debug_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.note import Note
        from ..models.search_response_debug_info import SearchResponseDebugInfo

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = Note.from_dict(results_item_data)

            results.append(results_item)

        _debug_info = d.pop("debugInfo", UNSET)
        debug_info: Union[Unset, SearchResponseDebugInfo]
        if isinstance(_debug_info, Unset):
            debug_info = UNSET
        else:
            debug_info = SearchResponseDebugInfo.from_dict(_debug_info)

        search_response = cls(
            results=results,
            debug_info=debug_info,
        )

        search_response.additional_properties = d
        return search_response

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
