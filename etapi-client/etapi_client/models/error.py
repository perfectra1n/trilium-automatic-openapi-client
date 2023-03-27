from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Error")


@attr.s(auto_attribs=True)
class Error:
    """
    Attributes:
        status (int): HTTP status, identical to the one given in HTTP response Example: 400.
        code (str): stable string constant Example: NOTE_IS_PROTECTED.
        message (str): Human readable error, potentially with more details, Example: Note 'evnnmvHTCgIn' is protected
            and cannot be modified through ETAPI.
    """

    status: int
    code: str
    message: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        code = self.code
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "code": code,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status")

        code = d.pop("code")

        message = d.pop("message")

        error = cls(
            status=status,
            code=code,
            message=message,
        )

        error.additional_properties = d
        return error

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
