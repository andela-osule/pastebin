import requests

API_URL = "http://pastebin.com/api/api_post.php"


class PasteBin():
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }

    def post(self,
             api_paste_name,
             api_paste_code,
             api_expire_date="10M",
             api_paste_private="1",):
        kwargs = {
            "api_dev_key": self.api_key,
            "api_option": "paste",
            "api_paste_code": api_paste_code,
            "api_paste_name": api_paste_name,
            "api_expire_date": api_expire_date,
            "api_paste_private": api_paste_private,
        }

        response = requests.post(API_URL,
                                 data=kwargs, headers=self.headers)

        return response.content
