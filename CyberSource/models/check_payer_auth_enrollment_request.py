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


class CheckPayerAuthEnrollmentRequest(object):
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
        'client_reference_information': 'Riskv1authenticationsClientReferenceInformation',
        'order_information': 'Riskv1authenticationsOrderInformation',
        'payment_information': 'Riskv1authenticationsPaymentInformation',
        'processing_information': 'Riskv1authenticationsProcessingInformation',
        'buyer_information': 'Riskv1authenticationsBuyerInformation',
        'device_information': 'Riskv1authenticationsDeviceInformation',
        'merchant_information': 'Riskv1decisionsMerchantInformation',
        'acquirer_information': 'Ptsv2paymentsAcquirerInformation',
        'recurring_payment_information': 'Ptsv2paymentsRecurringPaymentInformation',
        'consumer_authentication_information': 'Riskv1decisionsConsumerAuthenticationInformation',
        'risk_information': 'Riskv1authenticationsRiskInformation',
        'travel_information': 'Riskv1authenticationsTravelInformation',
        'merchant_defined_information': 'list[Riskv1decisionsMerchantDefinedInformation]'
    }

    attribute_map = {
        'client_reference_information': 'clientReferenceInformation',
        'order_information': 'orderInformation',
        'payment_information': 'paymentInformation',
        'processing_information': 'processingInformation',
        'buyer_information': 'buyerInformation',
        'device_information': 'deviceInformation',
        'merchant_information': 'merchantInformation',
        'acquirer_information': 'acquirerInformation',
        'recurring_payment_information': 'recurringPaymentInformation',
        'consumer_authentication_information': 'consumerAuthenticationInformation',
        'risk_information': 'riskInformation',
        'travel_information': 'travelInformation',
        'merchant_defined_information': 'merchantDefinedInformation'
    }

    def __init__(self, client_reference_information=None, order_information=None, payment_information=None, processing_information=None, buyer_information=None, device_information=None, merchant_information=None, acquirer_information=None, recurring_payment_information=None, consumer_authentication_information=None, risk_information=None, travel_information=None, merchant_defined_information=None):
        """
        CheckPayerAuthEnrollmentRequest - a model defined in Swagger
        """

        self._client_reference_information = None
        self._order_information = None
        self._payment_information = None
        self._processing_information = None
        self._buyer_information = None
        self._device_information = None
        self._merchant_information = None
        self._acquirer_information = None
        self._recurring_payment_information = None
        self._consumer_authentication_information = None
        self._risk_information = None
        self._travel_information = None
        self._merchant_defined_information = None

        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if order_information is not None:
          self.order_information = order_information
        if payment_information is not None:
          self.payment_information = payment_information
        if processing_information is not None:
          self.processing_information = processing_information
        if buyer_information is not None:
          self.buyer_information = buyer_information
        if device_information is not None:
          self.device_information = device_information
        if merchant_information is not None:
          self.merchant_information = merchant_information
        if acquirer_information is not None:
          self.acquirer_information = acquirer_information
        if recurring_payment_information is not None:
          self.recurring_payment_information = recurring_payment_information
        if consumer_authentication_information is not None:
          self.consumer_authentication_information = consumer_authentication_information
        if risk_information is not None:
          self.risk_information = risk_information
        if travel_information is not None:
          self.travel_information = travel_information
        if merchant_defined_information is not None:
          self.merchant_defined_information = merchant_defined_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this CheckPayerAuthEnrollmentRequest.

        :return: The client_reference_information of this CheckPayerAuthEnrollmentRequest.
        :rtype: Riskv1authenticationsClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this CheckPayerAuthEnrollmentRequest.

        :param client_reference_information: The client_reference_information of this CheckPayerAuthEnrollmentRequest.
        :type: Riskv1authenticationsClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def order_information(self):
        """
        Gets the order_information of this CheckPayerAuthEnrollmentRequest.

        :return: The order_information of this CheckPayerAuthEnrollmentRequest.
        :rtype: Riskv1authenticationsOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this CheckPayerAuthEnrollmentRequest.

        :param order_information: The order_information of this CheckPayerAuthEnrollmentRequest.
        :type: Riskv1authenticationsOrderInformation
        """

        self._order_information = order_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this CheckPayerAuthEnrollmentRequest.

        :return: The payment_information of this CheckPayerAuthEnrollmentRequest.
        :rtype: Riskv1authenticationsPaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this CheckPayerAuthEnrollmentRequest.

        :param payment_information: The payment_information of this CheckPayerAuthEnrollmentRequest.
        :type: Riskv1authenticationsPaymentInformation
        """

        self._payment_information = payment_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this CheckPayerAuthEnrollmentRequest.

        :return: The processing_information of this CheckPayerAuthEnrollmentRequest.
        :rtype: Riskv1authenticationsProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this CheckPayerAuthEnrollmentRequest.

        :param processing_information: The processing_information of this CheckPayerAuthEnrollmentRequest.
        :type: Riskv1authenticationsProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this CheckPayerAuthEnrollmentRequest.

        :return: The buyer_information of this CheckPayerAuthEnrollmentRequest.
        :rtype: Riskv1authenticationsBuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this CheckPayerAuthEnrollmentRequest.

        :param buyer_information: The buyer_information of this CheckPayerAuthEnrollmentRequest.
        :type: Riskv1authenticationsBuyerInformation
        """

        self._buyer_information = buyer_information

    @property
    def device_information(self):
        """
        Gets the device_information of this CheckPayerAuthEnrollmentRequest.

        :return: The device_information of this CheckPayerAuthEnrollmentRequest.
        :rtype: Riskv1authenticationsDeviceInformation
        """
        return self._device_information

    @device_information.setter
    def device_information(self, device_information):
        """
        Sets the device_information of this CheckPayerAuthEnrollmentRequest.

        :param device_information: The device_information of this CheckPayerAuthEnrollmentRequest.
        :type: Riskv1authenticationsDeviceInformation
        """

        self._device_information = device_information

    @property
    def merchant_information(self):
        """
        Gets the merchant_information of this CheckPayerAuthEnrollmentRequest.

        :return: The merchant_information of this CheckPayerAuthEnrollmentRequest.
        :rtype: Riskv1decisionsMerchantInformation
        """
        return self._merchant_information

    @merchant_information.setter
    def merchant_information(self, merchant_information):
        """
        Sets the merchant_information of this CheckPayerAuthEnrollmentRequest.

        :param merchant_information: The merchant_information of this CheckPayerAuthEnrollmentRequest.
        :type: Riskv1decisionsMerchantInformation
        """

        self._merchant_information = merchant_information

    @property
    def acquirer_information(self):
        """
        Gets the acquirer_information of this CheckPayerAuthEnrollmentRequest.

        :return: The acquirer_information of this CheckPayerAuthEnrollmentRequest.
        :rtype: Ptsv2paymentsAcquirerInformation
        """
        return self._acquirer_information

    @acquirer_information.setter
    def acquirer_information(self, acquirer_information):
        """
        Sets the acquirer_information of this CheckPayerAuthEnrollmentRequest.

        :param acquirer_information: The acquirer_information of this CheckPayerAuthEnrollmentRequest.
        :type: Ptsv2paymentsAcquirerInformation
        """

        self._acquirer_information = acquirer_information

    @property
    def recurring_payment_information(self):
        """
        Gets the recurring_payment_information of this CheckPayerAuthEnrollmentRequest.

        :return: The recurring_payment_information of this CheckPayerAuthEnrollmentRequest.
        :rtype: Ptsv2paymentsRecurringPaymentInformation
        """
        return self._recurring_payment_information

    @recurring_payment_information.setter
    def recurring_payment_information(self, recurring_payment_information):
        """
        Sets the recurring_payment_information of this CheckPayerAuthEnrollmentRequest.

        :param recurring_payment_information: The recurring_payment_information of this CheckPayerAuthEnrollmentRequest.
        :type: Ptsv2paymentsRecurringPaymentInformation
        """

        self._recurring_payment_information = recurring_payment_information

    @property
    def consumer_authentication_information(self):
        """
        Gets the consumer_authentication_information of this CheckPayerAuthEnrollmentRequest.

        :return: The consumer_authentication_information of this CheckPayerAuthEnrollmentRequest.
        :rtype: Riskv1decisionsConsumerAuthenticationInformation
        """
        return self._consumer_authentication_information

    @consumer_authentication_information.setter
    def consumer_authentication_information(self, consumer_authentication_information):
        """
        Sets the consumer_authentication_information of this CheckPayerAuthEnrollmentRequest.

        :param consumer_authentication_information: The consumer_authentication_information of this CheckPayerAuthEnrollmentRequest.
        :type: Riskv1decisionsConsumerAuthenticationInformation
        """

        self._consumer_authentication_information = consumer_authentication_information

    @property
    def risk_information(self):
        """
        Gets the risk_information of this CheckPayerAuthEnrollmentRequest.

        :return: The risk_information of this CheckPayerAuthEnrollmentRequest.
        :rtype: Riskv1authenticationsRiskInformation
        """
        return self._risk_information

    @risk_information.setter
    def risk_information(self, risk_information):
        """
        Sets the risk_information of this CheckPayerAuthEnrollmentRequest.

        :param risk_information: The risk_information of this CheckPayerAuthEnrollmentRequest.
        :type: Riskv1authenticationsRiskInformation
        """

        self._risk_information = risk_information

    @property
    def travel_information(self):
        """
        Gets the travel_information of this CheckPayerAuthEnrollmentRequest.

        :return: The travel_information of this CheckPayerAuthEnrollmentRequest.
        :rtype: Riskv1authenticationsTravelInformation
        """
        return self._travel_information

    @travel_information.setter
    def travel_information(self, travel_information):
        """
        Sets the travel_information of this CheckPayerAuthEnrollmentRequest.

        :param travel_information: The travel_information of this CheckPayerAuthEnrollmentRequest.
        :type: Riskv1authenticationsTravelInformation
        """

        self._travel_information = travel_information

    @property
    def merchant_defined_information(self):
        """
        Gets the merchant_defined_information of this CheckPayerAuthEnrollmentRequest.

        :return: The merchant_defined_information of this CheckPayerAuthEnrollmentRequest.
        :rtype: list[Riskv1decisionsMerchantDefinedInformation]
        """
        return self._merchant_defined_information

    @merchant_defined_information.setter
    def merchant_defined_information(self, merchant_defined_information):
        """
        Sets the merchant_defined_information of this CheckPayerAuthEnrollmentRequest.

        :param merchant_defined_information: The merchant_defined_information of this CheckPayerAuthEnrollmentRequest.
        :type: list[Riskv1decisionsMerchantDefinedInformation]
        """

        self._merchant_defined_information = merchant_defined_information

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
        if not isinstance(other, CheckPayerAuthEnrollmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
