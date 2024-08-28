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


from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, constr
from finbourne_identity.models.link import Link
from finbourne_identity.models.role_response import RoleResponse

class UserResponse(BaseModel):
    """
    UserResponse
    """
    id: constr(strict=True, min_length=1) = Field(..., description="The user's system supplied unique identifier")
    alternative_user_ids: Optional[Dict[str, StrictStr]] = Field(None, alias="alternativeUserIds", description="The user's alternative IDs")
    email_address: constr(strict=True, min_length=1) = Field(..., alias="emailAddress", description="The user's emailAddress address, which must be unique within the system")
    second_email_address: Optional[StrictStr] = Field(None, alias="secondEmailAddress", description="The user's second email address. Only allowed for service users.")
    login: constr(strict=True, min_length=1) = Field(...)
    first_name: constr(strict=True, min_length=1) = Field(..., alias="firstName", description="The user's first name")
    last_name: constr(strict=True, min_length=1) = Field(..., alias="lastName", description="The user's last name")
    roles: Optional[conlist(RoleResponse)] = Field(None, description="The roles that the user has.")
    type: constr(strict=True, min_length=1) = Field(..., description="The type of user (e.g. Personal or Service)")
    status: constr(strict=True, min_length=1) = Field(..., description="The status of the user")
    external: StrictBool = Field(..., description="Whether or not the user originates from an external identity system")
    links: Optional[conlist(Link)] = None
    __properties = ["id", "alternativeUserIds", "emailAddress", "secondEmailAddress", "login", "firstName", "lastName", "roles", "type", "status", "external", "links"]

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
    def from_json(cls, json_str: str) -> UserResponse:
        """Create an instance of UserResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if alternative_user_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.alternative_user_ids is None and "alternative_user_ids" in self.__fields_set__:
            _dict['alternativeUserIds'] = None

        # set to None if second_email_address (nullable) is None
        # and __fields_set__ contains the field
        if self.second_email_address is None and "second_email_address" in self.__fields_set__:
            _dict['secondEmailAddress'] = None

        # set to None if roles (nullable) is None
        # and __fields_set__ contains the field
        if self.roles is None and "roles" in self.__fields_set__:
            _dict['roles'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserResponse:
        """Create an instance of UserResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserResponse.parse_obj(obj)

        _obj = UserResponse.parse_obj({
            "id": obj.get("id"),
            "alternative_user_ids": obj.get("alternativeUserIds"),
            "email_address": obj.get("emailAddress"),
            "second_email_address": obj.get("secondEmailAddress"),
            "login": obj.get("login"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "roles": [RoleResponse.from_dict(_item) for _item in obj.get("roles")] if obj.get("roles") is not None else None,
            "type": obj.get("type"),
            "status": obj.get("status"),
            "external": obj.get("external"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
