#!/usr/bin/env python
# coding=utf-8
import pytest
from tools.ExcelHandle import ExcelHandle
from tools.EnvConf import EnvConf

def pytest_addoption(parser) -> None:
    parser.addoption('--project_name', action="store",help="项目名称，如：scello、lena、ezw、xiaoyi")
    parser.addoption('--file_name', action="store",help="文档名 例如scello-9106")
    parser.addoption('--port_info', action="store",default = '',help="端口信息，对应的是sheet name")
    parser.addoption('--tran_data',action = "store",default='',help = "下一个测试用例需要的数据，对用global data")

#todo:共享工作薄方便持续写入保存
@pytest.fixture(scope='session')
def write_book(request):
    project_name = request.config.getoption("--project_name")
    file_name = request.config.getoption("--file_name")
    port_info = request.config.getoption("--port_info")
    sheet_name = port_info if port_info else 'Sheet1'
    write_book = ExcelHandle(project_name,file_name+'.xlsx', sheet_name)
    return write_book

@pytest.fixture(scope='session')
def env_data(request):
    project_name = request.config.getoption('--project_name')
    file_name = request.config.getoption("--file_name")
    port_info = request.config.getoption("--port_info")
    data = project_name+'-'+ port_info
    result_data = data if port_info else file_name
    env_data = EnvConf(result_data).get_value()
    return env_data

@pytest.fixture(scope='session')
def tran_data(request):
    tran_name = request.config.getoption("--tran_data")
    # result_data =
    # env_data = EnvConf(result_data).get_value()
    return tran_name

#todo：序列化数据操作
def pytest_generate_tests(metafunc) -> None:
    project_name = metafunc.config.getoption('--project_name')
    file_name = metafunc.config.getoption("--file_name")
    port_info = metafunc.config.getoption("--port_info")
    sheet_name = port_info if port_info else 'Sheet1'
    testcase = ExcelHandle(project_name,file_name + '.xlsx', sheet_name)
    # testdata = testcase.get_all_cases()
    #获取所有case
    testdata = testcase.get_all_cases_two()
    metafunc.parametrize(argnames='autotest', argvalues=testdata)