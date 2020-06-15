import logging
import os

# 项目路径
prj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据目录
data_path=os.path.join(prj_path,'data')

# 日志目录
log_path=os.path.join(prj_path,'log','log.txt')

# html报告目录
report_path=os.path.join(prj_path,'report','jfjg_report.html')

# 用例目录
test_path=os.path.join(prj_path,'test')


# 日志配置
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s', # log格式
    datefmt='%Y-%m-%d %H:%M:%S', # 日期格式
    filename=log_path, # 日志输出文件
    filemode='a'
) # 追加模式


# 数据库配置
db_host='172.16.170.49'
db_port=3306
db_user='exp'
db_passwd='xdkj@2020'
db='expenditure_supervise'

# 邮件配置
smtp_server='smtp.exmail.qq.com'
smtp_port=465
smtp_user='chaizhenzhen@ebigdata.org'
smtp_password='Czz@123456'

sender=smtp_user  #发件人
receiver='1170162859@qq.com'  #收件人
receiver_two='1057835410@qq.com'
subject='接口测试报告'   #邮件主题


# 获取登录session的相关文件配置
request_headers= {
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
url_login='http://172.16.170.49/cms/api/user/login'
requests_string_login={
            "sn": "test",
            "password": "D5BCF1D75F6C61A276B0701AC2933765"
        }