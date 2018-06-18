# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MerchantStockPriceUpdateRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'merchant_product_no': 'str',
        'stock': 'int',
        'price': 'float'
    }

    attribute_map = {
        'merchant_product_no': 'MerchantProductNo',
        'stock': 'Stock',
        'price': 'Price'
    }

    def __init__(self, merchant_product_no=None, stock=None, price=None):  # noqa: E501
        """MerchantStockPriceUpdateRequest - a model defined in Swagger"""  # noqa: E501

        self._merchant_product_no = None
        self._stock = None
        self._price = None
        self.discriminator = None

        self.merchant_product_no = merchant_product_no
        if stock is not None:
            self.stock = stock
        if price is not None:
            self.price = price

    @property
    def merchant_product_no(self):
        """Gets the merchant_product_no of this MerchantStockPriceUpdateRequest.  # noqa: E501

        The unique product reference used by the Merchant (sku)  # noqa: E501

        :return: The merchant_product_no of this MerchantStockPriceUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._merchant_product_no

    @merchant_product_no.setter
    def merchant_product_no(self, merchant_product_no):
        """Sets the merchant_product_no of this MerchantStockPriceUpdateRequest.

        The unique product reference used by the Merchant (sku)  # noqa: E501

        :param merchant_product_no: The merchant_product_no of this MerchantStockPriceUpdateRequest.  # noqa: E501
        :type: str
        """
        if merchant_product_no is None:
            raise ValueError("Invalid value for `merchant_product_no`, must not be `None`")  # noqa: E501

        self._merchant_product_no = merchant_product_no

    @property
    def stock(self):
        """Gets the stock of this MerchantStockPriceUpdateRequest.  # noqa: E501

        The stock of the product. Should not be negative  # noqa: E501

        :return: The stock of this MerchantStockPriceUpdateRequest.  # noqa: E501
        :rtype: int
        """
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Sets the stock of this MerchantStockPriceUpdateRequest.

        The stock of the product. Should not be negative  # noqa: E501

        :param stock: The stock of this MerchantStockPriceUpdateRequest.  # noqa: E501
        :type: int
        """

        self._stock = stock

    @property
    def price(self):
        """Gets the price of this MerchantStockPriceUpdateRequest.  # noqa: E501

        The price of the product. Should not be negative  # noqa: E501

        :return: The price of this MerchantStockPriceUpdateRequest.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this MerchantStockPriceUpdateRequest.

        The price of the product. Should not be negative  # noqa: E501

        :param price: The price of this MerchantStockPriceUpdateRequest.  # noqa: E501
        :type: float
        """

        self._price = price

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MerchantStockPriceUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
