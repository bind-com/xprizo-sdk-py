# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import xprizo_sdk_py
from xprizo_sdk_py.paths.api_preference_set_request_payment_webhook import put  # noqa: E501
from xprizo_sdk_py import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiPreferenceSetRequestPaymentWebhook(ApiTestMixin, unittest.TestCase):
    """
    ApiPreferenceSetRequestPaymentWebhook unit test stubs
        Set a url that that can be used to receive callbacks when request payment is made  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
