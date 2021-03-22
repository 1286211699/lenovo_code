#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 16:33
# @Author  : Smile_Mr
# @File    : CookiesHandle.py
import requests


def get_pranbo_cookies():

    res = requests.session()
    url = "http://10.110.152.175:9104/smart-sso-server/login"
    payload='backUrl=http%3A%2F%2F10.110.152.171%3A30080%2F&random=789&account=gengyl3&password=botops_123&captcha=1111'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = res.request("POST", url, headers=headers, data=payload,allow_redirects=False)
    location_data = response.headers['Location']
    param_data = location_data.split('=')[-1]
    req_url = 'http://10.110.152.171:30081/user/login?__vt_param__={}'.format(param_data)
    user_response = res.request('POST',req_url)
    cookies = user_response.headers['Set-Cookie']
    return cookies

def get_scello_cookies():
    res = requests.session()
    url = "http://10.110.152.175:9104/smart-sso-server/login"
    payload = 'backUrl=http%3A%2F%2F10.110.152.171%3A30080%2F&random=789&account=bot_admin&password=123qweQW&captcha=1111'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = res.request("POST", url, headers=headers, data=payload, allow_redirects=False)
    location_data = response.headers['Location']
    param_data = location_data.split('=')[-1]
    req_url = 'http://10.110.152.171:30081/user/login?__vt_param__={}'.format(param_data)
    user_response = res.request('POST', req_url)
    cookies = user_response.headers['Set-Cookie']
    return cookies

def get_KG_cookies():
    res = requests.session()
    url = "http://10.110.152.175:9104/smart-sso-server/login"
    payload = 'backUrl=http%3A%2F%2F10.110.152.171%3A30080%2F&random=789&account=testanswer1&password=test_123&captcha=1111'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = res.request("POST", url, headers=headers, data=payload, allow_redirects=False)
    location_data = response.headers['Location']
    param_data = location_data.split('=')[-1]
    req_url = 'http://10.110.152.171:30081/user/login?__vt_param__={}'.format(param_data)
    user_response = res.request('POST', req_url)
    cookies = user_response.headers['Set-Cookie']
    return cookies


#获取cookie，提供不同的项目cookie
class CookiesHandle():

    def __init__(self,project_name):
        self.project_name = project_name
        self.cookies = globals()['get_' + project_name + '_cookies']

    @property
    def get_cookies(self):
        cookies = self.cookies()
        return cookies

if __name__ == '__main__':

    a = CookiesHandle('pranbo')
    print(a.get_cookies)