# -*- coding: UTF-8 -*-

from Businesses.test_API import TestApi
from data.Get_data import getdata
from common.Excel import ReadExcel
from common import HTMLTestRunner

class RunTest:
    def __init__(self):
        self.test_Api = TestApi()
        self.get_data = getdata()
        self.read_excel = ReadExcel()


    def go_run(self):
        #获取行数
        rows_count = self.get_data.get_case_lines()
        for i in range(2,rows_count+1):
            #请求参数
            url = self.get_data.get_Url(i)
            method = self.get_data.get_Method(i)
            data_type = eval(self.get_data.get_Request_Data_Type(i)) #从excel中获取数据，转换成dict
            request_data = eval(self.get_data.get_Request_Data(i))

            res = self.test_Api.test_api(url,method,request_data,data_type)
            rep = res.json()
            code = rep.get('code')
            #获取token
            cookie = rep.get('data')
            for cookie_value in dict(cookie).values():
                #写入excel
                self.read_excel.write_excel(cookie_value)
                #判断token是否有值
                if cookie_value !=None:
                    request_data = dict(request_data,cookie_value)
                    res = self.test_Api.test_api(url, method, request_data, data_type)


if __name__ == '__main__':
    RunTest().go_run()
