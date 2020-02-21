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


class Ptsv2paymentsidcapturesTravelInformation(object):
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
        'agency': 'Ptsv2paymentsTravelInformationAgency',
        'lodging': 'Ptsv2paymentsTravelInformationLodging',
        'transit': 'Ptsv2paymentsTravelInformationTransit'
    }

    attribute_map = {
        'agency': 'agency',
        'lodging': 'lodging',
        'transit': 'transit'
    }

    def __init__(self, agency=None, lodging=None, transit=None):
        """
        Ptsv2paymentsidcapturesTravelInformation - a model defined in Swagger
        """

        self._agency = None
        self._lodging = None
        self._transit = None

        if agency is not None:
          self.agency = agency
        if lodging is not None:
          self.lodging = lodging
        if transit is not None:
          self.transit = transit

    @property
    def agency(self):
        """
        Gets the agency of this Ptsv2paymentsidcapturesTravelInformation.

        :return: The agency of this Ptsv2paymentsidcapturesTravelInformation.
        :rtype: Ptsv2paymentsTravelInformationAgency
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """
        Sets the agency of this Ptsv2paymentsidcapturesTravelInformation.

        :param agency: The agency of this Ptsv2paymentsidcapturesTravelInformation.
        :type: Ptsv2paymentsTravelInformationAgency
        """

        self._agency = agency

    @property
    def lodging(self):
        """
        Gets the lodging of this Ptsv2paymentsidcapturesTravelInformation.

        :return: The lodging of this Ptsv2paymentsidcapturesTravelInformation.
        :rtype: Ptsv2paymentsTravelInformationLodging
        """
        return self._lodging

    @lodging.setter
    def lodging(self, lodging):
        """
        Sets the lodging of this Ptsv2paymentsidcapturesTravelInformation.

        :param lodging: The lodging of this Ptsv2paymentsidcapturesTravelInformation.
        :type: Ptsv2paymentsTravelInformationLodging
        """

        self._lodging = lodging

    @property
    def transit(self):
        """
        Gets the transit of this Ptsv2paymentsidcapturesTravelInformation.

        :return: The transit of this Ptsv2paymentsidcapturesTravelInformation.
        :rtype: Ptsv2paymentsTravelInformationTransit
        """
        return self._transit

    @transit.setter
    def transit(self, transit):
        """
        Sets the transit of this Ptsv2paymentsidcapturesTravelInformation.

        :param transit: The transit of this Ptsv2paymentsidcapturesTravelInformation.
        :type: Ptsv2paymentsTravelInformationTransit
        """

        self._transit = transit

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
        if not isinstance(other, Ptsv2paymentsidcapturesTravelInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
