# -*- coding: UTF-8 -*-

from common.request import TestApi
from data.Get_data import getdata
from common.Excel import ReadExcel


class APITest:
    def __init__(self):
        self.test_Api = TestApi()
        self.get_data = getdata()
        self.read_excel = ReadExcel()

    def run_data(self,sheet):
        rows_count = self.get_data.get_case_lines()
        for i in range(2, rows_count+1):
            Case_id = getdata.get_Case_id(sheet,i)
            Api_name = getdata.get_API_name(sheet,i)
            Url = getdata.get_Url(sheet,i)
            Method = getdata.get_Method(i)
            Request_Data_Type = getdata.get_Request_Data_Type(sheet,i)
            Token = getdata.get_token(sheet,i)
            Request_Data = getdata.get_Request_Data(sheet,i)
            code = req


if __name__ == '__main__':
    RunTest().login_token()
