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


class Data86(object):
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
        'physical_address': 'str',
        'name': 'str',
        'facility': 'str',
        'region': 'str',
        'comments': 'str',
        'slug': 'str',
        'contact_email': 'str',
        'custom_fields': 'str',
        'shipping_address': 'str',
        'contact_name': 'str',
        'contact_phone': 'str',
        'asn': 'int',
        'tenant': 'str'
    }

    attribute_map = {
        'physical_address': 'physical_address',
        'name': 'name',
        'facility': 'facility',
        'region': 'region',
        'comments': 'comments',
        'slug': 'slug',
        'contact_email': 'contact_email',
        'custom_fields': 'custom_fields',
        'shipping_address': 'shipping_address',
        'contact_name': 'contact_name',
        'contact_phone': 'contact_phone',
        'asn': 'asn',
        'tenant': 'tenant'
    }

    def __init__(self, physical_address=None, name=None, facility=None, region=None, comments=None, slug=None, contact_email=None, custom_fields=None, shipping_address=None, contact_name=None, contact_phone=None, asn=None, tenant=None):
        """
        Data86 - a model defined in Swagger
        """

        self._physical_address = None
        self._name = None
        self._facility = None
        self._region = None
        self._comments = None
        self._slug = None
        self._contact_email = None
        self._custom_fields = None
        self._shipping_address = None
        self._contact_name = None
        self._contact_phone = None
        self._asn = None
        self._tenant = None

        if physical_address is not None:
          self.physical_address = physical_address
        if name is not None:
          self.name = name
        if facility is not None:
          self.facility = facility
        if region is not None:
          self.region = region
        if comments is not None:
          self.comments = comments
        if slug is not None:
          self.slug = slug
        if contact_email is not None:
          self.contact_email = contact_email
        if custom_fields is not None:
          self.custom_fields = custom_fields
        if shipping_address is not None:
          self.shipping_address = shipping_address
        if contact_name is not None:
          self.contact_name = contact_name
        if contact_phone is not None:
          self.contact_phone = contact_phone
        if asn is not None:
          self.asn = asn
        if tenant is not None:
          self.tenant = tenant

    @property
    def physical_address(self):
        """
        Gets the physical_address of this Data86.
        

        :return: The physical_address of this Data86.
        :rtype: str
        """
        return self._physical_address

    @physical_address.setter
    def physical_address(self, physical_address):
        """
        Sets the physical_address of this Data86.
        

        :param physical_address: The physical_address of this Data86.
        :type: str
        """

        self._physical_address = physical_address

    @property
    def name(self):
        """
        Gets the name of this Data86.
        

        :return: The name of this Data86.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Data86.
        

        :param name: The name of this Data86.
        :type: str
        """

        self._name = name

    @property
    def facility(self):
        """
        Gets the facility of this Data86.
        

        :return: The facility of this Data86.
        :rtype: str
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """
        Sets the facility of this Data86.
        

        :param facility: The facility of this Data86.
        :type: str
        """

        self._facility = facility

    @property
    def region(self):
        """
        Gets the region of this Data86.
        

        :return: The region of this Data86.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this Data86.
        

        :param region: The region of this Data86.
        :type: str
        """

        self._region = region

    @property
    def comments(self):
        """
        Gets the comments of this Data86.
        

        :return: The comments of this Data86.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this Data86.
        

        :param comments: The comments of this Data86.
        :type: str
        """

        self._comments = comments

    @property
    def slug(self):
        """
        Gets the slug of this Data86.
        

        :return: The slug of this Data86.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """
        Sets the slug of this Data86.
        

        :param slug: The slug of this Data86.
        :type: str
        """

        self._slug = slug

    @property
    def contact_email(self):
        """
        Gets the contact_email of this Data86.
        

        :return: The contact_email of this Data86.
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """
        Sets the contact_email of this Data86.
        

        :param contact_email: The contact_email of this Data86.
        :type: str
        """

        self._contact_email = contact_email

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this Data86.
        

        :return: The custom_fields of this Data86.
        :rtype: str
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this Data86.
        

        :param custom_fields: The custom_fields of this Data86.
        :type: str
        """

        self._custom_fields = custom_fields

    @property
    def shipping_address(self):
        """
        Gets the shipping_address of this Data86.
        

        :return: The shipping_address of this Data86.
        :rtype: str
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """
        Sets the shipping_address of this Data86.
        

        :param shipping_address: The shipping_address of this Data86.
        :type: str
        """

        self._shipping_address = shipping_address

    @property
    def contact_name(self):
        """
        Gets the contact_name of this Data86.
        

        :return: The contact_name of this Data86.
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """
        Sets the contact_name of this Data86.
        

        :param contact_name: The contact_name of this Data86.
        :type: str
        """

        self._contact_name = contact_name

    @property
    def contact_phone(self):
        """
        Gets the contact_phone of this Data86.
        

        :return: The contact_phone of this Data86.
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """
        Sets the contact_phone of this Data86.
        

        :param contact_phone: The contact_phone of this Data86.
        :type: str
        """

        self._contact_phone = contact_phone

    @property
    def asn(self):
        """
        Gets the asn of this Data86.
        

        :return: The asn of this Data86.
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """
        Sets the asn of this Data86.
        

        :param asn: The asn of this Data86.
        :type: int
        """

        self._asn = asn

    @property
    def tenant(self):
        """
        Gets the tenant of this Data86.
        

        :return: The tenant of this Data86.
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """
        Sets the tenant of this Data86.
        

        :param tenant: The tenant of this Data86.
        :type: str
        """

        self._tenant = tenant

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
        if not isinstance(other, Data86):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
