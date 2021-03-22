#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 14:42
# @Author  : Smile_Mr
# @File    : test_api.py
import pytest,json
from tools.AssertHandle import assert_handle
from tools.RquestHandle import RequestHandle
import jsonpath
from tools.LogHandle import MyLog
log = MyLog().log
global_data = None

def Data_transfer(actual_result,tran_env_data,transfer_data=None):
    global global_data
    for i in tran_env_data['url_tran_data']:
        if jsonpath.jsonpath(actual_result, '$..' + i):
            global_data = jsonpath.jsonpath(actual_result, '$..' + i)[0]
            break
    # else:
    #     global_data = None


class Testdata:

    def test_start(self,autotest,write_book,env_data,tran_data):

        act_data = autotest['steps']
        tran_env_data = write_book.get_environment()
        global global_data
        for data in act_data:
            row = data['row']
            result = 'Pass'
            actual_result = None
            try:
                response = RequestHandle(data,env_data,global_data,autotest['project_name'],tran_data,tran_env_data).get_response()
                actual_result = response.json()
                # print(response.url)
                # Data_transfer(actual_result,tran_data)
                if jsonpath.jsonpath(actual_result, '$..botId'):
                    global_data = jsonpath.jsonpath(actual_result, '$..botId')[0]
                # Data_transfer(actual_result,tran_env_data)
                if jsonpath.jsonpath(actual_result, '$..slotId'):
                    global_data = jsonpath.jsonpath(actual_result, '$..slotId')[-1]
                if jsonpath.jsonpath(actual_result, '$..id'):
                    global_data = jsonpath.jsonpath(actual_result, '$..id')[0]
                if jsonpath.jsonpath(actual_result, '$..ssfId'):
                    global_data = jsonpath.jsonpath(actual_result, '$..ssfId')[0]
                # print('api:',global_data)
                assert assert_handle(actual_result, data['Expect'], data['Validate_Type'])
            except Exception as e:
                result = 'Fail'
                raise AssertionError(e)
            finally:
                write_book.write_back_result(row, json.dumps(actual_result), result)


if __name__ == '__main__':
    # pytest.main(['-s','-q','test_api.py','--project_name','scello','--file_name','scello','--port_info','9100'])
    # pytest.main(['-s','-q','test_api.py','--project_name','pranbo','--file_name','pranbo',])
    # pytest.main(['-s','-q','test_api.py','--project_name','KG','--file_name','KG',])
    # pytest.main(['-s','-q','test_api.py','--project_name','scello','--file_name','scello','--port_info','9100'])
    # pytest.main(['-s','-q','test_api.py','--project_name','KG','--file_name','KG-8016'])
    pytest.main(['-s','-q','test_api.py','--project_name','KG','--file_name','KG-8016','--tran_data','slotId'])

