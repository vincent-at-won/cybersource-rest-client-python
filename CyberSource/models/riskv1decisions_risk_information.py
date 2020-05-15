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


class Riskv1decisionsRiskInformation(object):
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
        'profile': 'Ptsv2paymentsRiskInformationProfile',
        'event_type': 'str',
        'buyer_history': 'Ptsv2paymentsRiskInformationBuyerHistory'
    }

    attribute_map = {
        'profile': 'profile',
        'event_type': 'eventType',
        'buyer_history': 'buyerHistory'
    }

    def __init__(self, profile=None, event_type=None, buyer_history=None):
        """
        Riskv1decisionsRiskInformation - a model defined in Swagger
        """

        self._profile = None
        self._event_type = None
        self._buyer_history = None

        if profile is not None:
          self.profile = profile
        if event_type is not None:
          self.event_type = event_type
        if buyer_history is not None:
          self.buyer_history = buyer_history

    @property
    def profile(self):
        """
        Gets the profile of this Riskv1decisionsRiskInformation.

        :return: The profile of this Riskv1decisionsRiskInformation.
        :rtype: Ptsv2paymentsRiskInformationProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """
        Sets the profile of this Riskv1decisionsRiskInformation.

        :param profile: The profile of this Riskv1decisionsRiskInformation.
        :type: Ptsv2paymentsRiskInformationProfile
        """

        self._profile = profile

    @property
    def event_type(self):
        """
        Gets the event_type of this Riskv1decisionsRiskInformation.
        Specifies one of the following types of events: - login - account_creation - account_update For regular payment transactions, do not send this field. 

        :return: The event_type of this Riskv1decisionsRiskInformation.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this Riskv1decisionsRiskInformation.
        Specifies one of the following types of events: - login - account_creation - account_update For regular payment transactions, do not send this field. 

        :param event_type: The event_type of this Riskv1decisionsRiskInformation.
        :type: str
        """
        if event_type is not None and len(event_type) > 255:
            raise ValueError("Invalid value for `event_type`, length must be less than or equal to `255`")

        self._event_type = event_type

    @property
    def buyer_history(self):
        """
        Gets the buyer_history of this Riskv1decisionsRiskInformation.

        :return: The buyer_history of this Riskv1decisionsRiskInformation.
        :rtype: Ptsv2paymentsRiskInformationBuyerHistory
        """
        return self._buyer_history

    @buyer_history.setter
    def buyer_history(self, buyer_history):
        """
        Sets the buyer_history of this Riskv1decisionsRiskInformation.

        :param buyer_history: The buyer_history of this Riskv1decisionsRiskInformation.
        :type: Ptsv2paymentsRiskInformationBuyerHistory
        """

        self._buyer_history = buyer_history

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
        if not isinstance(other, Riskv1decisionsRiskInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
