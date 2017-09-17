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


class Data122(object):
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
        'status': 'str',
        'group': 'str',
        'name': 'str',
        'vid': 'int',
        'site': 'str',
        'role': 'str',
        'custom_fields': 'str',
        'tenant': 'str',
        'description': 'str'
    }

    attribute_map = {
        'status': 'status',
        'group': 'group',
        'name': 'name',
        'vid': 'vid',
        'site': 'site',
        'role': 'role',
        'custom_fields': 'custom_fields',
        'tenant': 'tenant',
        'description': 'description'
    }

    def __init__(self, status=None, group=None, name=None, vid=None, site=None, role=None, custom_fields=None, tenant=None, description=None):
        """
        Data122 - a model defined in Swagger
        """

        self._status = None
        self._group = None
        self._name = None
        self._vid = None
        self._site = None
        self._role = None
        self._custom_fields = None
        self._tenant = None
        self._description = None

        if status is not None:
          self.status = status
        if group is not None:
          self.group = group
        if name is not None:
          self.name = name
        if vid is not None:
          self.vid = vid
        if site is not None:
          self.site = site
        if role is not None:
          self.role = role
        if custom_fields is not None:
          self.custom_fields = custom_fields
        if tenant is not None:
          self.tenant = tenant
        if description is not None:
          self.description = description

    @property
    def status(self):
        """
        Gets the status of this Data122.
        

        :return: The status of this Data122.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Data122.
        

        :param status: The status of this Data122.
        :type: str
        """

        self._status = status

    @property
    def group(self):
        """
        Gets the group of this Data122.
        

        :return: The group of this Data122.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this Data122.
        

        :param group: The group of this Data122.
        :type: str
        """

        self._group = group

    @property
    def name(self):
        """
        Gets the name of this Data122.
        

        :return: The name of this Data122.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Data122.
        

        :param name: The name of this Data122.
        :type: str
        """

        self._name = name

    @property
    def vid(self):
        """
        Gets the vid of this Data122.
        

        :return: The vid of this Data122.
        :rtype: int
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """
        Sets the vid of this Data122.
        

        :param vid: The vid of this Data122.
        :type: int
        """

        self._vid = vid

    @property
    def site(self):
        """
        Gets the site of this Data122.
        

        :return: The site of this Data122.
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        """
        Sets the site of this Data122.
        

        :param site: The site of this Data122.
        :type: str
        """

        self._site = site

    @property
    def role(self):
        """
        Gets the role of this Data122.
        

        :return: The role of this Data122.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this Data122.
        

        :param role: The role of this Data122.
        :type: str
        """

        self._role = role

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this Data122.
        

        :return: The custom_fields of this Data122.
        :rtype: str
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this Data122.
        

        :param custom_fields: The custom_fields of this Data122.
        :type: str
        """

        self._custom_fields = custom_fields

    @property
    def tenant(self):
        """
        Gets the tenant of this Data122.
        

        :return: The tenant of this Data122.
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """
        Sets the tenant of this Data122.
        

        :param tenant: The tenant of this Data122.
        :type: str
        """

        self._tenant = tenant

    @property
    def description(self):
        """
        Gets the description of this Data122.
        

        :return: The description of this Data122.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Data122.
        

        :param description: The description of this Data122.
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
        if not isinstance(other, Data122):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
