#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 15:47
# @Author  : Smile_Mr
# @File    : RquestHandle.py
import requests,json,time,demjson
# from config.config import EnvConf
from conftest import env_data
from tools.CookiesHandle import CookiesHandle

cookies = ''
def hand_url(result_url,host,port,url_tran_data,global_data):

    if url_tran_data['url_tran_data']:
        for i in url_tran_data['url_tran_data']:
            if '{'+ i +'}' in result_url:
                data = result_url.split('{'+ i +'}')
                re_datas =str(global_data).join(data)
                url = 'http://' + host + ':' + port + re_datas
                break
        else:
            url = 'http://' + host + ':' + port + result_url
        return url
    else:
        url = 'http://' + host + ':' + port + result_url
    return url

def hand_playload(playload,replace,tran_data='123'):
    result = []
    for i in playload.splitlines():
        if 'botActId' in i:
            i = i.format(botActId=replace)
        if '{version}' in i:
            i = i.format(version=replace)
        if '{botId}' in i:
            i = i.format(botId=replace)
        if '{slotId}' in i:
            i = i.format(slotId=replace)
        if '{id}' in i:
            i = i.format(id=replace)
        result.append(i)

    return '\n'.join(result)

#client-->代码已经部署了--前端展示--client端---》 快速生成bot展示工具
class RequestHandle:

    def __init__(self,autotest,env_data=None,global_data = None,project_name = None,tran_data=None,tran_env_data = None,*args,**kwargs):
        self.autotest = autotest
        self.env_data = env_data
        self.global_data = global_data
        self.project_name = project_name
        self.tran_data = tran_data
        self.tran_env_data = tran_env_data

    def get_response(self):
        method = self.autotest['Method'].upper()
        host = self.env_data[0]
        port = self.env_data[1]
        if 'botActId' in self.autotest['URL']:
            url = 'http://'+ host + ':' + port + self.autotest['URL'].format(botActId = self.autotest['botActId'])
        else:
            url = 'http://'+ host + ':' + port + self.autotest['URL']
        url = hand_url( self.autotest['URL'],host,port,self.tran_env_data,self.global_data)

        # print(url)
        # if 'slotId' in self.autotest['URL']:
        #
        #     url = 'http://'+ host + ':' + port + self.autotest['URL'].format(slotId = self.global_data)
        # else:
        #     url = 'http://'+ host + ':' + port + self.autotest['URL']
        #
        # if 'ssfId' in self.autotest['URL']:
        #
        #     url = 'http://'+ host + ':' + port + self.autotest['URL'].format(ssfId = self.global_data)
        # else:
        #     url = 'http://'+ host + ':' + port + self.autotest['URL']
        # url = hand_url(url, host, port, url_tran_data, self.global_data)
        headers = demjson.decode(self.autotest['Headers'].strip())
        #更改cookie
        if 'Cookie' in headers:
            if headers['Cookie']:
                pass
            else:
                cookies = CookiesHandle(self.project_name).get_cookies
                print(cookies)
                headers['Cookie'] = cookies
        Payload = self.autotest['Payload']

        if Payload and 'botActId' in Payload:
            Payload = hand_playload(Payload,self.autotest['botActId'])
        if Payload and "{version}" in Payload and self.global_data:
            Payload = hand_playload(Payload,self.global_data)
        if Payload and "{botId}" in Payload and self.global_data:
            Payload = hand_playload(Payload, self.global_data)
        if Payload and "{slotId}" in Payload and self.global_data:
            Payload = hand_playload(Payload, self.global_data)
        if Payload and "{id}" in Payload and self.global_data:
            Payload = hand_playload(Payload, self.global_data)
        if Payload and "{ssfId}" in Payload and self.global_data:
            Payload = hand_playload(Payload, self.global_data)
        print('基本参数',self.global_data,Payload)
        try:
            response = requests.request(method,url,headers=headers,data=Payload,cookies = None)
        except:
            response = None
        return response

if __name__ == '__main__':
    # data =  {'row': 1, 'CASE_NO_ID': 'test_fact_001', 'Description': '增加数据', 'Priority': 'P1', 'Component': 'KGMS', 'Automated': 'Yes', 'Steps': 'Step1', 'Headers': '{"Content-Type": "application/json"}', 'Method': 'POST', 'Auth': '', 'Payload': '[\n    {\n        "botActId": "{botActId}",\n        "categoryName": "Asking Information",\n        "usage": 0,\n        "scriptExample": "{\\"question\\":\\"how are you?\\",\\"answer\\":\\" I am fine\\",\\"imgUrl\\":[]}",\n        "description": "",\n        "scriptType": 1,\n        "scriptValue": "test",\n        "scriptFeature": {\n            "language": [\n                "English"\n            ]\n        }\n    }\n]', 'URL': '/editor/script/save/lena_de', 'Validate_Type': 'status_code', 'Expect': 200.0, 'Actual': ''}
    # data = {'row': 1, 'botActId': 'test289437', 'CASE_NO_ID': 'test_fact_001', 'Description': '增加数据', 'Priority': 'P1', 'Component': 'KGMS', 'Automated': 'Yes', 'Steps': 'Step1', 'Headers': '{"Content-Type": "application/json"}', 'Method': 'POST', 'Auth': '', 'Payload': '{\n    "category": "Appearance",\n    "location":"US/United States",\n    "language":"en",\n    "channel":"pc"\n}', 'URL': '/cli/detail', 'Validate_Type': 'status_code', 'Expect': 200.0, 'Actual': ''}
    # print(RequestHandle(data).get_response().json())
    data = '{"answerIdList":[{id}]}'
    print(hand_playload(data,1))
