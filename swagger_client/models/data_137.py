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


class Data137(object):
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
        'group': 'str',
        'description': 'str',
        'comments': 'str',
        'slug': 'str',
        'custom_fields': 'str',
        'name': 'str'
    }

    attribute_map = {
        'group': 'group',
        'description': 'description',
        'comments': 'comments',
        'slug': 'slug',
        'custom_fields': 'custom_fields',
        'name': 'name'
    }

    def __init__(self, group=None, description=None, comments=None, slug=None, custom_fields=None, name=None):
        """
        Data137 - a model defined in Swagger
        """

        self._group = None
        self._description = None
        self._comments = None
        self._slug = None
        self._custom_fields = None
        self._name = None

        if group is not None:
          self.group = group
        if description is not None:
          self.description = description
        if comments is not None:
          self.comments = comments
        if slug is not None:
          self.slug = slug
        if custom_fields is not None:
          self.custom_fields = custom_fields
        if name is not None:
          self.name = name

    @property
    def group(self):
        """
        Gets the group of this Data137.
        

        :return: The group of this Data137.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this Data137.
        

        :param group: The group of this Data137.
        :type: str
        """

        self._group = group

    @property
    def description(self):
        """
        Gets the description of this Data137.
        Long-form name (optional)

        :return: The description of this Data137.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Data137.
        Long-form name (optional)

        :param description: The description of this Data137.
        :type: str
        """

        self._description = description

    @property
    def comments(self):
        """
        Gets the comments of this Data137.
        

        :return: The comments of this Data137.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this Data137.
        

        :param comments: The comments of this Data137.
        :type: str
        """

        self._comments = comments

    @property
    def slug(self):
        """
        Gets the slug of this Data137.
        

        :return: The slug of this Data137.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """
        Sets the slug of this Data137.
        

        :param slug: The slug of this Data137.
        :type: str
        """

        self._slug = slug

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this Data137.
        

        :return: The custom_fields of this Data137.
        :rtype: str
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this Data137.
        

        :param custom_fields: The custom_fields of this Data137.
        :type: str
        """

        self._custom_fields = custom_fields

    @property
    def name(self):
        """
        Gets the name of this Data137.
        

        :return: The name of this Data137.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Data137.
        

        :param name: The name of this Data137.
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
        if not isinstance(other, Data137):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
