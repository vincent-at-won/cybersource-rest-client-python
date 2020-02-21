# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Riskv1liststypeentriesOrderInformation(object):
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
        'address': 'Riskv1liststypeentriesOrderInformationAddress',
        'bill_to': 'Riskv1liststypeentriesOrderInformationBillTo',
        'ship_to': 'Riskv1liststypeentriesOrderInformationShipTo',
        'line_items': 'list[Riskv1liststypeentriesOrderInformationLineItems]'
    }

    attribute_map = {
        'address': 'address',
        'bill_to': 'billTo',
        'ship_to': 'shipTo',
        'line_items': 'lineItems'
    }

    def __init__(self, address=None, bill_to=None, ship_to=None, line_items=None):
        """
        Riskv1liststypeentriesOrderInformation - a model defined in Swagger
        """

        self._address = None
        self._bill_to = None
        self._ship_to = None
        self._line_items = None

        if address is not None:
          self.address = address
        if bill_to is not None:
          self.bill_to = bill_to
        if ship_to is not None:
          self.ship_to = ship_to
        if line_items is not None:
          self.line_items = line_items

    @property
    def address(self):
        """
        Gets the address of this Riskv1liststypeentriesOrderInformation.

        :return: The address of this Riskv1liststypeentriesOrderInformation.
        :rtype: Riskv1liststypeentriesOrderInformationAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Riskv1liststypeentriesOrderInformation.

        :param address: The address of this Riskv1liststypeentriesOrderInformation.
        :type: Riskv1liststypeentriesOrderInformationAddress
        """

        self._address = address

    @property
    def bill_to(self):
        """
        Gets the bill_to of this Riskv1liststypeentriesOrderInformation.

        :return: The bill_to of this Riskv1liststypeentriesOrderInformation.
        :rtype: Riskv1liststypeentriesOrderInformationBillTo
        """
        return self._bill_to

    @bill_to.setter
    def bill_to(self, bill_to):
        """
        Sets the bill_to of this Riskv1liststypeentriesOrderInformation.

        :param bill_to: The bill_to of this Riskv1liststypeentriesOrderInformation.
        :type: Riskv1liststypeentriesOrderInformationBillTo
        """

        self._bill_to = bill_to

    @property
    def ship_to(self):
        """
        Gets the ship_to of this Riskv1liststypeentriesOrderInformation.

        :return: The ship_to of this Riskv1liststypeentriesOrderInformation.
        :rtype: Riskv1liststypeentriesOrderInformationShipTo
        """
        return self._ship_to

    @ship_to.setter
    def ship_to(self, ship_to):
        """
        Sets the ship_to of this Riskv1liststypeentriesOrderInformation.

        :param ship_to: The ship_to of this Riskv1liststypeentriesOrderInformation.
        :type: Riskv1liststypeentriesOrderInformationShipTo
        """

        self._ship_to = ship_to

    @property
    def line_items(self):
        """
        Gets the line_items of this Riskv1liststypeentriesOrderInformation.
        This array contains detailed information about individual products in the order.

        :return: The line_items of this Riskv1liststypeentriesOrderInformation.
        :rtype: list[Riskv1liststypeentriesOrderInformationLineItems]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """
        Sets the line_items of this Riskv1liststypeentriesOrderInformation.
        This array contains detailed information about individual products in the order.

        :param line_items: The line_items of this Riskv1liststypeentriesOrderInformation.
        :type: list[Riskv1liststypeentriesOrderInformationLineItems]
        """

        self._line_items = line_items

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
        if not isinstance(other, Riskv1liststypeentriesOrderInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
