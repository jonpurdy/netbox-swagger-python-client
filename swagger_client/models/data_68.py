# coding: utf-8

"""
    NetBox API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Data68(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'device': 'str',
        'power_outlet': 'str',
        'connection_status': 'str',
        'name': 'str'
    }

    attribute_map = {
        'device': 'device',
        'power_outlet': 'power_outlet',
        'connection_status': 'connection_status',
        'name': 'name'
    }

    def __init__(self, device=None, power_outlet=None, connection_status=None, name=None):
        """
        Data68 - a model defined in Swagger
        """

        self._device = None
        self._power_outlet = None
        self._connection_status = None
        self._name = None

        if device is not None:
          self.device = device
        if power_outlet is not None:
          self.power_outlet = power_outlet
        if connection_status is not None:
          self.connection_status = connection_status
        if name is not None:
          self.name = name

    @property
    def device(self):
        """
        Gets the device of this Data68.
        

        :return: The device of this Data68.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this Data68.
        

        :param device: The device of this Data68.
        :type: str
        """

        self._device = device

    @property
    def power_outlet(self):
        """
        Gets the power_outlet of this Data68.
        

        :return: The power_outlet of this Data68.
        :rtype: str
        """
        return self._power_outlet

    @power_outlet.setter
    def power_outlet(self, power_outlet):
        """
        Sets the power_outlet of this Data68.
        

        :param power_outlet: The power_outlet of this Data68.
        :type: str
        """

        self._power_outlet = power_outlet

    @property
    def connection_status(self):
        """
        Gets the connection_status of this Data68.
        

        :return: The connection_status of this Data68.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """
        Sets the connection_status of this Data68.
        

        :param connection_status: The connection_status of this Data68.
        :type: str
        """

        self._connection_status = connection_status

    @property
    def name(self):
        """
        Gets the name of this Data68.
        

        :return: The name of this Data68.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Data68.
        

        :param name: The name of this Data68.
        :type: str
        """

        self._name = name

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
        if not isinstance(other, Data68):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
