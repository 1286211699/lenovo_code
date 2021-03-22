#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 10:41
# @Author  : Smile_Mr
# @File    : EnvConf.py
from configparser import ConfigParser
import os

# pro_path = os.path.dirname(os.getcwd())
pro_path = os.path.dirname(os.path.dirname(os.path.abspath(os.path.abspath(__file__))))
# print(a,abs_path)



class EnvConf:

    def __init__(self,project_name,*args,**kwargs):
        self.target = ConfigParser()
        self.target.read(pro_path + '\config\environment.ini')
        self.project_name = project_name

    def get_value(self):
        env_host = self.target.get(self.project_name,'host')
        env_port = self.target.get(self.project_name,'port')
        return env_host,env_port

if __name__ == '__main__':
    env = EnvConf('scello-9100')
    print(env.get_value())
    #
