# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    OpenAPI spec version: 2.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from channelengine_merchant_api_client.models.merchant_return_line_response import MerchantReturnLineResponse  # noqa: F401,E501


class MerchantReturnResponse(object):
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
        'lines': 'list[MerchantReturnLineResponse]',
        'id': 'int',
        'reason': 'str',
        'customer_comment': 'str',
        'merchant_comment': 'str',
        'refund_incl_vat': 'float',
        'refund_excl_vat': 'float'
    }

    attribute_map = {
        'merchant_order_no': 'MerchantOrderNo',
        'lines': 'Lines',
        'id': 'Id',
        'reason': 'Reason',
        'customer_comment': 'CustomerComment',
        'merchant_comment': 'MerchantComment',
        'refund_incl_vat': 'RefundInclVat',
        'refund_excl_vat': 'RefundExclVat'
    }

    def __init__(self, merchant_order_no=None, lines=None, id=None, reason=None, customer_comment=None, merchant_comment=None, refund_incl_vat=None, refund_excl_vat=None):  # noqa: E501
        """MerchantReturnResponse - a model defined in Swagger"""  # noqa: E501

        self._merchant_order_no = None
        self._lines = None
        self._id = None
        self._reason = None
        self._customer_comment = None
        self._merchant_comment = None
        self._refund_incl_vat = None
        self._refund_excl_vat = None
        self.discriminator = None

        if merchant_order_no is not None:
            self.merchant_order_no = merchant_order_no
        if lines is not None:
            self.lines = lines
        if id is not None:
            self.id = id
        if reason is not None:
            self.reason = reason
        if customer_comment is not None:
            self.customer_comment = customer_comment
        if merchant_comment is not None:
            self.merchant_comment = merchant_comment
        if refund_incl_vat is not None:
            self.refund_incl_vat = refund_incl_vat
        if refund_excl_vat is not None:
            self.refund_excl_vat = refund_excl_vat

    @property
    def merchant_order_no(self):
        """Gets the merchant_order_no of this MerchantReturnResponse.  # noqa: E501


        :return: The merchant_order_no of this MerchantReturnResponse.  # noqa: E501
        :rtype: str
        """
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, merchant_order_no):
        """Sets the merchant_order_no of this MerchantReturnResponse.


        :param merchant_order_no: The merchant_order_no of this MerchantReturnResponse.  # noqa: E501
        :type: str
        """

        self._merchant_order_no = merchant_order_no

    @property
    def lines(self):
        """Gets the lines of this MerchantReturnResponse.  # noqa: E501


        :return: The lines of this MerchantReturnResponse.  # noqa: E501
        :rtype: list[MerchantReturnLineResponse]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this MerchantReturnResponse.


        :param lines: The lines of this MerchantReturnResponse.  # noqa: E501
        :type: list[MerchantReturnLineResponse]
        """

        self._lines = lines

    @property
    def id(self):
        """Gets the id of this MerchantReturnResponse.  # noqa: E501


        :return: The id of this MerchantReturnResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MerchantReturnResponse.


        :param id: The id of this MerchantReturnResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def reason(self):
        """Gets the reason of this MerchantReturnResponse.  # noqa: E501


        :return: The reason of this MerchantReturnResponse.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this MerchantReturnResponse.


        :param reason: The reason of this MerchantReturnResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["PRODUCT_DEFECT", "PRODUCT_UNSATISFACTORY", "REFUSED", "REFUSED_DAMAGED", "WRONG_ADDRESS", "NOT_COLLECTED", "OTHER"]  # noqa: E501
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def customer_comment(self):
        """Gets the customer_comment of this MerchantReturnResponse.  # noqa: E501


        :return: The customer_comment of this MerchantReturnResponse.  # noqa: E501
        :rtype: str
        """
        return self._customer_comment

    @customer_comment.setter
    def customer_comment(self, customer_comment):
        """Sets the customer_comment of this MerchantReturnResponse.


        :param customer_comment: The customer_comment of this MerchantReturnResponse.  # noqa: E501
        :type: str
        """
        if customer_comment is not None and len(customer_comment) > 4001:
            raise ValueError("Invalid value for `customer_comment`, length must be less than or equal to `4001`")  # noqa: E501
        if customer_comment is not None and len(customer_comment) < 0:
            raise ValueError("Invalid value for `customer_comment`, length must be greater than or equal to `0`")  # noqa: E501

        self._customer_comment = customer_comment

    @property
    def merchant_comment(self):
        """Gets the merchant_comment of this MerchantReturnResponse.  # noqa: E501


        :return: The merchant_comment of this MerchantReturnResponse.  # noqa: E501
        :rtype: str
        """
        return self._merchant_comment

    @merchant_comment.setter
    def merchant_comment(self, merchant_comment):
        """Sets the merchant_comment of this MerchantReturnResponse.


        :param merchant_comment: The merchant_comment of this MerchantReturnResponse.  # noqa: E501
        :type: str
        """
        if merchant_comment is not None and len(merchant_comment) > 4001:
            raise ValueError("Invalid value for `merchant_comment`, length must be less than or equal to `4001`")  # noqa: E501
        if merchant_comment is not None and len(merchant_comment) < 0:
            raise ValueError("Invalid value for `merchant_comment`, length must be greater than or equal to `0`")  # noqa: E501

        self._merchant_comment = merchant_comment

    @property
    def refund_incl_vat(self):
        """Gets the refund_incl_vat of this MerchantReturnResponse.  # noqa: E501


        :return: The refund_incl_vat of this MerchantReturnResponse.  # noqa: E501
        :rtype: float
        """
        return self._refund_incl_vat

    @refund_incl_vat.setter
    def refund_incl_vat(self, refund_incl_vat):
        """Sets the refund_incl_vat of this MerchantReturnResponse.


        :param refund_incl_vat: The refund_incl_vat of this MerchantReturnResponse.  # noqa: E501
        :type: float
        """

        self._refund_incl_vat = refund_incl_vat

    @property
    def refund_excl_vat(self):
        """Gets the refund_excl_vat of this MerchantReturnResponse.  # noqa: E501


        :return: The refund_excl_vat of this MerchantReturnResponse.  # noqa: E501
        :rtype: float
        """
        return self._refund_excl_vat

    @refund_excl_vat.setter
    def refund_excl_vat(self, refund_excl_vat):
        """Sets the refund_excl_vat of this MerchantReturnResponse.


        :param refund_excl_vat: The refund_excl_vat of this MerchantReturnResponse.  # noqa: E501
        :type: float
        """

        self._refund_excl_vat = refund_excl_vat

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
        if not isinstance(other, MerchantReturnResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
