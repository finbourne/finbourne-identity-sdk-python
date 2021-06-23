# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1254
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from finbourne_identity.api_client import ApiClient
from finbourne_identity.exceptions import (
    ApiTypeError,
    ApiValueError
)


class DomainsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_domain(self, code, create_domain_request, **kwargs):  # noqa: E501
        """Create Domain  # noqa: E501

        Creates a Domain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_domain(code, create_domain_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str code: The verification code necessary to create domains (required)
        :param CreateDomainRequest create_domain_request: The definition of the domain (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DomainResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_domain_with_http_info(code, create_domain_request, **kwargs)  # noqa: E501

    def create_domain_with_http_info(self, code, create_domain_request, **kwargs):  # noqa: E501
        """Create Domain  # noqa: E501

        Creates a Domain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_domain_with_http_info(code, create_domain_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str code: The verification code necessary to create domains (required)
        :param CreateDomainRequest create_domain_request: The definition of the domain (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DomainResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['code', 'create_domain_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_domain" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `create_domain`")  # noqa: E501
        # verify the required parameter 'create_domain_request' is set
        if ('create_domain_request' not in local_var_params or
                local_var_params['create_domain_request'] is None):
            raise ApiValueError("Missing the required parameter `create_domain_request` when calling `create_domain`")  # noqa: E501

        if ('code' in local_var_params and
                len(local_var_params['code']) > 2147483647):
            raise ApiValueError("Invalid value for parameter `code` when calling `create_domain`, length must be less than or equal to `2147483647`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) < 1):
            raise ApiValueError("Invalid value for parameter `code` when calling `create_domain`, length must be greater than or equal to `1`")  # noqa: E501
        if 'code' in local_var_params and not re.search(r'^[\s\S]*$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `create_domain`, must conform to the pattern `/^[\s\S]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'code' in local_var_params:
            query_params.append(('code', local_var_params['code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_domain_request' in local_var_params:
            body_params = local_var_params['create_domain_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.1254'

        return self.api_client.call_api(
            '/api/domains', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_agreement(self, agreement, **kwargs):  # noqa: E501
        """Get Agreement  # noqa: E501

        Check whether the domain has signed a specific agreement  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_agreement(agreement, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str agreement: Name of the agreement (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_agreement_with_http_info(agreement, **kwargs)  # noqa: E501

    def get_agreement_with_http_info(self, agreement, **kwargs):  # noqa: E501
        """Get Agreement  # noqa: E501

        Check whether the domain has signed a specific agreement  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_agreement_with_http_info(agreement, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str agreement: Name of the agreement (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(bool, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['agreement']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_agreement" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'agreement' is set
        if ('agreement' not in local_var_params or
                local_var_params['agreement'] is None):
            raise ApiValueError("Missing the required parameter `agreement` when calling `get_agreement`")  # noqa: E501

        if ('agreement' in local_var_params and
                len(local_var_params['agreement']) > 100):
            raise ApiValueError("Invalid value for parameter `agreement` when calling `get_agreement`, length must be less than or equal to `100`")  # noqa: E501
        if ('agreement' in local_var_params and
                len(local_var_params['agreement']) < 0):
            raise ApiValueError("Invalid value for parameter `agreement` when calling `get_agreement`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'agreement' in local_var_params:
            path_params['agreement'] = local_var_params['agreement']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.1254'

        return self.api_client.call_api(
            '/api/domains/me/agreements/{agreement}', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_my_domain(self, **kwargs):  # noqa: E501
        """Get current Domain  # noqa: E501

        Gets the Domain of the requesting User  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_my_domain(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DomainResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_my_domain_with_http_info(**kwargs)  # noqa: E501

    def get_my_domain_with_http_info(self, **kwargs):  # noqa: E501
        """Get current Domain  # noqa: E501

        Gets the Domain of the requesting User  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_my_domain_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DomainResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_my_domain" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.1254'

        return self.api_client.call_api(
            '/api/domains/me', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_agreements(self, **kwargs):  # noqa: E501
        """List Agreements  # noqa: E501

        Lists the signed agreements for the current domain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_agreements(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: dict(str, AgreementResponse)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_agreements_with_http_info(**kwargs)  # noqa: E501

    def list_agreements_with_http_info(self, **kwargs):  # noqa: E501
        """List Agreements  # noqa: E501

        Lists the signed agreements for the current domain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_agreements_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(dict(str, AgreementResponse), status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_agreements" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.1254'

        return self.api_client.call_api(
            '/api/domains/me/agreements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, AgreementResponse)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sign_agreement(self, agreement, **kwargs):  # noqa: E501
        """Sign Agreement  # noqa: E501

        Signs a specified agreement. Only the owner of a domain can sign an agreement  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sign_agreement(agreement, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str agreement: Name of the agreement being signed (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AgreementResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.sign_agreement_with_http_info(agreement, **kwargs)  # noqa: E501

    def sign_agreement_with_http_info(self, agreement, **kwargs):  # noqa: E501
        """Sign Agreement  # noqa: E501

        Signs a specified agreement. Only the owner of a domain can sign an agreement  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sign_agreement_with_http_info(agreement, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str agreement: Name of the agreement being signed (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AgreementResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['agreement']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sign_agreement" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'agreement' is set
        if ('agreement' not in local_var_params or
                local_var_params['agreement'] is None):
            raise ApiValueError("Missing the required parameter `agreement` when calling `sign_agreement`")  # noqa: E501

        if ('agreement' in local_var_params and
                len(local_var_params['agreement']) > 100):
            raise ApiValueError("Invalid value for parameter `agreement` when calling `sign_agreement`, length must be less than or equal to `100`")  # noqa: E501
        if ('agreement' in local_var_params and
                len(local_var_params['agreement']) < 0):
            raise ApiValueError("Invalid value for parameter `agreement` when calling `sign_agreement`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'agreement' in local_var_params:
            path_params['agreement'] = local_var_params['agreement']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.1254'

        return self.api_client.call_api(
            '/api/domains/me/agreements/{agreement}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AgreementResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
