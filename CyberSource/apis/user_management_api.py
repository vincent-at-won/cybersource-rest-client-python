# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class UserManagementApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """
	
    def __init__(self, merchant_config, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client
        self.api_client.set_configuration(merchant_config) 


    def get_users(self, **kwargs):
        """
        Get User Information - Deprecated
        This endpoint is deprecated. Please use the search end point.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_users(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str organization_id: This is the orgId of the organization which the user belongs to.
        :param str user_name: User ID of the user you want to get details on.
        :param str permission_id: permission that you are trying to search user on.
        :param str role_id: role of the user you are trying to search on.
        :return: UmsV1UsersGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_users_with_http_info(**kwargs)
        else:
            (data) = self.get_users_with_http_info(**kwargs)
            return data

    def get_users_with_http_info(self, **kwargs):
        """
        Get User Information - Deprecated
        This endpoint is deprecated. Please use the search end point.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_users_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str organization_id: This is the orgId of the organization which the user belongs to.
        :param str user_name: User ID of the user you want to get details on.
        :param str permission_id: permission that you are trying to search user on.
        :param str role_id: role of the user you are trying to search on.
        :return: UmsV1UsersGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_id', 'user_name', 'permission_id', 'role_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))
        if 'user_name' in params:
            query_params.append(('userName', params['user_name']))
        if 'permission_id' in params:
            query_params.append(('permissionId', params['permission_id']))
        if 'role_id' in params:
            query_params.append(('roleId', params['role_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/ums/v1/users', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UmsV1UsersGet200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
