import unittest
from lib.read_excel import *
import os
from config.config import *
import requests
from lib.db import *
from sql.sql import *
import json

class TestRuleSpecial(unittest.TestCase):

    def setUp(self) -> None:
        self.request_headers = request_headers
        self.data_list=excel_to_list(os.path.join(data_path,'test_data.xlsx'),'TestRuleSpecial')

    def test_rule_special(self):
        case_data=get_test_data(self.data_list,'test_rule_special_keyanshouru')
        if not case_data:
            print('用例不存在')
        url=case_data.get('url')
        request_string=case_data.get('args')
        response_expect=db.query(sql_keyanshouru)
        response=requests.post(url,headers=self.request_headers,json=request_string)
        response_results=json.loads(response.text)



    def tearDown(self) -> None:
        pass

