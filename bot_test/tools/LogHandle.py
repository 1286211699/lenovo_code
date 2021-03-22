#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 16:34
# @Author  : Smile_Mr
# @File    : LogHandle.py

import logging
import os
from config.config import PROJECT_PATH

class MyLog:

    def __init__(self,name = __name__,path = PROJECT_PATH + os.sep + 'report'+ os.sep + 'mylog.log',level = 'DEBUG'):
        self.name = name
        self.path = path
        self.level = level
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(self.level)

    def get_handler(self):
        sh = logging.StreamHandler()
        fh = logging.FileHandler(self.path,encoding='utf-8')
        return  sh,fh

    def set_handler(self,sh,fh,level = "DEBUG"):
        sh.setLevel(level)
        fh.setLevel(level)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def set_formatter(self,sh,fh):
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
                                      '-%(levelname)s-[日志信息]: %(message)s',
                                      datefmt='%a, %d %b %Y %H:%M:%S')
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

    def close_handler(self,sh,fh):
        sh.close()
        fh.close()

    @property
    def log(self):
        sh,fh = self.get_handler()
        self.set_handler(sh,fh)
        self.set_formatter(sh,fh)
        self.close_handler(sh,fh)
        return self.logger

if __name__ == '__main__':
    log = MyLog()
    logger = log.log
    logger.debug('I am a debug message')
