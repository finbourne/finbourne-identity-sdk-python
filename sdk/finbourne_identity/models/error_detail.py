# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.2243
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


class ErrorDetail(object):
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
        'id': 'str',
        'type': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'detail': 'detail'
    }

    required_map = {
        'id': 'optional',
        'type': 'optional',
        'detail': 'optional'
    }

    def __init__(self, id=None, type=None, detail=None, local_vars_configuration=None):  # noqa: E501
        """ErrorDetail - a model defined in OpenAPI"
        
        :param id:  Id of the entity this error relates to
        :type id: str
        :param type:  Error type
        :type type: str
        :param detail:  Human readable description of the error
        :type detail: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._detail = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.detail = detail

    @property
    def id(self):
        """Gets the id of this ErrorDetail.  # noqa: E501

        Id of the entity this error relates to  # noqa: E501

        :return: The id of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ErrorDetail.

        Id of the entity this error relates to  # noqa: E501

        :param id: The id of this ErrorDetail.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ErrorDetail.  # noqa: E501

        Error type  # noqa: E501

        :return: The type of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ErrorDetail.

        Error type  # noqa: E501

        :param type: The type of this ErrorDetail.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def detail(self):
        """Gets the detail of this ErrorDetail.  # noqa: E501

        Human readable description of the error  # noqa: E501

        :return: The detail of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ErrorDetail.

        Human readable description of the error  # noqa: E501

        :param detail: The detail of this ErrorDetail.  # noqa: E501
        :type detail: str
        """

        self._detail = detail

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
        if not isinstance(other, ErrorDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorDetail):
            return True

        return self.to_dict() != other.to_dict()
