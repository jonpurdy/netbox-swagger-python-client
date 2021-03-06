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


class Data50(object):
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
        'name': 'str',
        'parent': 'str',
        'discovered': 'bool',
        'part_id': 'str',
        'device': 'str',
        'serial': 'str',
        'manufacturer': 'str'
    }

    attribute_map = {
        'name': 'name',
        'parent': 'parent',
        'discovered': 'discovered',
        'part_id': 'part_id',
        'device': 'device',
        'serial': 'serial',
        'manufacturer': 'manufacturer'
    }

    def __init__(self, name=None, parent=None, discovered=None, part_id=None, device=None, serial=None, manufacturer=None):
        """
        Data50 - a model defined in Swagger
        """

        self._name = None
        self._parent = None
        self._discovered = None
        self._part_id = None
        self._device = None
        self._serial = None
        self._manufacturer = None

        if name is not None:
          self.name = name
        if parent is not None:
          self.parent = parent
        if discovered is not None:
          self.discovered = discovered
        if part_id is not None:
          self.part_id = part_id
        if device is not None:
          self.device = device
        if serial is not None:
          self.serial = serial
        if manufacturer is not None:
          self.manufacturer = manufacturer

    @property
    def name(self):
        """
        Gets the name of this Data50.
        

        :return: The name of this Data50.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Data50.
        

        :param name: The name of this Data50.
        :type: str
        """

        self._name = name

    @property
    def parent(self):
        """
        Gets the parent of this Data50.
        

        :return: The parent of this Data50.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this Data50.
        

        :param parent: The parent of this Data50.
        :type: str
        """

        self._parent = parent

    @property
    def discovered(self):
        """
        Gets the discovered of this Data50.
        

        :return: The discovered of this Data50.
        :rtype: bool
        """
        return self._discovered

    @discovered.setter
    def discovered(self, discovered):
        """
        Sets the discovered of this Data50.
        

        :param discovered: The discovered of this Data50.
        :type: bool
        """

        self._discovered = discovered

    @property
    def part_id(self):
        """
        Gets the part_id of this Data50.
        

        :return: The part_id of this Data50.
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """
        Sets the part_id of this Data50.
        

        :param part_id: The part_id of this Data50.
        :type: str
        """

        self._part_id = part_id

    @property
    def device(self):
        """
        Gets the device of this Data50.
        

        :return: The device of this Data50.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this Data50.
        

        :param device: The device of this Data50.
        :type: str
        """

        self._device = device

    @property
    def serial(self):
        """
        Gets the serial of this Data50.
        

        :return: The serial of this Data50.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this Data50.
        

        :param serial: The serial of this Data50.
        :type: str
        """

        self._serial = serial

    @property
    def manufacturer(self):
        """
        Gets the manufacturer of this Data50.
        

        :return: The manufacturer of this Data50.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """
        Sets the manufacturer of this Data50.
        

        :param manufacturer: The manufacturer of this Data50.
        :type: str
        """

        self._manufacturer = manufacturer

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
        if not isinstance(other, Data50):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
