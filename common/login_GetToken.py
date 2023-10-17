# -*- coding=utf-8 -*-
import allure
import pytest
import time
import os
import openpyxl
from selenium import webdriver
from common.request import TestApi
from data.Get_data import getdata
from common import conf

import pysnooper


class Login_GetToken:
    def __init__(self):
        self.test_Api = TestApi()
        self.get_data = getdata()

    @pysnooper.snoop('file.log')
    @allure.testcase("Test Login")
    @allure.feature("UI Tests")
    @pytest.mark.usefixtures("setup")
    def login_token(self):
        chromDriverFilePath = "D:\python-UI\jiekou\deiver/chromedriver"
        driver = webdriver.Chrome(chromDriverFilePath)
        with allure.step("Open the login page"):
            driver.get('http://192.168.40.23/m/#/user/login')
        with allure.step("Enter username and password"):
            username = driver.find_element_by_id('userName').send_keys('A666')
            password = driver.find_element_by_id('password').send_keys('123456')
        with allure.step("Click the login button"):
            dengru = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/form/button').click()

        #防止过快，无法获取token
        time.sleep(3)
        #从localStorage中获取，一定要使用return，不然获取为none
        token = driver.execute_script('return localStorage.getItem("TOKEN_MES");')

        # 获取行数
        workbook = os.path.join(conf.BASE_PATH, 'data', 'test.xlsx')
        table = openpyxl.load_workbook(workbook)
        sheet = table.active
        rows_count = self.get_data.get_case_lines()
        for i in range(2,rows_count):
            if self.get_data.get_Case_id() == None:
                token_value = self.get_data.get_token(i)
            else:
                token_cell = token
                table.save(workbook)
                table.close()

            # 请求参数
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


if __name__ == '__main__':
    Login_GetToken().login_token()
    pytest.main(["-s", "-v", "--alluredir=./allure-results"])