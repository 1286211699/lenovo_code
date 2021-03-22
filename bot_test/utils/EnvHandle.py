#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/9 17:15
# @Author  : Smile_Mr
# @File    : EnvHandle.py
import configparser,os
from config.config import PROJECT_PATH

def conf_handle(section):

    config = configparser.ConfigParser()
    conf_path = PROJECT_PATH + os.path.sep + 'config' + os.path.sep + 'test.ini'
    config.read(conf_path)
    if section in config.sections():
        # print(config.options('server1'))
        host = config.get(section,'host')
        port = config.get(section,'port')
        http = config.get(section,'http')
        return host,port,http
    else:
        host = config.get('server2','host')
        port = config.get('server2','port')
        http = config.get('server2','http')

if __name__ == '__main__':
    print(conf_handle('server1'))
