import pymysql
import os
import sys
sys.path.append("../..")
from config.config import *
# 1.建立连接

class DB:
    def __init__(self):
        self.conn=pymysql.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            passwd=db_passwd,
            db=db,
            charset='utf8'
        )
        self.cur=self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query(self,sql):
        self.cur.execute(sql)
        logging.debug(sql)
        return self.cur.fetchall()
        logging.debug(self.cur.fetchall())

    def change(self,sql):
        try:
            self.cur.execute(sql)
            logging.debug(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))
            logging.debug(str(e))

    def check_user(self,sn):
        result=self.query("select * from t_user where sn='{}'".format(sn))
        return True if result else False

    def del_user(self,sn):
        self.change("delete from t_user where sn='{}'".format(sn))

    def add_user(self,userName,email,phoneNum,sn,status):
        self.change("insert into t_user (name,email,phone_num,sn,status) values ('{}','{}','{}','{}')".format(userName,email,phoneNum,sn,status))


database=DB()
# db.check_user('test')