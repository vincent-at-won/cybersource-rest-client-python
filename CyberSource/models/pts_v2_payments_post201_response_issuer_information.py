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


class PtsV2PaymentsPost201ResponseIssuerInformation(object):
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
        'country': 'str',
        'discretionary_data': 'str',
        'country_specific_discretionary_data': 'str',
        'response_code': 'str'
    }

    attribute_map = {
        'country': 'country',
        'discretionary_data': 'discretionaryData',
        'country_specific_discretionary_data': 'countrySpecificDiscretionaryData',
        'response_code': 'responseCode'
    }

    def __init__(self, country=None, discretionary_data=None, country_specific_discretionary_data=None, response_code=None):
        """
        PtsV2PaymentsPost201ResponseIssuerInformation - a model defined in Swagger
        """

        self._country = None
        self._discretionary_data = None
        self._country_specific_discretionary_data = None
        self._response_code = None

        if country is not None:
          self.country = country
        if discretionary_data is not None:
          self.discretionary_data = discretionary_data
        if country_specific_discretionary_data is not None:
          self.country_specific_discretionary_data = country_specific_discretionary_data
        if response_code is not None:
          self.response_code = response_code

    @property
    def country(self):
        """
        Gets the country of this PtsV2PaymentsPost201ResponseIssuerInformation.
        Country in which the card was issued. This information enables you to determine whether the card was issued domestically or internationally. Use the two-character ISO Standard Country Codes.  This field is supported for Visa, Mastercard, Discover, Diners Club, JCB, and Maestro (International) on Chase Paymentech Solutions.  For details, see `auth_card_issuer_country` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The country of this PtsV2PaymentsPost201ResponseIssuerInformation.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this PtsV2PaymentsPost201ResponseIssuerInformation.
        Country in which the card was issued. This information enables you to determine whether the card was issued domestically or internationally. Use the two-character ISO Standard Country Codes.  This field is supported for Visa, Mastercard, Discover, Diners Club, JCB, and Maestro (International) on Chase Paymentech Solutions.  For details, see `auth_card_issuer_country` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param country: The country of this PtsV2PaymentsPost201ResponseIssuerInformation.
        :type: str
        """
        if country is not None and len(country) > 3:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `3`")

        self._country = country

    @property
    def discretionary_data(self):
        """
        Gets the discretionary_data of this PtsV2PaymentsPost201ResponseIssuerInformation.
        Data defined by the issuer.  The value for this reply field will probably be the same as the value that you submitted in the authorization request, but it is possible for the processor, issuer, or acquirer to modify the value.  This field is supported only for Visa transactions on **CyberSource through VisaNet**.  For details, see `issuer_additional_data` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The discretionary_data of this PtsV2PaymentsPost201ResponseIssuerInformation.
        :rtype: str
        """
        return self._discretionary_data

    @discretionary_data.setter
    def discretionary_data(self, discretionary_data):
        """
        Sets the discretionary_data of this PtsV2PaymentsPost201ResponseIssuerInformation.
        Data defined by the issuer.  The value for this reply field will probably be the same as the value that you submitted in the authorization request, but it is possible for the processor, issuer, or acquirer to modify the value.  This field is supported only for Visa transactions on **CyberSource through VisaNet**.  For details, see `issuer_additional_data` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param discretionary_data: The discretionary_data of this PtsV2PaymentsPost201ResponseIssuerInformation.
        :type: str
        """
        if discretionary_data is not None and len(discretionary_data) > 255:
            raise ValueError("Invalid value for `discretionary_data`, length must be less than or equal to `255`")

        self._discretionary_data = discretionary_data

    @property
    def country_specific_discretionary_data(self):
        """
        Gets the country_specific_discretionary_data of this PtsV2PaymentsPost201ResponseIssuerInformation.
        Data defined by the issuer.  This national use field contains two subfields for information unique to the processing of Visa transactions by members in Japan. This subfield contains the Katakana text to be printed on the receipt. For details, see `jpo_issuer_message` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The country_specific_discretionary_data of this PtsV2PaymentsPost201ResponseIssuerInformation.
        :rtype: str
        """
        return self._country_specific_discretionary_data

    @country_specific_discretionary_data.setter
    def country_specific_discretionary_data(self, country_specific_discretionary_data):
        """
        Sets the country_specific_discretionary_data of this PtsV2PaymentsPost201ResponseIssuerInformation.
        Data defined by the issuer.  This national use field contains two subfields for information unique to the processing of Visa transactions by members in Japan. This subfield contains the Katakana text to be printed on the receipt. For details, see `jpo_issuer_message` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param country_specific_discretionary_data: The country_specific_discretionary_data of this PtsV2PaymentsPost201ResponseIssuerInformation.
        :type: str
        """
        if country_specific_discretionary_data is not None and len(country_specific_discretionary_data) > 140:
            raise ValueError("Invalid value for `country_specific_discretionary_data`, length must be less than or equal to `140`")

        self._country_specific_discretionary_data = country_specific_discretionary_data

    @property
    def response_code(self):
        """
        Gets the response_code of this PtsV2PaymentsPost201ResponseIssuerInformation.
        Additional authorization code that must be printed on the receipt when returned by the processor.  This value is generated by the processor and is returned only for a successful transaction.  This field is supported only on FDC Nashville Global and SIX. 

        :return: The response_code of this PtsV2PaymentsPost201ResponseIssuerInformation.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this PtsV2PaymentsPost201ResponseIssuerInformation.
        Additional authorization code that must be printed on the receipt when returned by the processor.  This value is generated by the processor and is returned only for a successful transaction.  This field is supported only on FDC Nashville Global and SIX. 

        :param response_code: The response_code of this PtsV2PaymentsPost201ResponseIssuerInformation.
        :type: str
        """
        if response_code is not None and len(response_code) > 6:
            raise ValueError("Invalid value for `response_code`, length must be less than or equal to `6`")

        self._response_code = response_code

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseIssuerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
