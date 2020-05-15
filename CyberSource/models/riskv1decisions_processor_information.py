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


class Riskv1decisionsProcessorInformation(object):
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
        'avs': 'Riskv1decisionsProcessorInformationAvs',
        'card_verification': 'Riskv1decisionsProcessorInformationCardVerification'
    }

    attribute_map = {
        'avs': 'avs',
        'card_verification': 'cardVerification'
    }

    def __init__(self, avs=None, card_verification=None):
        """
        Riskv1decisionsProcessorInformation - a model defined in Swagger
        """

        self._avs = None
        self._card_verification = None

        if avs is not None:
          self.avs = avs
        if card_verification is not None:
          self.card_verification = card_verification

    @property
    def avs(self):
        """
        Gets the avs of this Riskv1decisionsProcessorInformation.

        :return: The avs of this Riskv1decisionsProcessorInformation.
        :rtype: Riskv1decisionsProcessorInformationAvs
        """
        return self._avs

    @avs.setter
    def avs(self, avs):
        """
        Sets the avs of this Riskv1decisionsProcessorInformation.

        :param avs: The avs of this Riskv1decisionsProcessorInformation.
        :type: Riskv1decisionsProcessorInformationAvs
        """

        self._avs = avs

    @property
    def card_verification(self):
        """
        Gets the card_verification of this Riskv1decisionsProcessorInformation.

        :return: The card_verification of this Riskv1decisionsProcessorInformation.
        :rtype: Riskv1decisionsProcessorInformationCardVerification
        """
        return self._card_verification

    @card_verification.setter
    def card_verification(self, card_verification):
        """
        Sets the card_verification of this Riskv1decisionsProcessorInformation.

        :param card_verification: The card_verification of this Riskv1decisionsProcessorInformation.
        :type: Riskv1decisionsProcessorInformationCardVerification
        """

        self._card_verification = card_verification

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
        if not isinstance(other, Riskv1decisionsProcessorInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
