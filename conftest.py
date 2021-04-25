# @Time : 2021/4/20 10:36 
# @Author : Smile_Mr
# @File : conftest.py 
# @Software: PyCharm
import pytest
import testinfra

@pytest.fixture(scope='session')
def host():

    host_info = testinfra.get_host("paramiko://root@10.110.152.175")
    return host_info