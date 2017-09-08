# coding: utf-8

"""
    ChannelEngine API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ShipmentApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def shipment_create(self, model, **kwargs):
        """
        Merchant: Create Shipment
        For merchants.    Mark (part of) an order as shipped.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.shipment_create(model, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MerchantShipmentRequest model:  (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.shipment_create_with_http_info(model, **kwargs)
        else:
            (data) = self.shipment_create_with_http_info(model, **kwargs)
            return data

    def shipment_create_with_http_info(self, model, **kwargs):
        """
        Merchant: Create Shipment
        For merchants.    Mark (part of) an order as shipped.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.shipment_create_with_http_info(model, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MerchantShipmentRequest model:  (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method shipment_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model' is set
        if ('model' not in params) or (params['model'] is None):
            raise ValueError("Missing the required parameter `model` when calling `shipment_create`")


        collection_formats = {}

        resource_path = '/v2/shipments'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'model' in params:
            body_params = params['model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ApiResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def shipment_index(self, created_since, **kwargs):
        """
        Channel: Get Shipments
        For channels.    Gets all shipments created since the supplied date.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.shipment_index(created_since, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime created_since:  (required)
        :return: CollectionOfChannelShipmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.shipment_index_with_http_info(created_since, **kwargs)
        else:
            (data) = self.shipment_index_with_http_info(created_since, **kwargs)
            return data

    def shipment_index_with_http_info(self, created_since, **kwargs):
        """
        Channel: Get Shipments
        For channels.    Gets all shipments created since the supplied date.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.shipment_index_with_http_info(created_since, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime created_since:  (required)
        :return: CollectionOfChannelShipmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['created_since']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method shipment_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'created_since' is set
        if ('created_since' not in params) or (params['created_since'] is None):
            raise ValueError("Missing the required parameter `created_since` when calling `shipment_index`")


        collection_formats = {}

        resource_path = '/v2/shipments'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'created_since' in params:
            query_params['createdSince'] = params['created_since']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json'])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CollectionOfChannelShipmentResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def shipment_update(self, merchant_shipment_no, model, **kwargs):
        """
        Merchant: Update Shipment
        For merchants.    Update an existing shipment with tracking information
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.shipment_update(merchant_shipment_no, model, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str merchant_shipment_no: The merchant's shipment reference (required)
        :param MerchantShipmentTrackingRequest model: The updated tracking information (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.shipment_update_with_http_info(merchant_shipment_no, model, **kwargs)
        else:
            (data) = self.shipment_update_with_http_info(merchant_shipment_no, model, **kwargs)
            return data

    def shipment_update_with_http_info(self, merchant_shipment_no, model, **kwargs):
        """
        Merchant: Update Shipment
        For merchants.    Update an existing shipment with tracking information
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.shipment_update_with_http_info(merchant_shipment_no, model, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str merchant_shipment_no: The merchant's shipment reference (required)
        :param MerchantShipmentTrackingRequest model: The updated tracking information (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_shipment_no', 'model']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method shipment_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'merchant_shipment_no' is set
        if ('merchant_shipment_no' not in params) or (params['merchant_shipment_no'] is None):
            raise ValueError("Missing the required parameter `merchant_shipment_no` when calling `shipment_update`")
        # verify the required parameter 'model' is set
        if ('model' not in params) or (params['model'] is None):
            raise ValueError("Missing the required parameter `model` when calling `shipment_update`")


        collection_formats = {}

        resource_path = '/v2/shipments/{merchantShipmentNo}'.replace('{format}', 'json')
        path_params = {}
        if 'merchant_shipment_no' in params:
            path_params['merchantShipmentNo'] = params['merchant_shipment_no']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'model' in params:
            body_params = params['model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ApiResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
