# -*- coding: UTF-8 -*-

from Businesses.test_API import TestApi
from data.Get_data import getdata
from common import HTMLTestRunner

class RunTest:
    def __init__(self):
        self.test_Api = TestApi()
        self.get_data = getdata()


    def go_run(self):
        #获取行数
        rows_count = self.get_data.get_case_lines()
        for i in range(2,rows_count+1):
            #请求参数
            url = self.get_data.get_Url(i)
            method = self.get_data.get_Method(i)
            data_type = self.get_data.get_Request_Data_Type(i)
            request_data = self.get_data.get_Request_Data(i)

            res = self.test_Api.test_api(url,method,data_type,request_data)
            rep = res.json()
            code = rep.get('code')
            print(code)
            print(rep)

if __name__ == '__main__':
    RunTest().go_run()
