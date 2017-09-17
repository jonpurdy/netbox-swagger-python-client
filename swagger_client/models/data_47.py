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


class Data47(object):
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
        'form_factor': 'str',
        'name': 'str',
        'description': 'str',
        'lag': 'str',
        'mac_address': 'str',
        'device': 'str',
        'mgmt_only': 'bool'
    }

    attribute_map = {
        'form_factor': 'form_factor',
        'name': 'name',
        'description': 'description',
        'lag': 'lag',
        'mac_address': 'mac_address',
        'device': 'device',
        'mgmt_only': 'mgmt_only'
    }

    def __init__(self, form_factor=None, name=None, description=None, lag=None, mac_address=None, device=None, mgmt_only=None):
        """
        Data47 - a model defined in Swagger
        """

        self._form_factor = None
        self._name = None
        self._description = None
        self._lag = None
        self._mac_address = None
        self._device = None
        self._mgmt_only = None

        if form_factor is not None:
          self.form_factor = form_factor
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if lag is not None:
          self.lag = lag
        if mac_address is not None:
          self.mac_address = mac_address
        if device is not None:
          self.device = device
        if mgmt_only is not None:
          self.mgmt_only = mgmt_only

    @property
    def form_factor(self):
        """
        Gets the form_factor of this Data47.
        

        :return: The form_factor of this Data47.
        :rtype: str
        """
        return self._form_factor

    @form_factor.setter
    def form_factor(self, form_factor):
        """
        Sets the form_factor of this Data47.
        

        :param form_factor: The form_factor of this Data47.
        :type: str
        """

        self._form_factor = form_factor

    @property
    def name(self):
        """
        Gets the name of this Data47.
        

        :return: The name of this Data47.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Data47.
        

        :param name: The name of this Data47.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Data47.
        

        :return: The description of this Data47.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Data47.
        

        :param description: The description of this Data47.
        :type: str
        """

        self._description = description

    @property
    def lag(self):
        """
        Gets the lag of this Data47.
        

        :return: The lag of this Data47.
        :rtype: str
        """
        return self._lag

    @lag.setter
    def lag(self, lag):
        """
        Sets the lag of this Data47.
        

        :param lag: The lag of this Data47.
        :type: str
        """

        self._lag = lag

    @property
    def mac_address(self):
        """
        Gets the mac_address of this Data47.
        

        :return: The mac_address of this Data47.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this Data47.
        

        :param mac_address: The mac_address of this Data47.
        :type: str
        """

        self._mac_address = mac_address

    @property
    def device(self):
        """
        Gets the device of this Data47.
        

        :return: The device of this Data47.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this Data47.
        

        :param device: The device of this Data47.
        :type: str
        """

        self._device = device

    @property
    def mgmt_only(self):
        """
        Gets the mgmt_only of this Data47.
        This interface is used only for out-of-band management

        :return: The mgmt_only of this Data47.
        :rtype: bool
        """
        return self._mgmt_only

    @mgmt_only.setter
    def mgmt_only(self, mgmt_only):
        """
        Sets the mgmt_only of this Data47.
        This interface is used only for out-of-band management

        :param mgmt_only: The mgmt_only of this Data47.
        :type: bool
        """

        self._mgmt_only = mgmt_only

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
        if not isinstance(other, Data47):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other