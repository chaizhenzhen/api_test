import unittest
import requests
import os
import sys
from lib.db import *
from lib.read_excel import *
from config.config import *
import json


# EXIST_USER='柴珍珍'

class TestUserLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.request_headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "60",
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "172.16.170.49",
            "Origin": "http://172.16.170.49",
            "Referer": "http://172.16.170.49/supervise/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
        }
        self.data_list=excel_to_list(os.path.join(data_path,'test_data.xlsx'), "TestUserLogin")

    def test_user_login_noraml(self):
        case_data=get_test_data(self.data_list,'test_user_login_normal')
        if not case_data:
            print('用例数据不存在')
        url=case_data['url']
        request_string=case_data['args']
        response_expect=case_data['expect_res']
        response_actual=requests.post(url,headers=self.request_headers,data=request_string)
        response_results=json.loads(response_actual.text)
        # 日志
        logging.info("测试用例：{}".format('test_user_login_normal'))
        logging.info("url：{}".format(url))
        logging.info("请求参数：{}".format(request_string))
        logging.info("期望结果：{}".format(response_expect))
        logging.info("实际结果：{}".format(response_results))
        # 断言
        # self.assertEqual(response_expect,response_results.get('data').get('name'))
        self.assertIn(response_expect, str(response_results))

    def test_user_login_wrong(self):
        case_data = get_test_data(self.data_list, 'test_user_login_password_wrong')
        if not case_data:
            print('用例数据不存在')
        url = case_data['url']
        request_string = case_data['args']
        response_expect = case_data['expect_res']
        response_actual = requests.post(url, headers=self.request_headers, data=request_string)
        response_results = json.loads(response_actual.text)
        # 日志
        logging.info("测试用例：{}".format('test_user_login_password_wrong'))
        logging.info("url：{}".format(url))
        logging.info("请求参数：{}".format(request_string))
        logging.info("期望结果：{}".format(response_expect))
        logging.info("实际结果：{}".format(response_results))
        # 断言
        # self.assertEqual(response_expect, response_results.get('message'))
        self.assertIn(response_expect, str(response_results))

    def tearDown(self) -> None:
        pass

