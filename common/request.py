# -*- coding: UTF-8 -*-

import requests
from urllib.error import HTTPError
from common.log import Log
import json

class TestApi:
    def test_api(self,Url,method,Request_Data,Request_Data_Type,Token):
        """自定义接口测试方法"""
        global results
        try:
            if method == 'POST' or method == 'post':
                res = requests.post(Url,data=json.dumps(Request_Data),headers=Request_Data_Type)#因为请求传送的参数是josn格式，所以要用到json.dumps()
            if method == 'GET' or method == 'get':
                res = requests.get(Url,data=json.dumps(Request_Data),headers=Request_Data_Type)
            response = results.json()
            code = response.get("code")
            return code
        except HTTPError as e:
            Log.debug('请求失败',e)

    def get_responses(self,Url,method,Request_Data,Request_Data_Type):
        try:
            res = None
            if method == 'POST' or method == 'POST':
                res = requests.post(Url,data=json.dumps(Request_Data),headers=Request_Data_Type)
            if method == 'GET' or method == 'get':
                res = requests.get(Url,data=json.dumps(Request_Data),headers=Request_Data_Type)
            response = results.json()
            message = response.get("message")
            result = response.get("result")
            content = {"message": message, "result": result}
            return content
        except HTTPError as e:
            Log.debug('响应失败',e)




if __name__ == '__main__':
    re = TestApi.test_api(Url = 'http://www.nangaoyun.com/ngy/sysAccount/login',method='POST',
                          Request_Data={"accountName":"jsng0000","password":"pQR8pjMwOsQUBPSRv8TVpg==","encryptKey":"C3B4m+iyaiE8G5RlqOrK6wBLy9pNMLThSCEBOtXUZpU="},
                          Request_Data_Type = {'Content-Type':'application/json'})
