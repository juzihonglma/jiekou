# -*- coding=utf-8 -*-

import yaml,os
from common.log import Log
from common import ready

path = os.getcwd()
class Login:
    def __init__(self,driver):
        self.dri = ready.ready_work(deriver)
        self.logs = Log.debug_message
        self.file = open(path + "\database\page_data.yaml", "r", encoding="utf-8")
        self.data = yaml.load(self.file)
        self.file.close()
        self.new_url = self.data['login'].get('url')
        self.new_name = self.data['login'].get('name')
        self.new_password = self.data['login'].get('password')
        self.submit = self.data['login'].get('denglu_btm')
        self.dri.get(self.new_url)
    def login(self,name,password,submit):
        self.dri.find_element_by_id(self.new_name).clear()
        self.dri.find_element_by_id(self.new_name).send_keys(name)
        self.dri.find_element_by_id(self.new_password).clear()
        self.dri.find_element_by_id(self.new_password).send_keys(password)
        sub = self.dri.find_element_by_xpath(submit)
        self.dri.execute_script("arguments[0].click();", sub);













