import requests
from config.config import *
import json

def get_session():
    header_login = request_headers
    url_login = 'http://172.16.170.49/cms/api/user/login'
    requests_string_login = {
        "sn": "test",
        "password": "D5BCF1D75F6C61A276B0701AC2933765"
    }
    session = requests.Session()
    session.post(url_login, header_login, json=requests_string_login)

def close_session():
    get_session().session.close()







'''
class GetSession:
    def __init__(self):
        self.header_login=request_headers
        self.url_login='http://172.16.170.49/cms/api/user/login'
        self.requests_string_login={
            "sn": "test",
            "password": "D5BCF1D75F6C61A276B0701AC2933765"
        }
        self.session=requests.session()

    # def __del__(self):
    #     self.session.close()

    def get_session(self):
        response=self.session.post(self.url_login,self.header_login,json=self.requests_string_login)
        return response

getSession=GetSession()

'''