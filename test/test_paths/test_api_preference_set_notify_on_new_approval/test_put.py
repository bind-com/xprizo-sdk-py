# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import xprizo_sdk_py
from xprizo_sdk_py.paths.api_preference_set_notify_on_new_approval import put  # noqa: E501
from xprizo_sdk_py import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiPreferenceSetNotifyOnNewApproval(ApiTestMixin, unittest.TestCase):
    """
    ApiPreferenceSetNotifyOnNewApproval unit test stubs
        Get a notification if there is a new approval  # noqa: E501
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