# coding: utf-8

"""
    Server APIs

    This page lists all the rest apis for server.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class OrderColourResponse(object):
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
        'colour': 'OrderColour',
        'order_id': 'OrderId',
        'status': 'str'
    }

    attribute_map = {
        'colour': 'colour',
        'order_id': 'orderId',
        'status': 'status'
    }

    def __init__(self, colour=None, order_id=None, status=None, _configuration=None):  # noqa: E501
        """OrderColourResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._colour = None
        self._order_id = None
        self._status = None
        self.discriminator = None

        if colour is not None:
            self.colour = colour
        if order_id is not None:
            self.order_id = order_id
        if status is not None:
            self.status = status

    @property
    def colour(self):
        """Gets the colour of this OrderColourResponse.  # noqa: E501


        :return: The colour of this OrderColourResponse.  # noqa: E501
        :rtype: OrderColour
        """
        return self._colour

    @colour.setter
    def colour(self, colour):
        """Sets the colour of this OrderColourResponse.


        :param colour: The colour of this OrderColourResponse.  # noqa: E501
        :type: OrderColour
        """

        self._colour = colour

    @property
    def order_id(self):
        """Gets the order_id of this OrderColourResponse.  # noqa: E501


        :return: The order_id of this OrderColourResponse.  # noqa: E501
        :rtype: OrderId
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderColourResponse.


        :param order_id: The order_id of this OrderColourResponse.  # noqa: E501
        :type: OrderId
        """

        self._order_id = order_id

    @property
    def status(self):
        """Gets the status of this OrderColourResponse.  # noqa: E501


        :return: The status of this OrderColourResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrderColourResponse.


        :param status: The status of this OrderColourResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["INCORRECT_STATE", "INTERNAL_ERROR", "NO_SEGMENT_AVAILABLE", "OK", "UNAUTHORIZED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(OrderColourResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrderColourResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderColourResponse):
            return True

        return self.to_dict() != other.to_dict()