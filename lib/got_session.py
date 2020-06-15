from config.config import *
import requests
import json

class GetSession:
    def __init__(self):
        self.header_login=request_headers
        self.url_login='http://172.16.170.49/cms/api/user/login'
        self.requests_string_login={
            "sn": "test",
            "password": "D5BCF1D75F6C61A276B0701AC2933765"
        }
        self.session=requests.Session()

    def __del__(self):
        self.session.close()

    def get_session(self):
        self.session.post(self.url_login,headers=self.header_login,json=self.requests_string_login)
        # print(json.loads(response_login.text))

sess=GetSession()
# sess.get_session()

