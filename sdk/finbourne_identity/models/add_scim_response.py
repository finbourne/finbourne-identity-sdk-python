# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.2353
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


class AddScimResponse(object):
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
        'base_url': 'str',
        'api_token': 'str'
    }

    attribute_map = {
        'base_url': 'baseUrl',
        'api_token': 'apiToken'
    }

    required_map = {
        'base_url': 'optional',
        'api_token': 'optional'
    }

    def __init__(self, base_url=None, api_token=None, local_vars_configuration=None):  # noqa: E501
        """AddScimResponse - a model defined in OpenAPI"
        
        :param base_url: 
        :type base_url: str
        :param api_token: 
        :type api_token: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._base_url = None
        self._api_token = None
        self.discriminator = None

        self.base_url = base_url
        self.api_token = api_token

    @property
    def base_url(self):
        """Gets the base_url of this AddScimResponse.  # noqa: E501


        :return: The base_url of this AddScimResponse.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this AddScimResponse.


        :param base_url: The base_url of this AddScimResponse.  # noqa: E501
        :type base_url: str
        """

        self._base_url = base_url

    @property
    def api_token(self):
        """Gets the api_token of this AddScimResponse.  # noqa: E501


        :return: The api_token of this AddScimResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token of this AddScimResponse.


        :param api_token: The api_token of this AddScimResponse.  # noqa: E501
        :type api_token: str
        """

        self._api_token = api_token

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
        if not isinstance(other, AddScimResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddScimResponse):
            return True

        return self.to_dict() != other.to_dict()
