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


class SingleOfChannelProductChangesResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, content=None, status_code=None, success=None, message=None, validation_errors=None):
        """
        SingleOfChannelProductChangesResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content': 'ChannelProductChangesResponse',
            'status_code': 'int',
            'success': 'bool',
            'message': 'str',
            'validation_errors': 'dict(str, list[str])'
        }

        self.attribute_map = {
            'content': 'Content',
            'status_code': 'StatusCode',
            'success': 'Success',
            'message': 'Message',
            'validation_errors': 'ValidationErrors'
        }

        self._content = content
        self._status_code = status_code
        self._success = success
        self._message = message
        self._validation_errors = validation_errors

    @property
    def content(self):
        """
        Gets the content of this SingleOfChannelProductChangesResponse.

        :return: The content of this SingleOfChannelProductChangesResponse.
        :rtype: ChannelProductChangesResponse
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this SingleOfChannelProductChangesResponse.

        :param content: The content of this SingleOfChannelProductChangesResponse.
        :type: ChannelProductChangesResponse
        """

        self._content = content

    @property
    def status_code(self):
        """
        Gets the status_code of this SingleOfChannelProductChangesResponse.

        :return: The status_code of this SingleOfChannelProductChangesResponse.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """
        Sets the status_code of this SingleOfChannelProductChangesResponse.

        :param status_code: The status_code of this SingleOfChannelProductChangesResponse.
        :type: int
        """

        self._status_code = status_code

    @property
    def success(self):
        """
        Gets the success of this SingleOfChannelProductChangesResponse.

        :return: The success of this SingleOfChannelProductChangesResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this SingleOfChannelProductChangesResponse.

        :param success: The success of this SingleOfChannelProductChangesResponse.
        :type: bool
        """

        self._success = success

    @property
    def message(self):
        """
        Gets the message of this SingleOfChannelProductChangesResponse.

        :return: The message of this SingleOfChannelProductChangesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this SingleOfChannelProductChangesResponse.

        :param message: The message of this SingleOfChannelProductChangesResponse.
        :type: str
        """

        self._message = message

    @property
    def validation_errors(self):
        """
        Gets the validation_errors of this SingleOfChannelProductChangesResponse.

        :return: The validation_errors of this SingleOfChannelProductChangesResponse.
        :rtype: dict(str, list[str])
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """
        Sets the validation_errors of this SingleOfChannelProductChangesResponse.

        :param validation_errors: The validation_errors of this SingleOfChannelProductChangesResponse.
        :type: dict(str, list[str])
        """

        self._validation_errors = validation_errors

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
        if not isinstance(other, SingleOfChannelProductChangesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
