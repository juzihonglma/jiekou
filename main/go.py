# -*- coding: UTF-8 -*-

from Businesses.test_API import TestApi
from data.Get_data import getdata
from common.Excel import ReadExcel

class RunTest:
    def __init__(self):
        self.test_Api = TestApi()
        self.get_data = getdata()
        self.read_excel = ReadExcel()


    def login_token(self):
        #获取行数
        rows_count = self.get_data.get_case_lines()
        print(rows_count)
        for i in range(2,rows_count):
            #请求参数
            url = self.get_data.get_Url(i)
            method = self.get_data.get_Method(i)
            data_type = eval(self.get_data.get_Request_Data_Type(i)) #从excel中获取数据，转换成dict
            request_data = eval(self.get_data.get_Request_Data(i))

            res = self.test_Api.test_api(url,method,request_data,data_type)
            rep = res.json()
            code = rep.get('code')
            #获取token
            token = rep.get('data').get('token')
            return token


    def run_data(self):
        rows_count = self.get_data.get_case_lines()
        for i in range(3, rows_count+1):
            # 请求参数
            url = self.get_data.get_Url(i)
            method = self.get_data.get_Method(i)
            request_data = eval(self.get_data.get_Request_Data(i))
            if self.get_data.token_col == None:
                data_type = eval(self.get_data.get_Request_Data_Type(i))  # 从excel中获取数据，转换成dict
                res = self.test_Api.test_api(url, method, request_data, data_type)
                rep = res.json()
                code = rep.get('code')
            else:
                data_type = eval(self.get_data.get_Request_Data_Type(i),self.get_data.get_token(i))
                res = self.test_Api.test_api(url, method, request_data, data_type)
                rep = res.json()
                code = rep.get('code')

if __name__ == '__main__':
    RunTest().login_token()
