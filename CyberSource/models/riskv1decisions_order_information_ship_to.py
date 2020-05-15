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


class Riskv1decisionsOrderInformationShipTo(object):
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
        'address1': 'str',
        'address2': 'str',
        'administrative_area': 'str',
        'country': 'str',
        'destination_types': 'str',
        'locality': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'phone_number': 'str',
        'postal_code': 'str',
        'destination_code': 'int',
        'method': 'str'
    }

    attribute_map = {
        'address1': 'address1',
        'address2': 'address2',
        'administrative_area': 'administrativeArea',
        'country': 'country',
        'destination_types': 'destinationTypes',
        'locality': 'locality',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'phone_number': 'phoneNumber',
        'postal_code': 'postalCode',
        'destination_code': 'destinationCode',
        'method': 'method'
    }

    def __init__(self, address1=None, address2=None, administrative_area=None, country=None, destination_types=None, locality=None, first_name=None, last_name=None, phone_number=None, postal_code=None, destination_code=None, method=None):
        """
        Riskv1decisionsOrderInformationShipTo - a model defined in Swagger
        """

        self._address1 = None
        self._address2 = None
        self._administrative_area = None
        self._country = None
        self._destination_types = None
        self._locality = None
        self._first_name = None
        self._last_name = None
        self._phone_number = None
        self._postal_code = None
        self._destination_code = None
        self._method = None

        if address1 is not None:
          self.address1 = address1
        if address2 is not None:
          self.address2 = address2
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if country is not None:
          self.country = country
        if destination_types is not None:
          self.destination_types = destination_types
        if locality is not None:
          self.locality = locality
        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name
        if phone_number is not None:
          self.phone_number = phone_number
        if postal_code is not None:
          self.postal_code = postal_code
        if destination_code is not None:
          self.destination_code = destination_code
        if method is not None:
          self.method = method

    @property
    def address1(self):
        """
        Gets the address1 of this Riskv1decisionsOrderInformationShipTo.
        First line of the shipping address.  Required field for authorization if any shipping address information is included in the request; otherwise, optional. 

        :return: The address1 of this Riskv1decisionsOrderInformationShipTo.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Riskv1decisionsOrderInformationShipTo.
        First line of the shipping address.  Required field for authorization if any shipping address information is included in the request; otherwise, optional. 

        :param address1: The address1 of this Riskv1decisionsOrderInformationShipTo.
        :type: str
        """
        if address1 is not None and len(address1) > 60:
            raise ValueError("Invalid value for `address1`, length must be less than or equal to `60`")

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this Riskv1decisionsOrderInformationShipTo.
        Second line of the shipping address.  Optional field. 

        :return: The address2 of this Riskv1decisionsOrderInformationShipTo.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this Riskv1decisionsOrderInformationShipTo.
        Second line of the shipping address.  Optional field. 

        :param address2: The address2 of this Riskv1decisionsOrderInformationShipTo.
        :type: str
        """
        if address2 is not None and len(address2) > 60:
            raise ValueError("Invalid value for `address2`, length must be less than or equal to `60`")

        self._address2 = address2

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Riskv1decisionsOrderInformationShipTo.
        State or province of the shipping address. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf)  Required field for authorization if any shipping address information is included in the request and shipping to the U.S. or Canada; otherwise, optional. 

        :return: The administrative_area of this Riskv1decisionsOrderInformationShipTo.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Riskv1decisionsOrderInformationShipTo.
        State or province of the shipping address. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf)  Required field for authorization if any shipping address information is included in the request and shipping to the U.S. or Canada; otherwise, optional. 

        :param administrative_area: The administrative_area of this Riskv1decisionsOrderInformationShipTo.
        :type: str
        """
        if administrative_area is not None and len(administrative_area) > 2:
            raise ValueError("Invalid value for `administrative_area`, length must be less than or equal to `2`")

        self._administrative_area = administrative_area

    @property
    def country(self):
        """
        Gets the country of this Riskv1decisionsOrderInformationShipTo.
        Country of the shipping address. Use the two-character [ISO Standard Country Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf)  Required field for authorization if any shipping address information is included in the request; otherwise, optional. 

        :return: The country of this Riskv1decisionsOrderInformationShipTo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Riskv1decisionsOrderInformationShipTo.
        Country of the shipping address. Use the two-character [ISO Standard Country Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf)  Required field for authorization if any shipping address information is included in the request; otherwise, optional. 

        :param country: The country of this Riskv1decisionsOrderInformationShipTo.
        :type: str
        """
        if country is not None and len(country) > 2:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `2`")

        self._country = country

    @property
    def destination_types(self):
        """
        Gets the destination_types of this Riskv1decisionsOrderInformationShipTo.
        Shipping destination of item. Example: Commercial, Residential, Store 

        :return: The destination_types of this Riskv1decisionsOrderInformationShipTo.
        :rtype: str
        """
        return self._destination_types

    @destination_types.setter
    def destination_types(self, destination_types):
        """
        Sets the destination_types of this Riskv1decisionsOrderInformationShipTo.
        Shipping destination of item. Example: Commercial, Residential, Store 

        :param destination_types: The destination_types of this Riskv1decisionsOrderInformationShipTo.
        :type: str
        """
        if destination_types is not None and len(destination_types) > 25:
            raise ValueError("Invalid value for `destination_types`, length must be less than or equal to `25`")

        self._destination_types = destination_types

    @property
    def locality(self):
        """
        Gets the locality of this Riskv1decisionsOrderInformationShipTo.
        City of the shipping address.  Required field for authorization if any shipping address information is included in the request and shipping to the U.S. or Canada; otherwise, optional. 

        :return: The locality of this Riskv1decisionsOrderInformationShipTo.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Riskv1decisionsOrderInformationShipTo.
        City of the shipping address.  Required field for authorization if any shipping address information is included in the request and shipping to the U.S. or Canada; otherwise, optional. 

        :param locality: The locality of this Riskv1decisionsOrderInformationShipTo.
        :type: str
        """
        if locality is not None and len(locality) > 50:
            raise ValueError("Invalid value for `locality`, length must be less than or equal to `50`")

        self._locality = locality

    @property
    def first_name(self):
        """
        Gets the first_name of this Riskv1decisionsOrderInformationShipTo.
        First name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field. 

        :return: The first_name of this Riskv1decisionsOrderInformationShipTo.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Riskv1decisionsOrderInformationShipTo.
        First name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field. 

        :param first_name: The first_name of this Riskv1decisionsOrderInformationShipTo.
        :type: str
        """
        if first_name is not None and len(first_name) > 60:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `60`")

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this Riskv1decisionsOrderInformationShipTo.
        Last name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field. 

        :return: The last_name of this Riskv1decisionsOrderInformationShipTo.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Riskv1decisionsOrderInformationShipTo.
        Last name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field. 

        :param last_name: The last_name of this Riskv1decisionsOrderInformationShipTo.
        :type: str
        """
        if last_name is not None and len(last_name) > 60:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `60`")

        self._last_name = last_name

    @property
    def phone_number(self):
        """
        Gets the phone_number of this Riskv1decisionsOrderInformationShipTo.
        Phone number associated with the shipping address.

        :return: The phone_number of this Riskv1decisionsOrderInformationShipTo.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this Riskv1decisionsOrderInformationShipTo.
        Phone number associated with the shipping address.

        :param phone_number: The phone_number of this Riskv1decisionsOrderInformationShipTo.
        :type: str
        """
        if phone_number is not None and len(phone_number) > 15:
            raise ValueError("Invalid value for `phone_number`, length must be less than or equal to `15`")

        self._phone_number = phone_number

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Riskv1decisionsOrderInformationShipTo.
        Postal code for the shipping address. The postal code must consist of 5 to 9 digits.  Required field for authorization if any shipping address information is included in the request and shipping to the U.S. or Canada; otherwise, optional.  When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits]  Example 12345-6789  When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][alpha][numeric]  Example A1B 2C3  #### American Express Direct Before sending the postal code to the processor, all nonalphanumeric characters are removed and, if the remaining value is longer than nine characters, the value is truncated starting from the right side. 

        :return: The postal_code of this Riskv1decisionsOrderInformationShipTo.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Riskv1decisionsOrderInformationShipTo.
        Postal code for the shipping address. The postal code must consist of 5 to 9 digits.  Required field for authorization if any shipping address information is included in the request and shipping to the U.S. or Canada; otherwise, optional.  When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits]  Example 12345-6789  When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][alpha][numeric]  Example A1B 2C3  #### American Express Direct Before sending the postal code to the processor, all nonalphanumeric characters are removed and, if the remaining value is longer than nine characters, the value is truncated starting from the right side. 

        :param postal_code: The postal_code of this Riskv1decisionsOrderInformationShipTo.
        :type: str
        """
        if postal_code is not None and len(postal_code) > 10:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `10`")

        self._postal_code = postal_code

    @property
    def destination_code(self):
        """
        Gets the destination_code of this Riskv1decisionsOrderInformationShipTo.
        Indicates destination chosen for the transaction. Possible values: - 01- Ship to cardholder billing address - 02- Ship to another verified address on file with merchant - 03- Ship to address that is different than billing address - 04- Ship to store (store address should be populated on request) - 05- Digital goods - 06- Travel and event tickets, not shipped - 07- Other 

        :return: The destination_code of this Riskv1decisionsOrderInformationShipTo.
        :rtype: int
        """
        return self._destination_code

    @destination_code.setter
    def destination_code(self, destination_code):
        """
        Sets the destination_code of this Riskv1decisionsOrderInformationShipTo.
        Indicates destination chosen for the transaction. Possible values: - 01- Ship to cardholder billing address - 02- Ship to another verified address on file with merchant - 03- Ship to address that is different than billing address - 04- Ship to store (store address should be populated on request) - 05- Digital goods - 06- Travel and event tickets, not shipped - 07- Other 

        :param destination_code: The destination_code of this Riskv1decisionsOrderInformationShipTo.
        :type: int
        """

        self._destination_code = destination_code

    @property
    def method(self):
        """
        Gets the method of this Riskv1decisionsOrderInformationShipTo.
        Shipping method for the product. Possible values: - lowcost: Lowest-cost service - sameday: Courier or same-day service - oneday: Next-day or overnight service - twoday: Two-day service - threeday: Three-day service - pickup: Store pick-up - other: Other shipping method - none: No shipping method because product is a service or subscription Required for American Express SafeKey (U.S.). 

        :return: The method of this Riskv1decisionsOrderInformationShipTo.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this Riskv1decisionsOrderInformationShipTo.
        Shipping method for the product. Possible values: - lowcost: Lowest-cost service - sameday: Courier or same-day service - oneday: Next-day or overnight service - twoday: Two-day service - threeday: Three-day service - pickup: Store pick-up - other: Other shipping method - none: No shipping method because product is a service or subscription Required for American Express SafeKey (U.S.). 

        :param method: The method of this Riskv1decisionsOrderInformationShipTo.
        :type: str
        """
        if method is not None and len(method) > 10:
            raise ValueError("Invalid value for `method`, length must be less than or equal to `10`")

        self._method = method

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
        if not isinstance(other, Riskv1decisionsOrderInformationShipTo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
