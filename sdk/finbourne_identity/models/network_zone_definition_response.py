# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist
from finbourne_identity.models.ip_address_definition import IpAddressDefinition
from finbourne_identity.models.network_zones_apply_rules import NetworkZonesApplyRules

class NetworkZoneDefinitionResponse(BaseModel):
    """
    The Client facing representation of a NetworkZone  # noqa: E501
    """
    code: Optional[StrictStr] = Field(None, description="The Network Zone Code")
    hierarchy: Optional[StrictInt] = Field(None, description="Hierarchy of the Network Zone")
    description: Optional[StrictStr] = Field(None, description="The Description of the Network Zone")
    created_at: Optional[datetime] = Field(None, alias="createdAt", description="Network Zone Creation timestamp")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt", description="Timestamp of the last update")
    network_zone_ips: Optional[conlist(IpAddressDefinition)] = Field(None, alias="networkZoneIPs", description="Network zone IP information (IPs and CIDR ranges)")
    action: Optional[StrictStr] = Field(None, description="Kind of action to apply when a request matches this Network Zone (Block/Allow/NoOp)")
    apply_rules: Optional[NetworkZonesApplyRules] = Field(None, alias="applyRules")
    created_by: Optional[StrictStr] = Field(None, alias="createdBy", description="User Id that created the Network Zone")
    updated_by: Optional[StrictStr] = Field(None, alias="updatedBy", description="User Id of the last update on the Network Zone")
    __properties = ["code", "hierarchy", "description", "createdAt", "updatedAt", "networkZoneIPs", "action", "applyRules", "createdBy", "updatedBy"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> NetworkZoneDefinitionResponse:
        """Create an instance of NetworkZoneDefinitionResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in network_zone_ips (list)
        _items = []
        if self.network_zone_ips:
            for _item in self.network_zone_ips:
                if _item:
                    _items.append(_item.to_dict())
            _dict['networkZoneIPs'] = _items
        # override the default output from pydantic by calling `to_dict()` of apply_rules
        if self.apply_rules:
            _dict['applyRules'] = self.apply_rules.to_dict()
        # set to None if code (nullable) is None
        # and __fields_set__ contains the field
        if self.code is None and "code" in self.__fields_set__:
            _dict['code'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if network_zone_ips (nullable) is None
        # and __fields_set__ contains the field
        if self.network_zone_ips is None and "network_zone_ips" in self.__fields_set__:
            _dict['networkZoneIPs'] = None

        # set to None if action (nullable) is None
        # and __fields_set__ contains the field
        if self.action is None and "action" in self.__fields_set__:
            _dict['action'] = None

        # set to None if created_by (nullable) is None
        # and __fields_set__ contains the field
        if self.created_by is None and "created_by" in self.__fields_set__:
            _dict['createdBy'] = None

        # set to None if updated_by (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_by is None and "updated_by" in self.__fields_set__:
            _dict['updatedBy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NetworkZoneDefinitionResponse:
        """Create an instance of NetworkZoneDefinitionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NetworkZoneDefinitionResponse.parse_obj(obj)

        _obj = NetworkZoneDefinitionResponse.parse_obj({
            "code": obj.get("code"),
            "hierarchy": obj.get("hierarchy"),
            "description": obj.get("description"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "network_zone_ips": [IpAddressDefinition.from_dict(_item) for _item in obj.get("networkZoneIPs")] if obj.get("networkZoneIPs") is not None else None,
            "action": obj.get("action"),
            "apply_rules": NetworkZonesApplyRules.from_dict(obj.get("applyRules")) if obj.get("applyRules") is not None else None,
            "created_by": obj.get("createdBy"),
            "updated_by": obj.get("updatedBy")
        })
        return _obj