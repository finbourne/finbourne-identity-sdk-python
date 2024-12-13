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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator
from finbourne_identity.models.role_id import RoleId

class CreateUserRequest(BaseModel):
    """
    Details necessary for creating a new user  # noqa: E501
    """
    first_name: constr(strict=True, max_length=50, min_length=1) = Field(..., alias="firstName", description="The first name of the user")
    last_name: constr(strict=True, max_length=50, min_length=2) = Field(..., alias="lastName", description="The last name of the user")
    email_address: constr(strict=True, max_length=80, min_length=5) = Field(..., alias="emailAddress", description="The user's email address - to which the account validation email will be sent. For user accounts  this should exactly match the Login.")
    second_email_address: Optional[constr(strict=True, max_length=80, min_length=5)] = Field(None, alias="secondEmailAddress", description="The user's second email address. Only allowed for Service users")
    login: constr(strict=True, max_length=80, min_length=5) = Field(..., description="The user's login username, in the form of an email address, which must be unique within the system.  For user accounts this should exactly match the user's email address.")
    alternative_user_ids: Optional[Dict[str, StrictStr]] = Field(None, alias="alternativeUserIds")
    roles: Optional[conlist(RoleId, max_items=20)] = Field(None, description="Optional. Any known roles the user should be created with.")
    type: constr(strict=True, max_length=20, min_length=1) = Field(..., description="The type of user (e.g. Personal or Service)")
    __properties = ["firstName", "lastName", "emailAddress", "secondEmailAddress", "login", "alternativeUserIds", "roles", "type"]

    @validator('first_name')
    def first_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

    @validator('last_name')
    def last_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

    @validator('type')
    def type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z]*$/")
        return value

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
    def from_json(cls, json_str: str) -> CreateUserRequest:
        """Create an instance of CreateUserRequest from a JSON string"""
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
    def from_dict(cls, obj: dict) -> CreateUserRequest:
        """Create an instance of CreateUserRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateUserRequest.parse_obj(obj)

        _obj = CreateUserRequest.parse_obj({
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "email_address": obj.get("emailAddress"),
            "second_email_address": obj.get("secondEmailAddress"),
            "login": obj.get("login"),
            "alternative_user_ids": obj.get("alternativeUserIds"),
            "roles": [RoleId.from_dict(_item) for _item in obj.get("roles")] if obj.get("roles") is not None else None,
            "type": obj.get("type")
        })
        return _obj
