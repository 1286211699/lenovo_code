import requests
from base.basetest import CaseData
from base.runmethod import RunMethod
import pytest
from tools.excel_operation import OperationExcel
from tools.operate_data import OperateExcelData
from tools.get_data import GetExcelData
from tools.common_util import CommonUtil
import json
import operator
import re
from config.config import Filename
from config.config import Sheet_id
from config.config import ExcelConfData
from xlutils import copy
import allure
import jsonpath



@allure.feature('kgservice接口功能')  # feature定义功能
class Test_KgApi(object):

    testcase = CaseData('sample_data.xlsx', 0)
    testdata, ids = testcase.get_testcase_data()

    @pytest.mark.parametrize('autotest', testdata['parameterize'])
    @allure.story('fact接口测试')  # story定义用户场景
    def test_case(self, autotest):
        try:
            response = requests.request(autotest['request-data']['method'], autotest['request-data']['url'],data=str(autotest['request-data']['data']),headers=autotest['request-data']['header'])
        except:
            response = requests.request(autotest['request-data']['method'], autotest['request-data']['url'],data=str(autotest['request-data']['data']),headers=autotest['request-data']['header'])

        outputInfo = response.json()
        checkpoint = json.loads(autotest['response-data']['expect'])

        if autotest['response-data']['validate'] == "json":
            productInfo = jsonpath.jsonpath(outputInfo, '$..productInfo')[0]
            assert productInfo == checkpoint

        elif autotest['response-data']['validate'] == "status_code":
            outputStatus = jsonpath.jsonpath(outputInfo, '$..status')[0]
            checkpointStatus = jsonpath.jsonpath(checkpoint, '$..status')[0]
            assert outputStatus == checkpointStatus

        elif autotest['response-data']['validate'] == "in":
            assert str(outputInfo) in str(checkpoint)

        elif autotest['response-data']['validate'] == "not in":
            assert not str(outputInfo) in str(checkpoint)

        elif autotest['response-data']['validate'] == "=":
            assert str(outputInfo) == str(checkpoint)

        elif autotest['response-data']['validate'] == "!=":
            assert not str(outputInfo) == str(checkpoint)



