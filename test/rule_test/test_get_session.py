# import requests
# import json

# from config.config import *
from lib.got_session import *

# 本文件测试session是否可以正常获取

url='http://172.16.170.49/supervise/api/audit/probable/list'
requests_string={
"businessEndDate": "",
"businessStartDate": "",
"issue": "",
"keyword": "",
"maxCreditMoney": "",
"maxDebitMoney": "",
"minCreditMoney": "",
"minDebitMoney": "",
"onlyNational": "0",
"pgCt": "1",
"pgSz": "10",
"ruleCode": "bdce8b92-9b42-11ea-a16a-005056b6438b",
"sortField": "",
"sortType": "",
"warnEndDate": "",
"warnLevelId": "",
"warnStartDate": "",
"warnStatus": "",
"warnTarget": "VOUCHER"
}

sess.get_session()
response02 = sess.session.post(url, headers=request_headers, json=requests_string)

print(json.loads(response02.text))




