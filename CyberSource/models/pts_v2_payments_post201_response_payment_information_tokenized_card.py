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


class PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard(object):
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
        'prefix': 'str',
        'suffix': 'str',
        'type': 'str',
        'assurance_level': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str',
        'requestor_id': 'str'
    }

    attribute_map = {
        'prefix': 'prefix',
        'suffix': 'suffix',
        'type': 'type',
        'assurance_level': 'assuranceLevel',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'requestor_id': 'requestorId'
    }

    def __init__(self, prefix=None, suffix=None, type=None, assurance_level=None, expiration_month=None, expiration_year=None, requestor_id=None):
        """
        PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard - a model defined in Swagger
        """

        self._prefix = None
        self._suffix = None
        self._type = None
        self._assurance_level = None
        self._expiration_month = None
        self._expiration_year = None
        self._requestor_id = None

        if prefix is not None:
          self.prefix = prefix
        if suffix is not None:
          self.suffix = suffix
        if type is not None:
          self.type = type
        if assurance_level is not None:
          self.assurance_level = assurance_level
        if expiration_month is not None:
          self.expiration_month = expiration_month
        if expiration_year is not None:
          self.expiration_year = expiration_year
        if requestor_id is not None:
          self.requestor_id = requestor_id

    @property
    def prefix(self):
        """
        Gets the prefix of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        First six digits of token. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.  For details, see `token_prefix` field description in [Google Pay Using the SCMP API.] (https://apps.cybersource.com/library/documentation/dev_guides/Google_Pay_SCMP_API/html/) 

        :return: The prefix of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        First six digits of token. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.  For details, see `token_prefix` field description in [Google Pay Using the SCMP API.] (https://apps.cybersource.com/library/documentation/dev_guides/Google_Pay_SCMP_API/html/) 

        :param prefix: The prefix of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        :type: str
        """
        if prefix is not None and len(prefix) > 6:
            raise ValueError("Invalid value for `prefix`, length must be less than or equal to `6`")

        self._prefix = prefix

    @property
    def suffix(self):
        """
        Gets the suffix of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        Last four digits of token. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.  For details, see `token_suffix` field description in [Google Pay Using the SCMP API.] (https://apps.cybersource.com/library/documentation/dev_guides/Google_Pay_SCMP_API/html/) 

        :return: The suffix of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        Last four digits of token. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.  For details, see `token_suffix` field description in [Google Pay Using the SCMP API.] (https://apps.cybersource.com/library/documentation/dev_guides/Google_Pay_SCMP_API/html/) 

        :param suffix: The suffix of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        :type: str
        """
        if suffix is not None and len(suffix) > 4:
            raise ValueError("Invalid value for `suffix`, length must be less than or equal to `4`")

        self._suffix = suffix

    @property
    def type(self):
        """
        Gets the type of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        Three-digit value that indicates the card type.  **IMPORTANT** It is strongly recommended that you include the card type field in request messages even if it is optional for your processor and card type. Omitting the card type can cause the transaction to be processed with the wrong card type.  Possible values: - `001`: Visa. For card-present transactions on all processors except SIX, the Visa Electron card type is processed the same way that the Visa debit card is processed. Use card type value `001` for Visa Electron. - `002`: Mastercard, Eurocard[^1], which is a European regional brand of Mastercard. - `003`: American Express - `004`: Discover - `005`: Diners Club - `006`: Carte Blanche[^1] - `007`: JCB[^1] - `014`: Enroute[^1] - `021`: JAL[^1] - `024`: Maestro (UK Domestic)[^1] - `031`: Delta[^1]: Use this value only for Ingenico ePayments. For other processors, use `001` for all Visa card types. - `033`: Visa Electron[^1]. Use this value only for Ingenico ePayments and SIX. For other processors, use `001` for all Visa card types. - `034`: Dankort[^1] - `036`: Cartes Bancaires[^1] - `037`: Carta Si[^1] - `039`: Encoded account number[^1] - `040`: UATP[^1] - `042`: Maestro (International)[^1] - `050`: Hipercard[^2,3] - `051`: Aura - `054`: Elo[^3] - `062`: China UnionPay  [^1]: For this card type, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in your request for an authorization or a stand-alone credit. [^2]: For this card type on Cielo 3.0, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. This card type is not supported on Cielo 1.5. [^3]: For this card type on Getnet and Rede, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit.  #### Used by **Authorization** Required for Carte Blanche and JCB. Optional for all other card types.  #### Card Present reply This field is included in the reply message when the client software that is installed on the POS terminal uses the token management service (TMS) to retrieve tokenized payment details. You must contact customer support to have your account enabled to receive these fields in the credit reply message.  Returned by the Credit service.  This reply field is only supported by the following processors: - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - OmniPay Direct - SIX  #### GPX This field only supports transactions from the following card types: - Visa - Mastercard - AMEX - Discover - Diners - JCB - Union Pay International 

        :return: The type of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        Three-digit value that indicates the card type.  **IMPORTANT** It is strongly recommended that you include the card type field in request messages even if it is optional for your processor and card type. Omitting the card type can cause the transaction to be processed with the wrong card type.  Possible values: - `001`: Visa. For card-present transactions on all processors except SIX, the Visa Electron card type is processed the same way that the Visa debit card is processed. Use card type value `001` for Visa Electron. - `002`: Mastercard, Eurocard[^1], which is a European regional brand of Mastercard. - `003`: American Express - `004`: Discover - `005`: Diners Club - `006`: Carte Blanche[^1] - `007`: JCB[^1] - `014`: Enroute[^1] - `021`: JAL[^1] - `024`: Maestro (UK Domestic)[^1] - `031`: Delta[^1]: Use this value only for Ingenico ePayments. For other processors, use `001` for all Visa card types. - `033`: Visa Electron[^1]. Use this value only for Ingenico ePayments and SIX. For other processors, use `001` for all Visa card types. - `034`: Dankort[^1] - `036`: Cartes Bancaires[^1] - `037`: Carta Si[^1] - `039`: Encoded account number[^1] - `040`: UATP[^1] - `042`: Maestro (International)[^1] - `050`: Hipercard[^2,3] - `051`: Aura - `054`: Elo[^3] - `062`: China UnionPay  [^1]: For this card type, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in your request for an authorization or a stand-alone credit. [^2]: For this card type on Cielo 3.0, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. This card type is not supported on Cielo 1.5. [^3]: For this card type on Getnet and Rede, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit.  #### Used by **Authorization** Required for Carte Blanche and JCB. Optional for all other card types.  #### Card Present reply This field is included in the reply message when the client software that is installed on the POS terminal uses the token management service (TMS) to retrieve tokenized payment details. You must contact customer support to have your account enabled to receive these fields in the credit reply message.  Returned by the Credit service.  This reply field is only supported by the following processors: - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - OmniPay Direct - SIX  #### GPX This field only supports transactions from the following card types: - Visa - Mastercard - AMEX - Discover - Diners - JCB - Union Pay International 

        :param type: The type of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        :type: str
        """

        self._type = type

    @property
    def assurance_level(self):
        """
        Gets the assurance_level of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        Confidence level of the tokenization. This value is assigned by the token service provider.  **Note** This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**. 

        :return: The assurance_level of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._assurance_level

    @assurance_level.setter
    def assurance_level(self, assurance_level):
        """
        Sets the assurance_level of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        Confidence level of the tokenization. This value is assigned by the token service provider.  **Note** This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**. 

        :param assurance_level: The assurance_level of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        :type: str
        """
        if assurance_level is not None and len(assurance_level) > 2:
            raise ValueError("Invalid value for `assurance_level`, length must be less than or equal to `2`")

        self._assurance_level = assurance_level

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        One of two possible meanings: - The two-digit month in which a token expires. - The two-digit month in which a card expires. Format: `MM` Possible values: `01` through `12`  **NOTE** The meaning of this field is dependent on the payment processor that is returning the value in an authorization reply. Please see the processor-specific details below.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`01` through `12`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (`card_type=039`), if there is no expiration date on the card, use `12`.\\ **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Samsung Pay and Apple Pay Month in which the token expires. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.  For processor-specific information, see the `customer_cc_expmo` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The expiration_month of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        One of two possible meanings: - The two-digit month in which a token expires. - The two-digit month in which a card expires. Format: `MM` Possible values: `01` through `12`  **NOTE** The meaning of this field is dependent on the payment processor that is returning the value in an authorization reply. Please see the processor-specific details below.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`01` through `12`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (`card_type=039`), if there is no expiration date on the card, use `12`.\\ **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Samsung Pay and Apple Pay Month in which the token expires. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.  For processor-specific information, see the `customer_cc_expmo` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param expiration_month: The expiration_month of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        :type: str
        """
        if expiration_month is not None and len(expiration_month) > 2:
            raise ValueError("Invalid value for `expiration_month`, length must be less than or equal to `2`")

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        One of two possible meanings: - The four-digit year in which a token expires. - The four-digit year in which a card expires. Format: `YYYY` Possible values: `1900` through `3000` Data type: Non-negative integer  **NOTE** The meaning of this field is dependent on the payment processor that is returning the value in an authorization reply. Please see the processor-specific details below.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (1900 through 3000) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (`card_ type=039`), if there is no expiration date on the card, use `2021`.  #### FDC Nashville Global and FDMS South You can send in 2 digits or 4 digits. When you send in 2 digits, they must be the last 2 digits of the year.  #### Samsung Pay and Apple Pay Year in which the token expires. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  For processor-specific information, see the `customer_cc_expyr` or `token_expiration_year` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The expiration_year of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        One of two possible meanings: - The four-digit year in which a token expires. - The four-digit year in which a card expires. Format: `YYYY` Possible values: `1900` through `3000` Data type: Non-negative integer  **NOTE** The meaning of this field is dependent on the payment processor that is returning the value in an authorization reply. Please see the processor-specific details below.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (1900 through 3000) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (`card_ type=039`), if there is no expiration date on the card, use `2021`.  #### FDC Nashville Global and FDMS South You can send in 2 digits or 4 digits. When you send in 2 digits, they must be the last 2 digits of the year.  #### Samsung Pay and Apple Pay Year in which the token expires. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  For processor-specific information, see the `customer_cc_expyr` or `token_expiration_year` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param expiration_year: The expiration_year of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        :type: str
        """
        if expiration_year is not None and len(expiration_year) > 4:
            raise ValueError("Invalid value for `expiration_year`, length must be less than or equal to `4`")

        self._expiration_year = expiration_year

    @property
    def requestor_id(self):
        """
        Gets the requestor_id of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        Value that identifies your business and indicates that the cardholder’s account number is tokenized. This value is assigned by the token service provider and is unique within the token service provider’s database.  **Note** This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**. 

        :return: The requestor_id of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._requestor_id

    @requestor_id.setter
    def requestor_id(self, requestor_id):
        """
        Sets the requestor_id of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        Value that identifies your business and indicates that the cardholder’s account number is tokenized. This value is assigned by the token service provider and is unique within the token service provider’s database.  **Note** This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**. 

        :param requestor_id: The requestor_id of this PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard.
        :type: str
        """
        if requestor_id is not None and len(requestor_id) > 11:
            raise ValueError("Invalid value for `requestor_id`, length must be less than or equal to `11`")

        self._requestor_id = requestor_id

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
        if not isinstance(other, PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
