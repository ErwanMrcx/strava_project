# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.segment_efforts_api import SegmentEffortsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSegmentEffortsApi(unittest.TestCase):
    """SegmentEffortsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.segment_efforts_api.SegmentEffortsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_efforts_by_segment_id(self):
        """Test case for get_efforts_by_segment_id

        List Segment Efforts  # noqa: E501
        """
        pass

    def test_get_segment_effort_by_id(self):
        """Test case for get_segment_effort_by_id

        Get Segment Effort  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
