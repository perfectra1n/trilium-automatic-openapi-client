import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppInfo")


@attr.s(auto_attribs=True)
class AppInfo:
    """
    Attributes:
        app_version (Union[Unset, str]): Trilium version Example: 0.50.2.
        db_version (Union[Unset, int]): DB version Example: 194.
        sync_version (Union[Unset, int]): Sync protocol version Example: 25.
        build_date (Union[Unset, datetime.datetime]): build date Example: 2022-02-09 22:52:36+01:00.
        build_revision (Union[Unset, str]): git build revision Example: 23daaa2387a0655685377f0a541d154aeec2aae8.
        data_directory (Union[Unset, str]): data directory where Trilium stores files Example: /home/user/data.
        clipper_protocol_version (Union[Unset, str]): version of the supported Trilium Web Clipper protocol Example:
            1.0.
        utc_date_time (Union[Unset, str]): current UTC date time Example: 2022-03-07 21:54:25.277000+00:00.
    """

    app_version: Union[Unset, str] = UNSET
    db_version: Union[Unset, int] = UNSET
    sync_version: Union[Unset, int] = UNSET
    build_date: Union[Unset, datetime.datetime] = UNSET
    build_revision: Union[Unset, str] = UNSET
    data_directory: Union[Unset, str] = UNSET
    clipper_protocol_version: Union[Unset, str] = UNSET
    utc_date_time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app_version = self.app_version
        db_version = self.db_version
        sync_version = self.sync_version
        build_date: Union[Unset, str] = UNSET
        if not isinstance(self.build_date, Unset):
            build_date = self.build_date.isoformat()

        build_revision = self.build_revision
        data_directory = self.data_directory
        clipper_protocol_version = self.clipper_protocol_version
        utc_date_time = self.utc_date_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_version is not UNSET:
            field_dict["appVersion"] = app_version
        if db_version is not UNSET:
            field_dict["dbVersion"] = db_version
        if sync_version is not UNSET:
            field_dict["syncVersion"] = sync_version
        if build_date is not UNSET:
            field_dict["buildDate"] = build_date
        if build_revision is not UNSET:
            field_dict["buildRevision"] = build_revision
        if data_directory is not UNSET:
            field_dict["dataDirectory"] = data_directory
        if clipper_protocol_version is not UNSET:
            field_dict["clipperProtocolVersion"] = clipper_protocol_version
        if utc_date_time is not UNSET:
            field_dict["utcDateTime"] = utc_date_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        app_version = d.pop("appVersion", UNSET)

        db_version = d.pop("dbVersion", UNSET)

        sync_version = d.pop("syncVersion", UNSET)

        _build_date = d.pop("buildDate", UNSET)
        build_date: Union[Unset, datetime.datetime]
        if isinstance(_build_date, Unset):
            build_date = UNSET
        else:
            build_date = isoparse(_build_date)

        build_revision = d.pop("buildRevision", UNSET)

        data_directory = d.pop("dataDirectory", UNSET)

        clipper_protocol_version = d.pop("clipperProtocolVersion", UNSET)

        utc_date_time = d.pop("utcDateTime", UNSET)

        app_info = cls(
            app_version=app_version,
            db_version=db_version,
            sync_version=sync_version,
            build_date=build_date,
            build_revision=build_revision,
            data_directory=data_directory,
            clipper_protocol_version=clipper_protocol_version,
            utc_date_time=utc_date_time,
        )

        app_info.additional_properties = d
        return app_info

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
