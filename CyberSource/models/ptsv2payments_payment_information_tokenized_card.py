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


class Ptsv2paymentsPaymentInformationTokenizedCard(object):
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
        'number': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str',
        'type': 'str',
        'cryptogram': 'str',
        'requestor_id': 'str',
        'transaction_type': 'str',
        'assurance_level': 'str',
        'storage_method': 'str',
        'security_code': 'str'
    }

    attribute_map = {
        'number': 'number',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'type': 'type',
        'cryptogram': 'cryptogram',
        'requestor_id': 'requestorId',
        'transaction_type': 'transactionType',
        'assurance_level': 'assuranceLevel',
        'storage_method': 'storageMethod',
        'security_code': 'securityCode'
    }

    def __init__(self, number=None, expiration_month=None, expiration_year=None, type=None, cryptogram=None, requestor_id=None, transaction_type=None, assurance_level=None, storage_method=None, security_code=None):
        """
        Ptsv2paymentsPaymentInformationTokenizedCard - a model defined in Swagger
        """

        self._number = None
        self._expiration_month = None
        self._expiration_year = None
        self._type = None
        self._cryptogram = None
        self._requestor_id = None
        self._transaction_type = None
        self._assurance_level = None
        self._storage_method = None
        self._security_code = None

        if number is not None:
          self.number = number
        if expiration_month is not None:
          self.expiration_month = expiration_month
        if expiration_year is not None:
          self.expiration_year = expiration_year
        if type is not None:
          self.type = type
        if cryptogram is not None:
          self.cryptogram = cryptogram
        if requestor_id is not None:
          self.requestor_id = requestor_id
        if transaction_type is not None:
          self.transaction_type = transaction_type
        if assurance_level is not None:
          self.assurance_level = assurance_level
        if storage_method is not None:
          self.storage_method = storage_method
        if security_code is not None:
          self.security_code = security_code

    @property
    def number(self):
        """
        Gets the number of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Customer’s payment network token value. 

        :return: The number of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Customer’s payment network token value. 

        :param number: The number of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """
        if number is not None and len(number) > 20:
            raise ValueError("Invalid value for `number`, length must be less than or equal to `20`")

        self._number = number

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this Ptsv2paymentsPaymentInformationTokenizedCard.
        One of two possible meanings: - The two-digit month in which a token expires. - The two-digit month in which a card expires. Format: `MM` Possible values: `01` through `12`  **NOTE** The meaning of this field is dependent on the payment processor that is returning the value in an authorization reply. Please see the processor-specific details below.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`01` through `12`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (`card_type=039`), if there is no expiration date on the card, use `12`.\\ **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Samsung Pay and Apple Pay Month in which the token expires. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.  For processor-specific information, see the `customer_cc_expmo` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The expiration_month of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this Ptsv2paymentsPaymentInformationTokenizedCard.
        One of two possible meanings: - The two-digit month in which a token expires. - The two-digit month in which a card expires. Format: `MM` Possible values: `01` through `12`  **NOTE** The meaning of this field is dependent on the payment processor that is returning the value in an authorization reply. Please see the processor-specific details below.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`01` through `12`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (`card_type=039`), if there is no expiration date on the card, use `12`.\\ **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Samsung Pay and Apple Pay Month in which the token expires. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.  For processor-specific information, see the `customer_cc_expmo` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param expiration_month: The expiration_month of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """
        if expiration_month is not None and len(expiration_month) > 2:
            raise ValueError("Invalid value for `expiration_month`, length must be less than or equal to `2`")

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this Ptsv2paymentsPaymentInformationTokenizedCard.
        One of two possible meanings: - The four-digit year in which a token expires. - The four-digit year in which a card expires. Format: `YYYY` Possible values: `1900` through `3000` Data type: Non-negative integer  **NOTE** The meaning of this field is dependent on the payment processor that is returning the value in an authorization reply. Please see the processor-specific details below.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (1900 through 3000) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (`card_ type=039`), if there is no expiration date on the card, use `2021`.  #### FDC Nashville Global and FDMS South You can send in 2 digits or 4 digits. When you send in 2 digits, they must be the last 2 digits of the year.  #### Samsung Pay and Apple Pay Year in which the token expires. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  For processor-specific information, see the `customer_cc_expyr` or `token_expiration_year` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The expiration_year of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this Ptsv2paymentsPaymentInformationTokenizedCard.
        One of two possible meanings: - The four-digit year in which a token expires. - The four-digit year in which a card expires. Format: `YYYY` Possible values: `1900` through `3000` Data type: Non-negative integer  **NOTE** The meaning of this field is dependent on the payment processor that is returning the value in an authorization reply. Please see the processor-specific details below.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (1900 through 3000) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (`card_ type=039`), if there is no expiration date on the card, use `2021`.  #### FDC Nashville Global and FDMS South You can send in 2 digits or 4 digits. When you send in 2 digits, they must be the last 2 digits of the year.  #### Samsung Pay and Apple Pay Year in which the token expires. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  For processor-specific information, see the `customer_cc_expyr` or `token_expiration_year` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param expiration_year: The expiration_year of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """
        if expiration_year is not None and len(expiration_year) > 4:
            raise ValueError("Invalid value for `expiration_year`, length must be less than or equal to `4`")

        self._expiration_year = expiration_year

    @property
    def type(self):
        """
        Gets the type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Three-digit value that indicates the card type.  Type of card to authorize. - 001 Visa - 002 Mastercard - 003 Amex - 004 Discover - 005: Diners Club - 007: JCB - 024: Maestro (UK Domestic) - 036: Cartes Bancaires - 039 Encoded account number - 042: Maestro (International)  For the complete list of possible values, see `card_type` field description in the [Credit Card Services Using the SCMP API Guide.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Three-digit value that indicates the card type.  Type of card to authorize. - 001 Visa - 002 Mastercard - 003 Amex - 004 Discover - 005: Diners Club - 007: JCB - 024: Maestro (UK Domestic) - 036: Cartes Bancaires - 039 Encoded account number - 042: Maestro (International)  For the complete list of possible values, see `card_type` field description in the [Credit Card Services Using the SCMP API Guide.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param type: The type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """

        self._type = type

    @property
    def cryptogram(self):
        """
        Gets the cryptogram of this Ptsv2paymentsPaymentInformationTokenizedCard.
        This field is used internally.

        :return: The cryptogram of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._cryptogram

    @cryptogram.setter
    def cryptogram(self, cryptogram):
        """
        Sets the cryptogram of this Ptsv2paymentsPaymentInformationTokenizedCard.
        This field is used internally.

        :param cryptogram: The cryptogram of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """
        if cryptogram is not None and len(cryptogram) > 40:
            raise ValueError("Invalid value for `cryptogram`, length must be less than or equal to `40`")

        self._cryptogram = cryptogram

    @property
    def requestor_id(self):
        """
        Gets the requestor_id of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Value that identifies your business and indicates that the cardholder’s account number is tokenized. This value is assigned by the token service provider and is unique within the token service provider’s database.  **Note** This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**. 

        :return: The requestor_id of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._requestor_id

    @requestor_id.setter
    def requestor_id(self, requestor_id):
        """
        Sets the requestor_id of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Value that identifies your business and indicates that the cardholder’s account number is tokenized. This value is assigned by the token service provider and is unique within the token service provider’s database.  **Note** This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**. 

        :param requestor_id: The requestor_id of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """
        if requestor_id is not None and len(requestor_id) > 11:
            raise ValueError("Invalid value for `requestor_id`, length must be less than or equal to `11`")

        self._requestor_id = requestor_id

    @property
    def transaction_type(self):
        """
        Gets the transaction_type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Type of transaction that provided the token data. This value does not specify the token service provider; it specifies the entity that provided you with information about the token.  Set the value for this field to 1. An application on the customer’s mobile device provided the token data. 

        :return: The transaction_type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """
        Sets the transaction_type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Type of transaction that provided the token data. This value does not specify the token service provider; it specifies the entity that provided you with information about the token.  Set the value for this field to 1. An application on the customer’s mobile device provided the token data. 

        :param transaction_type: The transaction_type of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """
        if transaction_type is not None and len(transaction_type) > 1:
            raise ValueError("Invalid value for `transaction_type`, length must be less than or equal to `1`")

        self._transaction_type = transaction_type

    @property
    def assurance_level(self):
        """
        Gets the assurance_level of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Confidence level of the tokenization. This value is assigned by the token service provider.  **Note** This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**. 

        :return: The assurance_level of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._assurance_level

    @assurance_level.setter
    def assurance_level(self, assurance_level):
        """
        Sets the assurance_level of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Confidence level of the tokenization. This value is assigned by the token service provider.  **Note** This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**. 

        :param assurance_level: The assurance_level of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """
        if assurance_level is not None and len(assurance_level) > 2:
            raise ValueError("Invalid value for `assurance_level`, length must be less than or equal to `2`")

        self._assurance_level = assurance_level

    @property
    def storage_method(self):
        """
        Gets the storage_method of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Type of technology used in the device to store token data. Possible values:  - `001`: Secure Element (SE). Smart card or memory with restricted access and encryption to prevent data tampering. For storing payment    credentials, a SE is tested against a set of requirements defined by the payment networks.     **Note** This field is supported only for _FDC Compass_.  - 002: Host Card Emulation (HCE). Emulation of a smart card by using software to create a virtual and exact representation of the card. Sensitive data is stored in a database that is hosted in the cloud. For storing payment credentials, a database must meet very stringent security requirements that exceed PCI DSS.  **Note** This field is supported only for _FDC Compass_. 

        :return: The storage_method of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._storage_method

    @storage_method.setter
    def storage_method(self, storage_method):
        """
        Sets the storage_method of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Type of technology used in the device to store token data. Possible values:  - `001`: Secure Element (SE). Smart card or memory with restricted access and encryption to prevent data tampering. For storing payment    credentials, a SE is tested against a set of requirements defined by the payment networks.     **Note** This field is supported only for _FDC Compass_.  - 002: Host Card Emulation (HCE). Emulation of a smart card by using software to create a virtual and exact representation of the card. Sensitive data is stored in a database that is hosted in the cloud. For storing payment credentials, a database must meet very stringent security requirements that exceed PCI DSS.  **Note** This field is supported only for _FDC Compass_. 

        :param storage_method: The storage_method of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """
        if storage_method is not None and len(storage_method) > 3:
            raise ValueError("Invalid value for `storage_method`, length must be less than or equal to `3`")

        self._storage_method = storage_method

    @property
    def security_code(self):
        """
        Gets the security_code of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Card Verification Number (CVN).  #### Ingenico ePayments Do not include this field when **commerceIndicator=recurring**. **Note** Ingenico ePayments was previously called _Global Collect_.  For details, see `customer_cc_cv_number` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The security_code of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """
        Sets the security_code of this Ptsv2paymentsPaymentInformationTokenizedCard.
        Card Verification Number (CVN).  #### Ingenico ePayments Do not include this field when **commerceIndicator=recurring**. **Note** Ingenico ePayments was previously called _Global Collect_.  For details, see `customer_cc_cv_number` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param security_code: The security_code of this Ptsv2paymentsPaymentInformationTokenizedCard.
        :type: str
        """
        if security_code is not None and len(security_code) > 4:
            raise ValueError("Invalid value for `security_code`, length must be less than or equal to `4`")

        self._security_code = security_code

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
        if not isinstance(other, Ptsv2paymentsPaymentInformationTokenizedCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
