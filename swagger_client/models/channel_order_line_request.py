# coding: utf-8

"""
    ChannelEngine API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ChannelOrderLineRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, channel_product_no=None, quantity=None, unit_price_incl_vat=None, fee_fixed=None, fee_rate=None, condition=None):
        """
        ChannelOrderLineRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'channel_product_no': 'str',
            'quantity': 'int',
            'unit_price_incl_vat': 'float',
            'fee_fixed': 'float',
            'fee_rate': 'float',
            'condition': 'str'
        }

        self.attribute_map = {
            'channel_product_no': 'ChannelProductNo',
            'quantity': 'Quantity',
            'unit_price_incl_vat': 'UnitPriceInclVat',
            'fee_fixed': 'FeeFixed',
            'fee_rate': 'FeeRate',
            'condition': 'Condition'
        }

        self._channel_product_no = channel_product_no
        self._quantity = quantity
        self._unit_price_incl_vat = unit_price_incl_vat
        self._fee_fixed = fee_fixed
        self._fee_rate = fee_rate
        self._condition = condition

    @property
    def channel_product_no(self):
        """
        Gets the channel_product_no of this ChannelOrderLineRequest.

        :return: The channel_product_no of this ChannelOrderLineRequest.
        :rtype: str
        """
        return self._channel_product_no

    @channel_product_no.setter
    def channel_product_no(self, channel_product_no):
        """
        Sets the channel_product_no of this ChannelOrderLineRequest.

        :param channel_product_no: The channel_product_no of this ChannelOrderLineRequest.
        :type: str
        """
        if channel_product_no is None:
            raise ValueError("Invalid value for `channel_product_no`, must not be `None`")
        if channel_product_no is not None and len(channel_product_no) > 50:
            raise ValueError("Invalid value for `channel_product_no`, length must be less than or equal to `50`")
        if channel_product_no is not None and len(channel_product_no) < 0:
            raise ValueError("Invalid value for `channel_product_no`, length must be greater than or equal to `0`")

        self._channel_product_no = channel_product_no

    @property
    def quantity(self):
        """
        Gets the quantity of this ChannelOrderLineRequest.

        :return: The quantity of this ChannelOrderLineRequest.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this ChannelOrderLineRequest.

        :param quantity: The quantity of this ChannelOrderLineRequest.
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")

        self._quantity = quantity

    @property
    def unit_price_incl_vat(self):
        """
        Gets the unit_price_incl_vat of this ChannelOrderLineRequest.
        The value of a single unit of the ordered product including VAT  (in the tenant's base currency calculated using the exchange rate at the time of ordering).

        :return: The unit_price_incl_vat of this ChannelOrderLineRequest.
        :rtype: float
        """
        return self._unit_price_incl_vat

    @unit_price_incl_vat.setter
    def unit_price_incl_vat(self, unit_price_incl_vat):
        """
        Sets the unit_price_incl_vat of this ChannelOrderLineRequest.
        The value of a single unit of the ordered product including VAT  (in the tenant's base currency calculated using the exchange rate at the time of ordering).

        :param unit_price_incl_vat: The unit_price_incl_vat of this ChannelOrderLineRequest.
        :type: float
        """
        if unit_price_incl_vat is None:
            raise ValueError("Invalid value for `unit_price_incl_vat`, must not be `None`")

        self._unit_price_incl_vat = unit_price_incl_vat

    @property
    def fee_fixed(self):
        """
        Gets the fee_fixed of this ChannelOrderLineRequest.
        A fixed fee that is charged by the Channel for this orderline.  This field is optional, send 0 if not applicable.

        :return: The fee_fixed of this ChannelOrderLineRequest.
        :rtype: float
        """
        return self._fee_fixed

    @fee_fixed.setter
    def fee_fixed(self, fee_fixed):
        """
        Sets the fee_fixed of this ChannelOrderLineRequest.
        A fixed fee that is charged by the Channel for this orderline.  This field is optional, send 0 if not applicable.

        :param fee_fixed: The fee_fixed of this ChannelOrderLineRequest.
        :type: float
        """

        self._fee_fixed = fee_fixed

    @property
    def fee_rate(self):
        """
        Gets the fee_rate of this ChannelOrderLineRequest.
        A percentage fee that is charged by the Channel for this orderline.  This field is optional, send 0 if not applicable.

        :return: The fee_rate of this ChannelOrderLineRequest.
        :rtype: float
        """
        return self._fee_rate

    @fee_rate.setter
    def fee_rate(self, fee_rate):
        """
        Sets the fee_rate of this ChannelOrderLineRequest.
        A percentage fee that is charged by the Channel for this orderline.  This field is optional, send 0 if not applicable.

        :param fee_rate: The fee_rate of this ChannelOrderLineRequest.
        :type: float
        """

        self._fee_rate = fee_rate

    @property
    def condition(self):
        """
        Gets the condition of this ChannelOrderLineRequest.
        The condition of the product, this can be used to indicate that a product is a second-hand product

        :return: The condition of this ChannelOrderLineRequest.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this ChannelOrderLineRequest.
        The condition of the product, this can be used to indicate that a product is a second-hand product

        :param condition: The condition of this ChannelOrderLineRequest.
        :type: str
        """
        allowed_values = ["NEW", "NEW_REFURBISHED", "USED_AS_NEW", "USED_GOOD", "USED_REASONABLE", "USED_MEDIOCRE", "UNKNOWN"]
        if condition not in allowed_values:
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"
                .format(condition, allowed_values)
            )

        self._condition = condition

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ChannelOrderLineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
