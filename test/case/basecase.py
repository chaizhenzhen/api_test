import unittest
import sys
import os
import requests
import json
sys.path.append("../..")
from lib.read_excel import *
from config.config import *

class BaseCase(unittest.TestCase):
    def setUpClass(cls) -> None:
        if cls.__name__ != 'BaseCase':
            cls.data_list = excel_to_list(os.path.join(data_path,'test_data.xlsx'),cls.__name__)

    def get_case_data(self,case_name):
        return get_test_data(self.data_list,case_name)

    def send_request(self,case_data):
        case_name = case_data.get('case_name')
        url = case_data.get('url')
        args = case_data.get('args')
        # headers = case_data.get('headers')
        expect_res = case_data.get('expect_res')
        method = case_data.get('method')
        data_type = case_data.get('data_type')

        if method.upper() == 'GET':
            res=requests.get(url=url,headers=request_headers,params=json.loads(args))

        elif method.upper() == 'POST':
            res=requests.post(url=url,headers=request_headers,data=args)

        elif method.upper() == 'PUT':
            res=requests.put(url=url,headers=request_headers,data=args)

        elif method.upper() == 'DELETE':
            res=requests.delete(url=url,headers=request_headers,data=args)

        else:
            print(method.upper()+'该请求方式的接口未配置相关响应')

        results=json.loads(res.text)
        return results


