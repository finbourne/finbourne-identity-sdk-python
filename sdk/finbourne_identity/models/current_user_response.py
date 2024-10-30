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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr
from finbourne_identity.models.link import Link

class CurrentUserResponse(BaseModel):
    """
    CurrentUserResponse
    """
    id: constr(strict=True, min_length=1) = Field(..., description="The user's system supplied unique identifier")
    email_address: constr(strict=True, min_length=1) = Field(..., alias="emailAddress", description="The user's email address which may be null depending on the authentication method")
    type: constr(strict=True, min_length=1) = Field(..., description="The type of user (e.g. Personal or Service)")
    domain_type: Optional[StrictStr] = Field(None, alias="domainType", description="The type of domain in which the user exists")
    user_expiry: Optional[datetime] = Field(None, alias="userExpiry", description="The user's user expiry datetime")
    links: Optional[conlist(Link)] = None
    __properties = ["id", "emailAddress", "type", "domainType", "userExpiry", "links"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CurrentUserResponse:
        """Create an instance of CurrentUserResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if domain_type (nullable) is None
        # and __fields_set__ contains the field
        if self.domain_type is None and "domain_type" in self.__fields_set__:
            _dict['domainType'] = None

        # set to None if user_expiry (nullable) is None
        # and __fields_set__ contains the field
        if self.user_expiry is None and "user_expiry" in self.__fields_set__:
            _dict['userExpiry'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CurrentUserResponse:
        """Create an instance of CurrentUserResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CurrentUserResponse.parse_obj(obj)

        _obj = CurrentUserResponse.parse_obj({
            "id": obj.get("id"),
            "email_address": obj.get("emailAddress"),
            "type": obj.get("type"),
            "domain_type": obj.get("domainType"),
            "user_expiry": obj.get("userExpiry"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
