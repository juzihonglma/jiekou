# -*- coding: UTF-8 -*-

import requests
from urllib.error import HTTPError
from common.log import Log
import json

class TestApi:
    def test_api(self,Url,method,Request_Data,Request_Data_Type):
        try:
            res =None
            if method == 'POST' or method == 'post':
                res = requests.post(Url,Request_Data_Type,json.dumps(Request_Data))#因为请求传送的参数是josn格式，所以要用到json.dumps()
            if method == 'GET' or method == 'get':
                res = requests.get(Url,Request_Data_Type,json.dumps(Request_Data))
            # rep = res.json()
            # print(rep)
            return res
        except HTTPError as e:
            Log.debug('请求失败',e)

    def get_responses(self,Url,method,Request_Data,Request_Data_Type):
        try:
            res = None
            if method == 'POST' or method == 'POST':
                res = requests.post(Url,Request_Data,Request_Data_Type)
            if method == 'GET' or method == 'get':
                res = requests.get(Url,Request_Data,Request_Data_Type)
            responese = res.json()
            return responese
            # code = responese.get("code")
            # msg = responese.get("msg")
            # content = {"code":code,"msg":msg}
            # return content
        except HTTPError as e:
            Log.debug('响应失败',e)



#
# if __name__ == '__main__':
#     re = TestApi.test_api(Url = 'http://172.21.3.4/ngy/sysAccount/login',method='POST',
#                           Request_Data={"accountName":"a0006","password":"JezHmIz7K2/kMGOv3geBdg==","encryptKey":"SJRmX5VQrcN+0oFB3ZcoIwBLy9pNMLThSCEBOtXUZpU="},
#                           Request_Data_Type = {"Content-Type":"application/json,charset=utf-8"})
