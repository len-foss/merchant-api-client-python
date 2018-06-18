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


class MerchantReturnLineResponse(object):
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
        'quantity': 'int'
    }

    attribute_map = {
        'merchant_product_no': 'MerchantProductNo',
        'quantity': 'Quantity'
    }

    def __init__(self, merchant_product_no=None, quantity=None):  # noqa: E501
        """MerchantReturnLineResponse - a model defined in Swagger"""  # noqa: E501

        self._merchant_product_no = None
        self._quantity = None
        self.discriminator = None

        if merchant_product_no is not None:
            self.merchant_product_no = merchant_product_no
        self.quantity = quantity

    @property
    def merchant_product_no(self):
        """Gets the merchant_product_no of this MerchantReturnLineResponse.  # noqa: E501

        The unique product reference used by the Merchant (sku)  # noqa: E501

        :return: The merchant_product_no of this MerchantReturnLineResponse.  # noqa: E501
        :rtype: str
        """
        return self._merchant_product_no

    @merchant_product_no.setter
    def merchant_product_no(self, merchant_product_no):
        """Sets the merchant_product_no of this MerchantReturnLineResponse.

        The unique product reference used by the Merchant (sku)  # noqa: E501

        :param merchant_product_no: The merchant_product_no of this MerchantReturnLineResponse.  # noqa: E501
        :type: str
        """

        self._merchant_product_no = merchant_product_no

    @property
    def quantity(self):
        """Gets the quantity of this MerchantReturnLineResponse.  # noqa: E501

        Number of items of the product in this return  # noqa: E501

        :return: The quantity of this MerchantReturnLineResponse.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this MerchantReturnLineResponse.

        Number of items of the product in this return  # noqa: E501

        :param quantity: The quantity of this MerchantReturnLineResponse.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

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
        if not isinstance(other, MerchantReturnLineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
