# @Time : 2021/4/19 13:41 
# @Author : Smile_Mr
# @File : test_host.py 
# @Software: PyCharm
import pytest


def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed
    assert nginx.version.startswith("1.16")

def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled