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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, conlist, constr, validator 
from finbourne_identity.models.role_id import RoleId

class UpdateUserRequest(BaseModel):
    """
    UpdateUserRequest
    """
    first_name:  StrictStr = Field(...,alias="firstName") 
    last_name:  StrictStr = Field(...,alias="lastName") 
    email_address:  StrictStr = Field(...,alias="emailAddress") 
    second_email_address:  Optional[StrictStr] = Field(None,alias="secondEmailAddress") 
    login:  StrictStr = Field(...,alias="login", description="The user's login username, in the form of an email address, which must be unique within the system.  For user accounts this should exactly match the user's email address.") 
    alternative_user_ids: Optional[Dict[str, StrictStr]] = Field(None, alias="alternativeUserIds")
    roles: Optional[conlist(RoleId)] = Field(None, description="Deprecated. To update a user's roles use the AddUserToRole and RemoveUserFromRole endpoints")
    __properties = ["firstName", "lastName", "emailAddress", "secondEmailAddress", "login", "alternativeUserIds", "roles"]

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
    def from_json(cls, json_str: str) -> UpdateUserRequest:
        """Create an instance of UpdateUserRequest from a JSON string"""
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
        # set to None if second_email_address (nullable) is None
        # and __fields_set__ contains the field
        if self.second_email_address is None and "second_email_address" in self.__fields_set__:
            _dict['secondEmailAddress'] = None

        # set to None if alternative_user_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.alternative_user_ids is None and "alternative_user_ids" in self.__fields_set__:
            _dict['alternativeUserIds'] = None

        # set to None if roles (nullable) is None
        # and __fields_set__ contains the field
        if self.roles is None and "roles" in self.__fields_set__:
            _dict['roles'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateUserRequest:
        """Create an instance of UpdateUserRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateUserRequest.parse_obj(obj)

        _obj = UpdateUserRequest.parse_obj({
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "email_address": obj.get("emailAddress"),
            "second_email_address": obj.get("secondEmailAddress"),
            "login": obj.get("login"),
            "alternative_user_ids": obj.get("alternativeUserIds"),
            "roles": [RoleId.from_dict(_item) for _item in obj.get("roles")] if obj.get("roles") is not None else None
        })
        return _obj
