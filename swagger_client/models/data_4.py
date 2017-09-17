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


class Data4(object):
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
        'slug': 'str'
    }

    attribute_map = {
        'name': 'name',
        'slug': 'slug'
    }

    def __init__(self, name=None, slug=None):
        """
        Data4 - a model defined in Swagger
        """

        self._name = None
        self._slug = None

        self.name = name
        self.slug = slug

    @property
    def name(self):
        """
        Gets the name of this Data4.
        

        :return: The name of this Data4.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Data4.
        

        :param name: The name of this Data4.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def slug(self):
        """
        Gets the slug of this Data4.
        

        :return: The slug of this Data4.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """
        Sets the slug of this Data4.
        

        :param slug: The slug of this Data4.
        :type: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")

        self._slug = slug

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
        if not isinstance(other, Data4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
