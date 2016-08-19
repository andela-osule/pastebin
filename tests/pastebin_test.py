import unittest
import mock
from pastebin import PasteBin, API_URL


class PastebinTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls,):
        super(PasteBin, cls).setUpClass()
        cls.pastebin = PasteBin('secret_keys')

    @mock.patch('requests.post')
    def test_initial_configuration_works(self, mock_request_post):
        cls_bin = PastebinTest.pastebin
        cls_bin.post(
            "herego.es",
            "Here goes nothing.",
        )
        mock_request_post.called_with(
            API_URL,
            {
                "api_dev_key": self.api_key,
                "api_option": "paste",
                "api_paste_code": "Here goes nothing",
                "api_paste_name": "herego.es",
                "api_expire_date": "10M",
                "api_paste_private": "1",
            },
            headers=cls_bin.headers)
