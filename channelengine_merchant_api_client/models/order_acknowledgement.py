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


class OrderAcknowledgement(object):
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
        'merchant_order_no': 'str',
        'order_id': 'int'
    }

    attribute_map = {
        'merchant_order_no': 'MerchantOrderNo',
        'order_id': 'OrderId'
    }

    def __init__(self, merchant_order_no=None, order_id=None):  # noqa: E501
        """OrderAcknowledgement - a model defined in Swagger"""  # noqa: E501

        self._merchant_order_no = None
        self._order_id = None
        self.discriminator = None

        self.merchant_order_no = merchant_order_no
        self.order_id = order_id

    @property
    def merchant_order_no(self):
        """Gets the merchant_order_no of this OrderAcknowledgement.  # noqa: E501

        Your own order reference, this will be used in consecutive order processing API calls  # noqa: E501

        :return: The merchant_order_no of this OrderAcknowledgement.  # noqa: E501
        :rtype: str
        """
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, merchant_order_no):
        """Sets the merchant_order_no of this OrderAcknowledgement.

        Your own order reference, this will be used in consecutive order processing API calls  # noqa: E501

        :param merchant_order_no: The merchant_order_no of this OrderAcknowledgement.  # noqa: E501
        :type: str
        """
        if merchant_order_no is None:
            raise ValueError("Invalid value for `merchant_order_no`, must not be `None`")  # noqa: E501
        if merchant_order_no is not None and len(merchant_order_no) > 50:
            raise ValueError("Invalid value for `merchant_order_no`, length must be less than or equal to `50`")  # noqa: E501
        if merchant_order_no is not None and len(merchant_order_no) < 0:
            raise ValueError("Invalid value for `merchant_order_no`, length must be greater than or equal to `0`")  # noqa: E501

        self._merchant_order_no = merchant_order_no

    @property
    def order_id(self):
        """Gets the order_id of this OrderAcknowledgement.  # noqa: E501

        The ChannelEngine order ID of the order you would like to acknowledge  # noqa: E501

        :return: The order_id of this OrderAcknowledgement.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderAcknowledgement.

        The ChannelEngine order ID of the order you would like to acknowledge  # noqa: E501

        :param order_id: The order_id of this OrderAcknowledgement.  # noqa: E501
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

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
        if not isinstance(other, OrderAcknowledgement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
