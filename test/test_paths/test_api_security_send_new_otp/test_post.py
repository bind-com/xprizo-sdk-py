# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import xprizo_sdk_py
from xprizo_sdk_py.paths.api_security_send_new_otp import post  # noqa: E501
from xprizo_sdk_py import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiSecuritySendNewOtp(ApiTestMixin, unittest.TestCase):
    """
    ApiSecuritySendNewOtp unit test stubs
        Send one time password to user  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
