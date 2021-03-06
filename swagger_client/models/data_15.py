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


class Data15(object):
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
        'cs_port': 'str',
        'connection_status': 'str',
        'name': 'str'
    }

    attribute_map = {
        'device': 'device',
        'cs_port': 'cs_port',
        'connection_status': 'connection_status',
        'name': 'name'
    }

    def __init__(self, device=None, cs_port=None, connection_status=None, name=None):
        """
        Data15 - a model defined in Swagger
        """

        self._device = None
        self._cs_port = None
        self._connection_status = None
        self._name = None

        self.device = device
        if cs_port is not None:
          self.cs_port = cs_port
        if connection_status is not None:
          self.connection_status = connection_status
        self.name = name

    @property
    def device(self):
        """
        Gets the device of this Data15.
        

        :return: The device of this Data15.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this Data15.
        

        :param device: The device of this Data15.
        :type: str
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")

        self._device = device

    @property
    def cs_port(self):
        """
        Gets the cs_port of this Data15.
        

        :return: The cs_port of this Data15.
        :rtype: str
        """
        return self._cs_port

    @cs_port.setter
    def cs_port(self, cs_port):
        """
        Sets the cs_port of this Data15.
        

        :param cs_port: The cs_port of this Data15.
        :type: str
        """

        self._cs_port = cs_port

    @property
    def connection_status(self):
        """
        Gets the connection_status of this Data15.
        

        :return: The connection_status of this Data15.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """
        Sets the connection_status of this Data15.
        

        :param connection_status: The connection_status of this Data15.
        :type: str
        """

        self._connection_status = connection_status

    @property
    def name(self):
        """
        Gets the name of this Data15.
        

        :return: The name of this Data15.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Data15.
        

        :param name: The name of this Data15.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

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
        if not isinstance(other, Data15):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
