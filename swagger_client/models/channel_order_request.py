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


class ChannelOrderRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, channel_order_no=None, lines=None, phone=None, email=None, company_registration_no=None, vat_no=None, payment_method=None, shipping_costs_incl_vat=None, currency_code=None, order_date=None, channel_customer_no=None, billing_address=None, shipping_address=None, extra_data=None):
        """
        ChannelOrderRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'channel_order_no': 'str',
            'lines': 'list[ChannelOrderLineRequest]',
            'phone': 'str',
            'email': 'str',
            'company_registration_no': 'str',
            'vat_no': 'str',
            'payment_method': 'str',
            'shipping_costs_incl_vat': 'float',
            'currency_code': 'str',
            'order_date': 'datetime',
            'channel_customer_no': 'str',
            'billing_address': 'EntitiesAddressModels',
            'shipping_address': 'EntitiesAddressModels',
            'extra_data': 'dict(str, str)'
        }

        self.attribute_map = {
            'channel_order_no': 'ChannelOrderNo',
            'lines': 'Lines',
            'phone': 'Phone',
            'email': 'Email',
            'company_registration_no': 'CompanyRegistrationNo',
            'vat_no': 'VatNo',
            'payment_method': 'PaymentMethod',
            'shipping_costs_incl_vat': 'ShippingCostsInclVat',
            'currency_code': 'CurrencyCode',
            'order_date': 'OrderDate',
            'channel_customer_no': 'ChannelCustomerNo',
            'billing_address': 'BillingAddress',
            'shipping_address': 'ShippingAddress',
            'extra_data': 'ExtraData'
        }

        self._channel_order_no = channel_order_no
        self._lines = lines
        self._phone = phone
        self._email = email
        self._company_registration_no = company_registration_no
        self._vat_no = vat_no
        self._payment_method = payment_method
        self._shipping_costs_incl_vat = shipping_costs_incl_vat
        self._currency_code = currency_code
        self._order_date = order_date
        self._channel_customer_no = channel_customer_no
        self._billing_address = billing_address
        self._shipping_address = shipping_address
        self._extra_data = extra_data

    @property
    def channel_order_no(self):
        """
        Gets the channel_order_no of this ChannelOrderRequest.
        The unique order reference used by the Channel

        :return: The channel_order_no of this ChannelOrderRequest.
        :rtype: str
        """
        return self._channel_order_no

    @channel_order_no.setter
    def channel_order_no(self, channel_order_no):
        """
        Sets the channel_order_no of this ChannelOrderRequest.
        The unique order reference used by the Channel

        :param channel_order_no: The channel_order_no of this ChannelOrderRequest.
        :type: str
        """
        if channel_order_no is None:
            raise ValueError("Invalid value for `channel_order_no`, must not be `None`")
        if channel_order_no is not None and len(channel_order_no) > 50:
            raise ValueError("Invalid value for `channel_order_no`, length must be less than or equal to `50`")
        if channel_order_no is not None and len(channel_order_no) < 0:
            raise ValueError("Invalid value for `channel_order_no`, length must be greater than or equal to `0`")

        self._channel_order_no = channel_order_no

    @property
    def lines(self):
        """
        Gets the lines of this ChannelOrderRequest.
        The order lines

        :return: The lines of this ChannelOrderRequest.
        :rtype: list[ChannelOrderLineRequest]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """
        Sets the lines of this ChannelOrderRequest.
        The order lines

        :param lines: The lines of this ChannelOrderRequest.
        :type: list[ChannelOrderLineRequest]
        """
        if lines is None:
            raise ValueError("Invalid value for `lines`, must not be `None`")

        self._lines = lines

    @property
    def phone(self):
        """
        Gets the phone of this ChannelOrderRequest.

        :return: The phone of this ChannelOrderRequest.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this ChannelOrderRequest.

        :param phone: The phone of this ChannelOrderRequest.
        :type: str
        """
        if phone is not None and len(phone) > 20:
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `20`")
        if phone is not None and len(phone) < 0:
            raise ValueError("Invalid value for `phone`, length must be greater than or equal to `0`")

        self._phone = phone

    @property
    def email(self):
        """
        Gets the email of this ChannelOrderRequest.

        :return: The email of this ChannelOrderRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this ChannelOrderRequest.

        :param email: The email of this ChannelOrderRequest.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")
        if email is not None and len(email) > 250:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `250`")
        if email is not None and len(email) < 0:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `0`")

        self._email = email

    @property
    def company_registration_no(self):
        """
        Gets the company_registration_no of this ChannelOrderRequest.

        :return: The company_registration_no of this ChannelOrderRequest.
        :rtype: str
        """
        return self._company_registration_no

    @company_registration_no.setter
    def company_registration_no(self, company_registration_no):
        """
        Sets the company_registration_no of this ChannelOrderRequest.

        :param company_registration_no: The company_registration_no of this ChannelOrderRequest.
        :type: str
        """
        if company_registration_no is not None and len(company_registration_no) > 50:
            raise ValueError("Invalid value for `company_registration_no`, length must be less than or equal to `50`")
        if company_registration_no is not None and len(company_registration_no) < 0:
            raise ValueError("Invalid value for `company_registration_no`, length must be greater than or equal to `0`")

        self._company_registration_no = company_registration_no

    @property
    def vat_no(self):
        """
        Gets the vat_no of this ChannelOrderRequest.

        :return: The vat_no of this ChannelOrderRequest.
        :rtype: str
        """
        return self._vat_no

    @vat_no.setter
    def vat_no(self, vat_no):
        """
        Sets the vat_no of this ChannelOrderRequest.

        :param vat_no: The vat_no of this ChannelOrderRequest.
        :type: str
        """
        if vat_no is not None and len(vat_no) > 50:
            raise ValueError("Invalid value for `vat_no`, length must be less than or equal to `50`")
        if vat_no is not None and len(vat_no) < 0:
            raise ValueError("Invalid value for `vat_no`, length must be greater than or equal to `0`")

        self._vat_no = vat_no

    @property
    def payment_method(self):
        """
        Gets the payment_method of this ChannelOrderRequest.

        :return: The payment_method of this ChannelOrderRequest.
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """
        Sets the payment_method of this ChannelOrderRequest.

        :param payment_method: The payment_method of this ChannelOrderRequest.
        :type: str
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")
        if payment_method is not None and len(payment_method) > 50:
            raise ValueError("Invalid value for `payment_method`, length must be less than or equal to `50`")
        if payment_method is not None and len(payment_method) < 0:
            raise ValueError("Invalid value for `payment_method`, length must be greater than or equal to `0`")

        self._payment_method = payment_method

    @property
    def shipping_costs_incl_vat(self):
        """
        Gets the shipping_costs_incl_vat of this ChannelOrderRequest.
        The shipping fee including VAT  (in the tenant's base currency calculated using the exchange rate at the time of ordering).

        :return: The shipping_costs_incl_vat of this ChannelOrderRequest.
        :rtype: float
        """
        return self._shipping_costs_incl_vat

    @shipping_costs_incl_vat.setter
    def shipping_costs_incl_vat(self, shipping_costs_incl_vat):
        """
        Sets the shipping_costs_incl_vat of this ChannelOrderRequest.
        The shipping fee including VAT  (in the tenant's base currency calculated using the exchange rate at the time of ordering).

        :param shipping_costs_incl_vat: The shipping_costs_incl_vat of this ChannelOrderRequest.
        :type: float
        """
        if shipping_costs_incl_vat is None:
            raise ValueError("Invalid value for `shipping_costs_incl_vat`, must not be `None`")

        self._shipping_costs_incl_vat = shipping_costs_incl_vat

    @property
    def currency_code(self):
        """
        Gets the currency_code of this ChannelOrderRequest.

        :return: The currency_code of this ChannelOrderRequest.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this ChannelOrderRequest.

        :param currency_code: The currency_code of this ChannelOrderRequest.
        :type: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")

        self._currency_code = currency_code

    @property
    def order_date(self):
        """
        Gets the order_date of this ChannelOrderRequest.

        :return: The order_date of this ChannelOrderRequest.
        :rtype: datetime
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """
        Sets the order_date of this ChannelOrderRequest.

        :param order_date: The order_date of this ChannelOrderRequest.
        :type: datetime
        """
        if order_date is None:
            raise ValueError("Invalid value for `order_date`, must not be `None`")

        self._order_date = order_date

    @property
    def channel_customer_no(self):
        """
        Gets the channel_customer_no of this ChannelOrderRequest.

        :return: The channel_customer_no of this ChannelOrderRequest.
        :rtype: str
        """
        return self._channel_customer_no

    @channel_customer_no.setter
    def channel_customer_no(self, channel_customer_no):
        """
        Sets the channel_customer_no of this ChannelOrderRequest.

        :param channel_customer_no: The channel_customer_no of this ChannelOrderRequest.
        :type: str
        """
        if channel_customer_no is not None and len(channel_customer_no) > 50:
            raise ValueError("Invalid value for `channel_customer_no`, length must be less than or equal to `50`")
        if channel_customer_no is not None and len(channel_customer_no) < 0:
            raise ValueError("Invalid value for `channel_customer_no`, length must be greater than or equal to `0`")

        self._channel_customer_no = channel_customer_no

    @property
    def billing_address(self):
        """
        Gets the billing_address of this ChannelOrderRequest.

        :return: The billing_address of this ChannelOrderRequest.
        :rtype: EntitiesAddressModels
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """
        Sets the billing_address of this ChannelOrderRequest.

        :param billing_address: The billing_address of this ChannelOrderRequest.
        :type: EntitiesAddressModels
        """
        if billing_address is None:
            raise ValueError("Invalid value for `billing_address`, must not be `None`")

        self._billing_address = billing_address

    @property
    def shipping_address(self):
        """
        Gets the shipping_address of this ChannelOrderRequest.

        :return: The shipping_address of this ChannelOrderRequest.
        :rtype: EntitiesAddressModels
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """
        Sets the shipping_address of this ChannelOrderRequest.

        :param shipping_address: The shipping_address of this ChannelOrderRequest.
        :type: EntitiesAddressModels
        """
        if shipping_address is None:
            raise ValueError("Invalid value for `shipping_address`, must not be `None`")

        self._shipping_address = shipping_address

    @property
    def extra_data(self):
        """
        Gets the extra_data of this ChannelOrderRequest.

        :return: The extra_data of this ChannelOrderRequest.
        :rtype: dict(str, str)
        """
        return self._extra_data

    @extra_data.setter
    def extra_data(self, extra_data):
        """
        Sets the extra_data of this ChannelOrderRequest.

        :param extra_data: The extra_data of this ChannelOrderRequest.
        :type: dict(str, str)
        """

        self._extra_data = extra_data

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
        if not isinstance(other, ChannelOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
