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


class Data(object):
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
        'pp_info': 'str',
        'site': 'str',
        'term_side': 'str',
        'xconnect_id': 'str',
        'circuit': 'str',
        'port_speed': 'int',
        'interface': 'str',
        'upstream_speed': 'int'
    }

    attribute_map = {
        'pp_info': 'pp_info',
        'site': 'site',
        'term_side': 'term_side',
        'xconnect_id': 'xconnect_id',
        'circuit': 'circuit',
        'port_speed': 'port_speed',
        'interface': 'interface',
        'upstream_speed': 'upstream_speed'
    }

    def __init__(self, pp_info=None, site=None, term_side=None, xconnect_id=None, circuit=None, port_speed=None, interface=None, upstream_speed=None):
        """
        Data - a model defined in Swagger
        """

        self._pp_info = None
        self._site = None
        self._term_side = None
        self._xconnect_id = None
        self._circuit = None
        self._port_speed = None
        self._interface = None
        self._upstream_speed = None

        if pp_info is not None:
          self.pp_info = pp_info
        self.site = site
        self.term_side = term_side
        if xconnect_id is not None:
          self.xconnect_id = xconnect_id
        self.circuit = circuit
        self.port_speed = port_speed
        if interface is not None:
          self.interface = interface
        if upstream_speed is not None:
          self.upstream_speed = upstream_speed

    @property
    def pp_info(self):
        """
        Gets the pp_info of this Data.
        

        :return: The pp_info of this Data.
        :rtype: str
        """
        return self._pp_info

    @pp_info.setter
    def pp_info(self, pp_info):
        """
        Sets the pp_info of this Data.
        

        :param pp_info: The pp_info of this Data.
        :type: str
        """

        self._pp_info = pp_info

    @property
    def site(self):
        """
        Gets the site of this Data.
        

        :return: The site of this Data.
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        """
        Sets the site of this Data.
        

        :param site: The site of this Data.
        :type: str
        """
        if site is None:
            raise ValueError("Invalid value for `site`, must not be `None`")

        self._site = site

    @property
    def term_side(self):
        """
        Gets the term_side of this Data.
        

        :return: The term_side of this Data.
        :rtype: str
        """
        return self._term_side

    @term_side.setter
    def term_side(self, term_side):
        """
        Sets the term_side of this Data.
        

        :param term_side: The term_side of this Data.
        :type: str
        """
        if term_side is None:
            raise ValueError("Invalid value for `term_side`, must not be `None`")

        self._term_side = term_side

    @property
    def xconnect_id(self):
        """
        Gets the xconnect_id of this Data.
        

        :return: The xconnect_id of this Data.
        :rtype: str
        """
        return self._xconnect_id

    @xconnect_id.setter
    def xconnect_id(self, xconnect_id):
        """
        Sets the xconnect_id of this Data.
        

        :param xconnect_id: The xconnect_id of this Data.
        :type: str
        """

        self._xconnect_id = xconnect_id

    @property
    def circuit(self):
        """
        Gets the circuit of this Data.
        

        :return: The circuit of this Data.
        :rtype: str
        """
        return self._circuit

    @circuit.setter
    def circuit(self, circuit):
        """
        Sets the circuit of this Data.
        

        :param circuit: The circuit of this Data.
        :type: str
        """
        if circuit is None:
            raise ValueError("Invalid value for `circuit`, must not be `None`")

        self._circuit = circuit

    @property
    def port_speed(self):
        """
        Gets the port_speed of this Data.
        

        :return: The port_speed of this Data.
        :rtype: int
        """
        return self._port_speed

    @port_speed.setter
    def port_speed(self, port_speed):
        """
        Sets the port_speed of this Data.
        

        :param port_speed: The port_speed of this Data.
        :type: int
        """
        if port_speed is None:
            raise ValueError("Invalid value for `port_speed`, must not be `None`")

        self._port_speed = port_speed

    @property
    def interface(self):
        """
        Gets the interface of this Data.
        

        :return: The interface of this Data.
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """
        Sets the interface of this Data.
        

        :param interface: The interface of this Data.
        :type: str
        """

        self._interface = interface

    @property
    def upstream_speed(self):
        """
        Gets the upstream_speed of this Data.
        Upstream speed, if different from port speed

        :return: The upstream_speed of this Data.
        :rtype: int
        """
        return self._upstream_speed

    @upstream_speed.setter
    def upstream_speed(self, upstream_speed):
        """
        Sets the upstream_speed of this Data.
        Upstream speed, if different from port speed

        :param upstream_speed: The upstream_speed of this Data.
        :type: int
        """

        self._upstream_speed = upstream_speed

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
        if not isinstance(other, Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other