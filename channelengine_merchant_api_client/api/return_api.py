# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    The version of the OpenAPI document: 2.9.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from channelengine_merchant_api_client.api_client import ApiClient
from channelengine_merchant_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ReturnApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def return_declare_for_merchant(self, **kwargs):  # noqa: E501
        """Create Return.  # noqa: E501

        Mark (part of) an order as returned by the customer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.return_declare_for_merchant(async_req=True)
        >>> result = thread.get()

        :param merchant_return_request:
        :type merchant_return_request: MerchantReturnRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.return_declare_for_merchant_with_http_info(**kwargs)  # noqa: E501

    def return_declare_for_merchant_with_http_info(self, **kwargs):  # noqa: E501
        """Create Return.  # noqa: E501

        Mark (part of) an order as returned by the customer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.return_declare_for_merchant_with_http_info(async_req=True)
        >>> result = thread.get()

        :param merchant_return_request:
        :type merchant_return_request: MerchantReturnRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ApiResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'merchant_return_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method return_declare_for_merchant" % key
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
        if 'merchant_return_request' in local_var_params:
            body_params = local_var_params['merchant_return_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/returns/merchant', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def return_get_by_merchant_order_no(self, merchant_order_no, **kwargs):  # noqa: E501
        """Get Return.  # noqa: E501

        Retrieve returns based on the supplied merchant order number. May return more than 1 result.<br />This call is supposed to be used by merchants. Channels should use the 'GET /v2/returns/channel'<br />call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.return_get_by_merchant_order_no(merchant_order_no, async_req=True)
        >>> result = thread.get()

        :param merchant_order_no: (required)
        :type merchant_order_no: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CollectionOfMerchantSingleOrderReturnResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.return_get_by_merchant_order_no_with_http_info(merchant_order_no, **kwargs)  # noqa: E501

    def return_get_by_merchant_order_no_with_http_info(self, merchant_order_no, **kwargs):  # noqa: E501
        """Get Return.  # noqa: E501

        Retrieve returns based on the supplied merchant order number. May return more than 1 result.<br />This call is supposed to be used by merchants. Channels should use the 'GET /v2/returns/channel'<br />call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.return_get_by_merchant_order_no_with_http_info(merchant_order_no, async_req=True)
        >>> result = thread.get()

        :param merchant_order_no: (required)
        :type merchant_order_no: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CollectionOfMerchantSingleOrderReturnResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'merchant_order_no'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method return_get_by_merchant_order_no" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'merchant_order_no' in local_var_params:
            path_params['merchantOrderNo'] = local_var_params['merchant_order_no']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/returns/merchant/{merchantOrderNo}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionOfMerchantSingleOrderReturnResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def return_get_declared_by_channel(self, **kwargs):  # noqa: E501
        """Get Returns.  # noqa: E501

        Get all returns created by the channel. This call is supposed<br />to be used by merchants. Channels should use the 'GET /v2/returns/channel'<br />call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.return_get_declared_by_channel(async_req=True)
        >>> result = thread.get()

        :param merchant_order_nos: Filter on unique order reference used by the merchant.
        :type merchant_order_nos: list[str]
        :param created_since: Deprecated, please use FromDate instead.
        :type created_since: datetime
        :param statuses: Return status(es) to filter on.
        :type statuses: list[ReturnStatus]
        :param reasons: Return reason(s) to filter on.
        :type reasons: list[ReturnReason]
        :param from_date: Filter on the creation date, starting from this date. This date is inclusive.
        :type from_date: datetime
        :param to_date: Filter on the creation date, until this date. This date is exclusive.
        :type to_date: datetime
        :param page: The page to filter on. Starts at 1.
        :type page: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CollectionOfMerchantReturnResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.return_get_declared_by_channel_with_http_info(**kwargs)  # noqa: E501

    def return_get_declared_by_channel_with_http_info(self, **kwargs):  # noqa: E501
        """Get Returns.  # noqa: E501

        Get all returns created by the channel. This call is supposed<br />to be used by merchants. Channels should use the 'GET /v2/returns/channel'<br />call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.return_get_declared_by_channel_with_http_info(async_req=True)
        >>> result = thread.get()

        :param merchant_order_nos: Filter on unique order reference used by the merchant.
        :type merchant_order_nos: list[str]
        :param created_since: Deprecated, please use FromDate instead.
        :type created_since: datetime
        :param statuses: Return status(es) to filter on.
        :type statuses: list[ReturnStatus]
        :param reasons: Return reason(s) to filter on.
        :type reasons: list[ReturnReason]
        :param from_date: Filter on the creation date, starting from this date. This date is inclusive.
        :type from_date: datetime
        :param to_date: Filter on the creation date, until this date. This date is exclusive.
        :type to_date: datetime
        :param page: The page to filter on. Starts at 1.
        :type page: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CollectionOfMerchantReturnResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'merchant_order_nos',
            'created_since',
            'statuses',
            'reasons',
            'from_date',
            'to_date',
            'page'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method return_get_declared_by_channel" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'merchant_order_nos' in local_var_params and local_var_params['merchant_order_nos'] is not None:  # noqa: E501
            query_params.append(('merchantOrderNos', local_var_params['merchant_order_nos']))  # noqa: E501
            collection_formats['merchantOrderNos'] = 'multi'  # noqa: E501
        if 'created_since' in local_var_params and local_var_params['created_since'] is not None:  # noqa: E501
            query_params.append(('createdSince', local_var_params['created_since']))  # noqa: E501
        if 'statuses' in local_var_params and local_var_params['statuses'] is not None:  # noqa: E501
            query_params.append(('statuses', local_var_params['statuses']))  # noqa: E501
            collection_formats['statuses'] = 'multi'  # noqa: E501
        if 'reasons' in local_var_params and local_var_params['reasons'] is not None:  # noqa: E501
            query_params.append(('reasons', local_var_params['reasons']))  # noqa: E501
            collection_formats['reasons'] = 'multi'  # noqa: E501
        if 'from_date' in local_var_params and local_var_params['from_date'] is not None:  # noqa: E501
            query_params.append(('fromDate', local_var_params['from_date']))  # noqa: E501
        if 'to_date' in local_var_params and local_var_params['to_date'] is not None:  # noqa: E501
            query_params.append(('toDate', local_var_params['to_date']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/returns/merchant', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionOfMerchantReturnResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def return_get_unhandled(self, **kwargs):  # noqa: E501
        """Get Unhandled Returns.  # noqa: E501

        Get all new / unhandled returns created by channels. This call is supposed<br />to be used by merchants. Channels should use the 'GET /v2/returns/channel'<br />call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.return_get_unhandled(async_req=True)
        >>> result = thread.get()

        :param page: The page to filter on. Starts at 1.
        :type page: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CollectionOfMerchantReturnResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.return_get_unhandled_with_http_info(**kwargs)  # noqa: E501

    def return_get_unhandled_with_http_info(self, **kwargs):  # noqa: E501
        """Get Unhandled Returns.  # noqa: E501

        Get all new / unhandled returns created by channels. This call is supposed<br />to be used by merchants. Channels should use the 'GET /v2/returns/channel'<br />call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.return_get_unhandled_with_http_info(async_req=True)
        >>> result = thread.get()

        :param page: The page to filter on. Starts at 1.
        :type page: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CollectionOfMerchantReturnResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'page'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method return_get_unhandled" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/returns/merchant/new', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionOfMerchantReturnResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def return_update_for_merchant(self, **kwargs):  # noqa: E501
        """Mark a return as received.  # noqa: E501

        Mark a return as received.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.return_update_for_merchant(async_req=True)
        >>> result = thread.get()

        :param merchant_return_update_request:
        :type merchant_return_update_request: MerchantReturnUpdateRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.return_update_for_merchant_with_http_info(**kwargs)  # noqa: E501

    def return_update_for_merchant_with_http_info(self, **kwargs):  # noqa: E501
        """Mark a return as received.  # noqa: E501

        Mark a return as received.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.return_update_for_merchant_with_http_info(async_req=True)
        >>> result = thread.get()

        :param merchant_return_update_request:
        :type merchant_return_update_request: MerchantReturnUpdateRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ApiResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'merchant_return_update_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method return_update_for_merchant" % key
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
        if 'merchant_return_update_request' in local_var_params:
            body_params = local_var_params['merchant_return_update_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/returns', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
