from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multi_value_map_string_string_all import MultiValueMapStringStringAll


T = TypeVar("T", bound="MultiValueMapStringString")


@_attrs_define
class MultiValueMapStringString:
    """
    Attributes:
        all_ (Union[Unset, MultiValueMapStringStringAll]):
        empty (Union[Unset, bool]):
    """

    all_: Union[Unset, "MultiValueMapStringStringAll"] = UNSET
    empty: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, List[str]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        all_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.all_, Unset):
            all_ = self.all_.to_dict()

        empty = self.empty

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if empty is not UNSET:
            field_dict["empty"] = empty

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multi_value_map_string_string_all import MultiValueMapStringStringAll

        d = src_dict.copy()
        _all_ = d.pop("all", UNSET)
        all_: Union[Unset, MultiValueMapStringStringAll]
        if isinstance(_all_, Unset):
            all_ = UNSET
        else:
            all_ = MultiValueMapStringStringAll.from_dict(_all_)

        empty = d.pop("empty", UNSET)

        multi_value_map_string_string = cls(
            all_=all_,
            empty=empty,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = cast(List[str], prop_dict)

            additional_properties[prop_name] = additional_property

        multi_value_map_string_string.additional_properties = additional_properties
        return multi_value_map_string_string

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> List[str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: List[str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
