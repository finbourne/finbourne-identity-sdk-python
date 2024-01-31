# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.2774
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


class SupportAccessExpiryWithRole(object):
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
        'expiry': 'datetime',
        'permitted_role': 'str'
    }

    attribute_map = {
        'expiry': 'expiry',
        'permitted_role': 'permittedRole'
    }

    required_map = {
        'expiry': 'required',
        'permitted_role': 'required'
    }

    def __init__(self, expiry=None, permitted_role=None, local_vars_configuration=None):  # noqa: E501
        """SupportAccessExpiryWithRole - a model defined in OpenAPI"
        
        :param expiry:  DateTimeOffset at which the access will be revoked (required)
        :type expiry: datetime
        :param permitted_role:  Unique identifier for permitted role.   Use GET /identity/api/authentication/support-roles to lookup role label/code from identifier. (required)
        :type permitted_role: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._expiry = None
        self._permitted_role = None
        self.discriminator = None

        self.expiry = expiry
        self.permitted_role = permitted_role

    @property
    def expiry(self):
        """Gets the expiry of this SupportAccessExpiryWithRole.  # noqa: E501

        DateTimeOffset at which the access will be revoked  # noqa: E501

        :return: The expiry of this SupportAccessExpiryWithRole.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this SupportAccessExpiryWithRole.

        DateTimeOffset at which the access will be revoked  # noqa: E501

        :param expiry: The expiry of this SupportAccessExpiryWithRole.  # noqa: E501
        :type expiry: datetime
        """
        if self.local_vars_configuration.client_side_validation and expiry is None:  # noqa: E501
            raise ValueError("Invalid value for `expiry`, must not be `None`")  # noqa: E501

        self._expiry = expiry

    @property
    def permitted_role(self):
        """Gets the permitted_role of this SupportAccessExpiryWithRole.  # noqa: E501

        Unique identifier for permitted role.   Use GET /identity/api/authentication/support-roles to lookup role label/code from identifier.  # noqa: E501

        :return: The permitted_role of this SupportAccessExpiryWithRole.  # noqa: E501
        :rtype: str
        """
        return self._permitted_role

    @permitted_role.setter
    def permitted_role(self, permitted_role):
        """Sets the permitted_role of this SupportAccessExpiryWithRole.

        Unique identifier for permitted role.   Use GET /identity/api/authentication/support-roles to lookup role label/code from identifier.  # noqa: E501

        :param permitted_role: The permitted_role of this SupportAccessExpiryWithRole.  # noqa: E501
        :type permitted_role: str
        """
        if self.local_vars_configuration.client_side_validation and permitted_role is None:  # noqa: E501
            raise ValueError("Invalid value for `permitted_role`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                permitted_role is not None and len(permitted_role) < 1):
            raise ValueError("Invalid value for `permitted_role`, length must be greater than or equal to `1`")  # noqa: E501

        self._permitted_role = permitted_role

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
        if not isinstance(other, SupportAccessExpiryWithRole):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SupportAccessExpiryWithRole):
            return True

        return self.to_dict() != other.to_dict()
