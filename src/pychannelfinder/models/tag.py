from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel import Channel


T = TypeVar("T", bound="Tag")


@_attrs_define
class Tag:
    """
    Attributes:
        name (Union[Unset, str]):
        owner (Union[Unset, str]):
        channels (Union[Unset, List['Channel']]):
    """

    name: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    channels: Union[Unset, List[Channel]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        owner = self.owner

        channels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:  # pylint: disable=not-an-iterable
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if channels is not UNSET:
            field_dict["channels"] = channels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.channel import Channel

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        owner = d.pop("owner", UNSET)

        channels = []
        _channels = d.pop("channels", UNSET)
        for channels_item_data in _channels or []:
            channels_item = Channel.from_dict(channels_item_data)

            channels.append(channels_item)

        tag = cls(
            name=name,
            owner=owner,
            channels=channels,
        )

        tag.additional_properties = d
        return tag

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
