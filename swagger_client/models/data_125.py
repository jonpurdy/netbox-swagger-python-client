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


class Data125(object):
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
        'tenant': 'str',
        'name': 'str',
        'rd': 'str',
        'enforce_unique': 'bool',
        'custom_fields': 'str',
        'description': 'str'
    }

    attribute_map = {
        'tenant': 'tenant',
        'name': 'name',
        'rd': 'rd',
        'enforce_unique': 'enforce_unique',
        'custom_fields': 'custom_fields',
        'description': 'description'
    }

    def __init__(self, tenant=None, name=None, rd=None, enforce_unique=None, custom_fields=None, description=None):
        """
        Data125 - a model defined in Swagger
        """

        self._tenant = None
        self._name = None
        self._rd = None
        self._enforce_unique = None
        self._custom_fields = None
        self._description = None

        if tenant is not None:
          self.tenant = tenant
        if name is not None:
          self.name = name
        if rd is not None:
          self.rd = rd
        if enforce_unique is not None:
          self.enforce_unique = enforce_unique
        if custom_fields is not None:
          self.custom_fields = custom_fields
        if description is not None:
          self.description = description

    @property
    def tenant(self):
        """
        Gets the tenant of this Data125.
        

        :return: The tenant of this Data125.
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """
        Sets the tenant of this Data125.
        

        :param tenant: The tenant of this Data125.
        :type: str
        """

        self._tenant = tenant

    @property
    def name(self):
        """
        Gets the name of this Data125.
        

        :return: The name of this Data125.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Data125.
        

        :param name: The name of this Data125.
        :type: str
        """

        self._name = name

    @property
    def rd(self):
        """
        Gets the rd of this Data125.
        

        :return: The rd of this Data125.
        :rtype: str
        """
        return self._rd

    @rd.setter
    def rd(self, rd):
        """
        Sets the rd of this Data125.
        

        :param rd: The rd of this Data125.
        :type: str
        """

        self._rd = rd

    @property
    def enforce_unique(self):
        """
        Gets the enforce_unique of this Data125.
        Prevent duplicate prefixes/IP addresses within this VRF

        :return: The enforce_unique of this Data125.
        :rtype: bool
        """
        return self._enforce_unique

    @enforce_unique.setter
    def enforce_unique(self, enforce_unique):
        """
        Sets the enforce_unique of this Data125.
        Prevent duplicate prefixes/IP addresses within this VRF

        :param enforce_unique: The enforce_unique of this Data125.
        :type: bool
        """

        self._enforce_unique = enforce_unique

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this Data125.
        

        :return: The custom_fields of this Data125.
        :rtype: str
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this Data125.
        

        :param custom_fields: The custom_fields of this Data125.
        :type: str
        """

        self._custom_fields = custom_fields

    @property
    def description(self):
        """
        Gets the description of this Data125.
        

        :return: The description of this Data125.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Data125.
        

        :param description: The description of this Data125.
        :type: str
        """

        self._description = description

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
        if not isinstance(other, Data125):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
