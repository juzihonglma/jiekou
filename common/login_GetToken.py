# -*- coding=utf-8 -*-
import allure
import requests
from selenium import webdriver
from Businesses.test_API import TestApi
from data.Get_data import getdata


class Login_GetToken:
    def __init__(self):
        self.test_Api = TestApi()
        self.get_data = getdata()

    @allure.step("系统登入")
    def login_token(self):
        #获取行数
        driver = webdriver.Chrome(executable_path='')
        driver.get('http://192.168.40.41/C5/#/user/login')
        username = driver.find_element_by_id('username').send_keys('A666')
        password = driver.find_element_by_id('password').send_keys('123456')
        dengru = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/form/button').click()


        rows_count = self.get_data.get_case_lines()
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


if __name__ == '__main__':
    Login_GetToken().login_token()