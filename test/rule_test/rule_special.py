import unittest
from lib.read_excel import *
import os
from config.config import *
import requests
from lib.db import *
from sql.sql import *
import json
from lib.got_session import *

class TestRuleSpecial(unittest.TestCase):

    def setUp(self) -> None:
        self.request_headers = request_headers
        self.data_list = excel_to_list(os.path.join(data_path,
                                                    'test_data.xlsx'),
                                       'TestRuleSpecial')
        sess.get_session()

    def test_rule_special_keyanshouru(self):
        case_data = get_test_data(self.data_list,
                                  'test_rule_special_keyanshouru')
        if not case_data:
            print('用例不存在')
        url = case_data.get('url')

        # 请求参数
        request_string = case_data.get('args')

        # 用sql查询结果,结果是元组
        response_sql_expect = database.query(sql_keyanshouru)
        response_sql_expect_list = []

        # 建立实际结果的响应
        response = sess.session.post(url, headers=self.request_headers,
                                     data=request_string)
        # 查询实际结果
        response_results = json.loads(response.text)

        # 日志
        logging.info("测试用例：{}".format('test_rule_special_keyanshouru'))
        logging.info("url：{}".format(url))
        logging.info("请求参数：{}".format(request_string))
        logging.info("期望结果：{}".format(response_sql_expect_list))
        logging.info("实际结果：{}".format(response_results))

        # 将元组中的凭证取出来放入列表，并和实际结果做断言
        for i in response_sql_expect:
            for voucher in i:
                response_sql_expect_list.append(voucher)
                self.assertIn(voucher, str(response_results))

    def tearDown(self) -> None:
        pass

