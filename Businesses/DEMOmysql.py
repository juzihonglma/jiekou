import pymysql
import os
from configparser import ConfigParser
from common import log

class connect:
    def __init__(self,host=None,port=0,user=None,passwd=None,db=None,charset=None,max_retries_count =None,
                 conn_retries_count=None,conn_timeout=None):
        con_status = True
        #定位路径
        file = os.path.abspath(os.path.join(os.getcwd(),'..','database','config'))
        config = ConfigParser()
        config.read(file)
        host = config.get("mysql",'host')
        port = config.getint("mysql",'port')
        user = config.get("mysql",'user')
        passwd = config.get("mysql",'passwd')
        db = config.get("mysql",'db')
        charset = config.get("mysql",'charset')
        max_retries_count = config.getint("mysql",'max_retries_count')
        conn_retries_count = config.getint("mysql",'conn_retries_count')
        connect_timeout = config.getint("mysql",'connect_timeout')

        while con_status and max_retries_count > conn_retries_count:
            try:
                #建立连接
                self.conn = pymysql.Connect(host=host, port=port, user=user, passwd=passwd, db=db,charset=charset)
                log.Log
                # 创建游标
                self.cursor = self.conn.cursor()
                con_status = False
            except:
                conn_retries_count +=1
                print(conn_retries_count)
                print('连接失败')
            continue

    #关闭数据库
    def closeConn(self):
        self.cursor.close()
        self.conn.close()
        print('关闭')

    def Select(self,sql):
        #执行查询sql
        self.cursor.execute(sql)
        #获取单条数据
        rows = self.cursor.fetchall()
        for data in rows:
            print(data)
        return rows


if __name__ == '__main__':
    sql = "select * from sys_user"
    r = connect().Select(sql)
    connect().closeConn()


