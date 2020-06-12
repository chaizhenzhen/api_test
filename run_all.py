from test.user.test_user_login import TestUserLogin
import unittest
import HTMLTestRunner
from lib.send_email import *
from config.config import *


logging.debug('=======================测试开始=======================')
# 添加测试集
suite=unittest.TestSuite()
suite.addTests([TestUserLogin("test_user_login_noraml"),TestUserLogin("test_user_login_wrong")])
# suite=unittest.defaultTestLoader.discover("./")
# unittest.TextTestRunner(suite)

# 发送html测试报告
fp=open(report_path,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='经费监管测试报告',description='测试用例情况：')
# 执行测试用例
runner.run(suite)
fp.close()
# 发送邮件
send_email(report_path)
logging.debug('=======================测试结束=======================')





