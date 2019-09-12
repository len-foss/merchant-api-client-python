# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from channelengine_merchant_api_client.api_client import ApiClient


class ProductBundleApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def product_bundle_get_by_filter(self, **kwargs):  # noqa: E501
        """Get product bundles.  You can get the full product information on bundles from the regular /products endpoint.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_bundle_get_by_filter(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search: Search product(s) by Name, MerchantProductNo, Ean or Brand      This search is applied to the result after applying the other filters.
        :param list[str] ean_list: Search products by submitting a list of EAN's
        :param list[str] merchant_product_no_list: Search products by submitting a list of MerchantProductNo's
        :param int page: The page to filter on. Starts at 1.
        :return: CollectionOfMerchantProductBundleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.product_bundle_get_by_filter_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.product_bundle_get_by_filter_with_http_info(**kwargs)  # noqa: E501
            return data

    def product_bundle_get_by_filter_with_http_info(self, **kwargs):  # noqa: E501
        """Get product bundles.  You can get the full product information on bundles from the regular /products endpoint.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.product_bundle_get_by_filter_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search: Search product(s) by Name, MerchantProductNo, Ean or Brand      This search is applied to the result after applying the other filters.
        :param list[str] ean_list: Search products by submitting a list of EAN's
        :param list[str] merchant_product_no_list: Search products by submitting a list of MerchantProductNo's
        :param int page: The page to filter on. Starts at 1.
        :return: CollectionOfMerchantProductBundleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'ean_list', 'merchant_product_no_list', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method product_bundle_get_by_filter" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'ean_list' in params:
            query_params.append(('eanList', params['ean_list']))  # noqa: E501
            collection_formats['eanList'] = 'multi'  # noqa: E501
        if 'merchant_product_no_list' in params:
            query_params.append(('merchantProductNoList', params['merchant_product_no_list']))  # noqa: E501
            collection_formats['merchantProductNoList'] = 'multi'  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/productbundles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionOfMerchantProductBundleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
