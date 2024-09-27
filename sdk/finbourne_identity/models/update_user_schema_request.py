# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.3048
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from finbourne_identity.configuration import Configuration


class UpdateUserSchemaRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'alternative_user_ids': 'list[UserSchemaProperty]'
    }

    attribute_map = {
        'alternative_user_ids': 'alternativeUserIds'
    }

    required_map = {
        'alternative_user_ids': 'required'
    }

    def __init__(self, alternative_user_ids=None, local_vars_configuration=None):  # noqa: E501
        """UpdateUserSchemaRequest - a model defined in OpenAPI"
        
        :param alternative_user_ids:  (required)
        :type alternative_user_ids: list[finbourne_identity.UserSchemaProperty]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._alternative_user_ids = None
        self.discriminator = None

        self.alternative_user_ids = alternative_user_ids

    @property
    def alternative_user_ids(self):
        """Gets the alternative_user_ids of this UpdateUserSchemaRequest.  # noqa: E501


        :return: The alternative_user_ids of this UpdateUserSchemaRequest.  # noqa: E501
        :rtype: list[finbourne_identity.UserSchemaProperty]
        """
        return self._alternative_user_ids

    @alternative_user_ids.setter
    def alternative_user_ids(self, alternative_user_ids):
        """Sets the alternative_user_ids of this UpdateUserSchemaRequest.


        :param alternative_user_ids: The alternative_user_ids of this UpdateUserSchemaRequest.  # noqa: E501
        :type alternative_user_ids: list[finbourne_identity.UserSchemaProperty]
        """
        if self.local_vars_configuration.client_side_validation and alternative_user_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `alternative_user_ids`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                alternative_user_ids is not None and len(alternative_user_ids) > 10):
            raise ValueError("Invalid value for `alternative_user_ids`, number of items must be less than or equal to `10`")  # noqa: E501

        self._alternative_user_ids = alternative_user_ids

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateUserSchemaRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateUserSchemaRequest):
            return True

        return self.to_dict() != other.to_dict()
