#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 15:47
# @Author  : Smile_Mr
# @File    : AssertHandle.py
import demjson
import jsonpath

def tran_upper(data):
    return data.upper()

#todo:对返回数据和期望数据进行比对
def assert_handle(actual_result,expect_result,Validate_Type):
    '''
    :param actual_result: 真实数据
    :param expect_result: 期望数据
    :param Validate_Type: 对比的类型
    :return: Ture or False
    '''
    if Validate_Type.lower() == 'json':
        try:
            expect_result = demjson.decode(expect_result)
        except:
            expect_result = '{'+ expect_result +'}'
            expect_result = demjson.decode(expect_result)
        result = True
        for key,value in expect_result.items():
            data = jsonpath.jsonpath(actual_result,'$..'+ key)[0]
            if data == value:
                pass
            else:
                result = False
        return  result

    elif Validate_Type.lower() == 'status_code':
        data = None
        if jsonpath.jsonpath(actual_result,'$..code'):
            data = jsonpath.jsonpath(actual_result,'$..code')[0]
        elif jsonpath.jsonpath(actual_result,'$..status code'):
            data = jsonpath.jsonpath(actual_result,'$..status code')[0]
        elif jsonpath.jsonpath(actual_result, '$..status'):
            data = jsonpath.jsonpath(actual_result, '$..status')[0]
            # data = jsonpath.jsonpath(actual_result,'$..code')[0]
        if data:
            return int(expect_result) == int(data)
        else:
            return False

    elif Validate_Type.lower() == "in":
        return str(expect_result) in str(actual_result)

    elif Validate_Type.lower() == "not in":
        return str(expect_result) not in str(actual_result)

    elif Validate_Type == '=':
        return str(expect_result).upper() == str(actual_result).upper()

    elif Validate_Type == '!=':
        return str(expect_result).upper() != str(actual_result).upper()

    else:
        return False


