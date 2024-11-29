# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic.v1 import validate_arguments, ValidationError
from typing import overload, Optional, Union, Awaitable

from typing_extensions import Annotated
from pydantic.v1 import Field, constr, validator

from typing import List

from finbourne_identity.models.create_network_zone_request import CreateNetworkZoneRequest
from finbourne_identity.models.network_zone_definition_response import NetworkZoneDefinitionResponse
from finbourne_identity.models.update_network_zone_request import UpdateNetworkZoneRequest

from finbourne_identity.api_client import ApiClient
from finbourne_identity.api_response import ApiResponse
from finbourne_identity.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from finbourne_identity.extensions.configuration_options import ConfigurationOptions


class NetworkZonesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def create_network_zone(self, create_network_zone_request : Annotated[CreateNetworkZoneRequest, Field(..., description="The details of the network zone to define")], **kwargs) -> NetworkZoneDefinitionResponse:  # noqa: E501
        ...

    @overload
    def create_network_zone(self, create_network_zone_request : Annotated[CreateNetworkZoneRequest, Field(..., description="The details of the network zone to define")], async_req: Optional[bool]=True, **kwargs) -> NetworkZoneDefinitionResponse:  # noqa: E501
        ...

    @validate_arguments
    def create_network_zone(self, create_network_zone_request : Annotated[CreateNetworkZoneRequest, Field(..., description="The details of the network zone to define")], async_req: Optional[bool]=None, **kwargs) -> Union[NetworkZoneDefinitionResponse, Awaitable[NetworkZoneDefinitionResponse]]:  # noqa: E501
        """[BETA] CreateNetworkZone: Creates a network zone  # noqa: E501

        By default, the network zone will have its hierarchy set to last on creation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_network_zone(create_network_zone_request, async_req=True)
        >>> result = thread.get()

        :param create_network_zone_request: The details of the network zone to define (required)
        :type create_network_zone_request: CreateNetworkZoneRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NetworkZoneDefinitionResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_network_zone_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.create_network_zone_with_http_info(create_network_zone_request, **kwargs)  # noqa: E501

    @validate_arguments
    def create_network_zone_with_http_info(self, create_network_zone_request : Annotated[CreateNetworkZoneRequest, Field(..., description="The details of the network zone to define")], **kwargs) -> ApiResponse:  # noqa: E501
        """[BETA] CreateNetworkZone: Creates a network zone  # noqa: E501

        By default, the network zone will have its hierarchy set to last on creation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_network_zone_with_http_info(create_network_zone_request, async_req=True)
        >>> result = thread.get()

        :param create_network_zone_request: The details of the network zone to define (required)
        :type create_network_zone_request: CreateNetworkZoneRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NetworkZoneDefinitionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'create_network_zone_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_network_zone" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['create_network_zone_request'] is not None:
            _body_params = _params['create_network_zone_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '201': "NetworkZoneDefinitionResponse",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/networkzones', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def delete_network_zone(self, code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The unique identifier of the network zone to delete")], **kwargs) -> None:  # noqa: E501
        ...

    @overload
    def delete_network_zone(self, code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The unique identifier of the network zone to delete")], async_req: Optional[bool]=True, **kwargs) -> None:  # noqa: E501
        ...

    @validate_arguments
    def delete_network_zone(self, code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The unique identifier of the network zone to delete")], async_req: Optional[bool]=None, **kwargs) -> Union[None, Awaitable[None]]:  # noqa: E501
        """[BETA] DeleteNetworkZone: Deletes a network zone  # noqa: E501

        Will return a success if network zone already deleted  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_network_zone(code, async_req=True)
        >>> result = thread.get()

        :param code: The unique identifier of the network zone to delete (required)
        :type code: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the delete_network_zone_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.delete_network_zone_with_http_info(code, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_network_zone_with_http_info(self, code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The unique identifier of the network zone to delete")], **kwargs) -> ApiResponse:  # noqa: E501
        """[BETA] DeleteNetworkZone: Deletes a network zone  # noqa: E501

        Will return a success if network zone already deleted  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_network_zone_with_http_info(code, async_req=True)
        >>> result = thread.get()

        :param code: The unique identifier of the network zone to delete (required)
        :type code: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'code'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_network_zone" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['code']:
            _path_params['code'] = _params['code']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/networkzones/{code}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def get_network_zone(self, code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The unique identifier of the network zone")], **kwargs) -> NetworkZoneDefinitionResponse:  # noqa: E501
        ...

    @overload
    def get_network_zone(self, code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The unique identifier of the network zone")], async_req: Optional[bool]=True, **kwargs) -> NetworkZoneDefinitionResponse:  # noqa: E501
        ...

    @validate_arguments
    def get_network_zone(self, code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The unique identifier of the network zone")], async_req: Optional[bool]=None, **kwargs) -> Union[NetworkZoneDefinitionResponse, Awaitable[NetworkZoneDefinitionResponse]]:  # noqa: E501
        """[BETA] GetNetworkZone: Retrieve a Network Zone  # noqa: E501

        Retrieves a Network Zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_network_zone(code, async_req=True)
        >>> result = thread.get()

        :param code: The unique identifier of the network zone (required)
        :type code: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NetworkZoneDefinitionResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_network_zone_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_network_zone_with_http_info(code, **kwargs)  # noqa: E501

    @validate_arguments
    def get_network_zone_with_http_info(self, code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The unique identifier of the network zone")], **kwargs) -> ApiResponse:  # noqa: E501
        """[BETA] GetNetworkZone: Retrieve a Network Zone  # noqa: E501

        Retrieves a Network Zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_network_zone_with_http_info(code, async_req=True)
        >>> result = thread.get()

        :param code: The unique identifier of the network zone (required)
        :type code: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NetworkZoneDefinitionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'code'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_network_zone" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['code']:
            _path_params['code'] = _params['code']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "NetworkZoneDefinitionResponse",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/networkzones/{code}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def list_network_zones(self, **kwargs) -> List[NetworkZoneDefinitionResponse]:  # noqa: E501
        ...

    @overload
    def list_network_zones(self, async_req: Optional[bool]=True, **kwargs) -> List[NetworkZoneDefinitionResponse]:  # noqa: E501
        ...

    @validate_arguments
    def list_network_zones(self, async_req: Optional[bool]=None, **kwargs) -> Union[List[NetworkZoneDefinitionResponse], Awaitable[List[NetworkZoneDefinitionResponse]]]:  # noqa: E501
        """[BETA] ListNetworkZones: Lists all network zones for a domain  # noqa: E501

        Lists all network zones for a domain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_network_zones(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[NetworkZoneDefinitionResponse]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_network_zones_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.list_network_zones_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def list_network_zones_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """[BETA] ListNetworkZones: Lists all network zones for a domain  # noqa: E501

        Lists all network zones for a domain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_network_zones_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[NetworkZoneDefinitionResponse], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_network_zones" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "List[NetworkZoneDefinitionResponse]",
        }

        return self.api_client.call_api(
            '/api/networkzones', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def update_network_zone(self, code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The unique identifier of the network zone")], update_network_zone_request : Annotated[UpdateNetworkZoneRequest, Field(..., description="The updated definition of the network zone")], **kwargs) -> NetworkZoneDefinitionResponse:  # noqa: E501
        ...

    @overload
    def update_network_zone(self, code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The unique identifier of the network zone")], update_network_zone_request : Annotated[UpdateNetworkZoneRequest, Field(..., description="The updated definition of the network zone")], async_req: Optional[bool]=True, **kwargs) -> NetworkZoneDefinitionResponse:  # noqa: E501
        ...

    @validate_arguments
    def update_network_zone(self, code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The unique identifier of the network zone")], update_network_zone_request : Annotated[UpdateNetworkZoneRequest, Field(..., description="The updated definition of the network zone")], async_req: Optional[bool]=None, **kwargs) -> Union[NetworkZoneDefinitionResponse, Awaitable[NetworkZoneDefinitionResponse]]:  # noqa: E501
        """[BETA] UpdateNetworkZone: Updates an existing network zone  # noqa: E501

        Updates an existing network zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_network_zone(code, update_network_zone_request, async_req=True)
        >>> result = thread.get()

        :param code: The unique identifier of the network zone (required)
        :type code: str
        :param update_network_zone_request: The updated definition of the network zone (required)
        :type update_network_zone_request: UpdateNetworkZoneRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NetworkZoneDefinitionResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the update_network_zone_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.update_network_zone_with_http_info(code, update_network_zone_request, **kwargs)  # noqa: E501

    @validate_arguments
    def update_network_zone_with_http_info(self, code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The unique identifier of the network zone")], update_network_zone_request : Annotated[UpdateNetworkZoneRequest, Field(..., description="The updated definition of the network zone")], **kwargs) -> ApiResponse:  # noqa: E501
        """[BETA] UpdateNetworkZone: Updates an existing network zone  # noqa: E501

        Updates an existing network zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_network_zone_with_http_info(code, update_network_zone_request, async_req=True)
        >>> result = thread.get()

        :param code: The unique identifier of the network zone (required)
        :type code: str
        :param update_network_zone_request: The updated definition of the network zone (required)
        :type update_network_zone_request: UpdateNetworkZoneRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NetworkZoneDefinitionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'code',
            'update_network_zone_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_network_zone" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['code']:
            _path_params['code'] = _params['code']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['update_network_zone_request'] is not None:
            _body_params = _params['update_network_zone_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "NetworkZoneDefinitionResponse",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/networkzones/{code}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
