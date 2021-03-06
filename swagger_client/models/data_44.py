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


class Data44(object):
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
        'mgmt_only': 'bool',
        'name': 'str',
        'device_type': 'str',
        'form_factor': 'str'
    }

    attribute_map = {
        'mgmt_only': 'mgmt_only',
        'name': 'name',
        'device_type': 'device_type',
        'form_factor': 'form_factor'
    }

    def __init__(self, mgmt_only=None, name=None, device_type=None, form_factor=None):
        """
        Data44 - a model defined in Swagger
        """

        self._mgmt_only = None
        self._name = None
        self._device_type = None
        self._form_factor = None

        if mgmt_only is not None:
          self.mgmt_only = mgmt_only
        if name is not None:
          self.name = name
        if device_type is not None:
          self.device_type = device_type
        if form_factor is not None:
          self.form_factor = form_factor

    @property
    def mgmt_only(self):
        """
        Gets the mgmt_only of this Data44.
        

        :return: The mgmt_only of this Data44.
        :rtype: bool
        """
        return self._mgmt_only

    @mgmt_only.setter
    def mgmt_only(self, mgmt_only):
        """
        Sets the mgmt_only of this Data44.
        

        :param mgmt_only: The mgmt_only of this Data44.
        :type: bool
        """

        self._mgmt_only = mgmt_only

    @property
    def name(self):
        """
        Gets the name of this Data44.
        

        :return: The name of this Data44.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Data44.
        

        :param name: The name of this Data44.
        :type: str
        """

        self._name = name

    @property
    def device_type(self):
        """
        Gets the device_type of this Data44.
        

        :return: The device_type of this Data44.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """
        Sets the device_type of this Data44.
        

        :param device_type: The device_type of this Data44.
        :type: str
        """

        self._device_type = device_type

    @property
    def form_factor(self):
        """
        Gets the form_factor of this Data44.
        

        :return: The form_factor of this Data44.
        :rtype: str
        """
        return self._form_factor

    @form_factor.setter
    def form_factor(self, form_factor):
        """
        Sets the form_factor of this Data44.
        

        :param form_factor: The form_factor of this Data44.
        :type: str
        """

        self._form_factor = form_factor

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
        if not isinstance(other, Data44):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
