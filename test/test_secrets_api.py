# coding: utf-8

"""
    NetBox API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.secrets_api import SecretsApi


class TestSecretsApi(unittest.TestCase):
    """ SecretsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.secrets_api.SecretsApi()

    def tearDown(self):
        pass

    def test_generate_rsa_key_pair_list(self):
        """
        Test case for generate_rsa_key_pair_list

        This endpoint can be used to generate a new RSA key pair. The keys are returned in PEM format.
        """
        pass

    def test_get_session_key_create(self):
        """
        Test case for get_session_key_create

        Retrieve a temporary session key to use for encrypting and decrypting secrets via the API. The user's private RSA
        """
        pass

    def test_secret_roles_create(self):
        """
        Test case for secret_roles_create

        
        """
        pass

    def test_secret_roles_delete(self):
        """
        Test case for secret_roles_delete

        
        """
        pass

    def test_secret_roles_list(self):
        """
        Test case for secret_roles_list

        
        """
        pass

    def test_secret_roles_partial_update(self):
        """
        Test case for secret_roles_partial_update

        
        """
        pass

    def test_secret_roles_read(self):
        """
        Test case for secret_roles_read

        
        """
        pass

    def test_secret_roles_update(self):
        """
        Test case for secret_roles_update

        
        """
        pass

    def test_secrets_create(self):
        """
        Test case for secrets_create

        
        """
        pass

    def test_secrets_delete(self):
        """
        Test case for secrets_delete

        
        """
        pass

    def test_secrets_list(self):
        """
        Test case for secrets_list

        
        """
        pass

    def test_secrets_partial_update(self):
        """
        Test case for secrets_partial_update

        
        """
        pass

    def test_secrets_read(self):
        """
        Test case for secrets_read

        
        """
        pass

    def test_secrets_update(self):
        """
        Test case for secrets_update

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
