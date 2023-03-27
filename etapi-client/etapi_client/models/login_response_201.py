from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginResponse201")


@attr.s(auto_attribs=True)
class LoginResponse201:
    """
    Attributes:
        auth_token (Union[Unset, str]):  Example: Bc4bFn0Ffiok_4NpbVCDnFz7B2WU+pdhW8B5Ne3DiR5wXrEyqdjgRIsk=.
    """

    auth_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auth_token = self.auth_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_token is not UNSET:
            field_dict["authToken"] = auth_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auth_token = d.pop("authToken", UNSET)

        login_response_201 = cls(
            auth_token=auth_token,
        )

        login_response_201.additional_properties = d
        return login_response_201

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
