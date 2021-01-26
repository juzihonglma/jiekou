# -*- coding=utf-8 -*-

import yaml
import os
from common.log import Log
from common import ready

class Login:
    def __init__(self,deriver):
        self.dri = ready.ready_work(deriver)
        # self.logs = Log.debug()
        self.filepath = os.path.abspath(os.path.join(os.getcwd(),'..','database','page_data.yaml'))
        self.file = open(self.filepath,'r',encoding = 'utf-8')
        self.data = yaml.full_load(self.file)
        self.file.close()
        self.new_url = self.data['login'].get('url')
        self.new_name = self.data['login'].get('name')
        self.new_password = self.data['login'].get('password')
        self.submit = self.data['login'].get('denglu_btm')
        self.dri.get(self.new_url)
    def login(self,name,password,submit):
        self.dri.find_element_by_id(self.new_name).clear()
        self.dri.find_element_by_id(self.new_name).send_keys('a0006')
        self.dri.find_element_by_id(self.new_password).clear()
        self.dri.find_element_by_id(self.new_password).send_keys('123456')
        sub = self.dri.find_element_by_xpath(submit)
        self.dri.execute_script("arguments[0].click();", sub)

if __name__ == '__main__':
    Login()













