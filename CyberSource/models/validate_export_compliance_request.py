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


class ValidateExportComplianceRequest(object):
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
        'client_reference_information': 'Riskv1addressverificationsClientReferenceInformation',
        'order_information': 'Riskv1exportcomplianceinquiriesOrderInformation',
        'buyer_information': 'Riskv1addressverificationsBuyerInformation',
        'device_information': 'Riskv1exportcomplianceinquiriesDeviceInformation',
        'export_compliance_information': 'Riskv1exportcomplianceinquiriesExportComplianceInformation'
    }

    attribute_map = {
        'client_reference_information': 'clientReferenceInformation',
        'order_information': 'orderInformation',
        'buyer_information': 'buyerInformation',
        'device_information': 'deviceInformation',
        'export_compliance_information': 'exportComplianceInformation'
    }

    def __init__(self, client_reference_information=None, order_information=None, buyer_information=None, device_information=None, export_compliance_information=None):
        """
        ValidateExportComplianceRequest - a model defined in Swagger
        """

        self._client_reference_information = None
        self._order_information = None
        self._buyer_information = None
        self._device_information = None
        self._export_compliance_information = None

        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if order_information is not None:
          self.order_information = order_information
        if buyer_information is not None:
          self.buyer_information = buyer_information
        if device_information is not None:
          self.device_information = device_information
        if export_compliance_information is not None:
          self.export_compliance_information = export_compliance_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this ValidateExportComplianceRequest.

        :return: The client_reference_information of this ValidateExportComplianceRequest.
        :rtype: Riskv1addressverificationsClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this ValidateExportComplianceRequest.

        :param client_reference_information: The client_reference_information of this ValidateExportComplianceRequest.
        :type: Riskv1addressverificationsClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def order_information(self):
        """
        Gets the order_information of this ValidateExportComplianceRequest.

        :return: The order_information of this ValidateExportComplianceRequest.
        :rtype: Riskv1exportcomplianceinquiriesOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this ValidateExportComplianceRequest.

        :param order_information: The order_information of this ValidateExportComplianceRequest.
        :type: Riskv1exportcomplianceinquiriesOrderInformation
        """

        self._order_information = order_information

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this ValidateExportComplianceRequest.

        :return: The buyer_information of this ValidateExportComplianceRequest.
        :rtype: Riskv1addressverificationsBuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this ValidateExportComplianceRequest.

        :param buyer_information: The buyer_information of this ValidateExportComplianceRequest.
        :type: Riskv1addressverificationsBuyerInformation
        """

        self._buyer_information = buyer_information

    @property
    def device_information(self):
        """
        Gets the device_information of this ValidateExportComplianceRequest.

        :return: The device_information of this ValidateExportComplianceRequest.
        :rtype: Riskv1exportcomplianceinquiriesDeviceInformation
        """
        return self._device_information

    @device_information.setter
    def device_information(self, device_information):
        """
        Sets the device_information of this ValidateExportComplianceRequest.

        :param device_information: The device_information of this ValidateExportComplianceRequest.
        :type: Riskv1exportcomplianceinquiriesDeviceInformation
        """

        self._device_information = device_information

    @property
    def export_compliance_information(self):
        """
        Gets the export_compliance_information of this ValidateExportComplianceRequest.

        :return: The export_compliance_information of this ValidateExportComplianceRequest.
        :rtype: Riskv1exportcomplianceinquiriesExportComplianceInformation
        """
        return self._export_compliance_information

    @export_compliance_information.setter
    def export_compliance_information(self, export_compliance_information):
        """
        Sets the export_compliance_information of this ValidateExportComplianceRequest.

        :param export_compliance_information: The export_compliance_information of this ValidateExportComplianceRequest.
        :type: Riskv1exportcomplianceinquiriesExportComplianceInformation
        """

        self._export_compliance_information = export_compliance_information

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
        if not isinstance(other, ValidateExportComplianceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other