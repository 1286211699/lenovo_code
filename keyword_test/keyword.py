# @Time : 2021/5/11 14:32 
# @Author : Smile_Mr
# @File : keyword.py 
# @Software: PyChar
'''
什么是关键字驱动？
将驱动数据和代码区分出来，使用固定的关键字，实现一些场景设计，方便测试人员维护
例如：
以下以selenium框架举例
excel驱动数据中有对应的数据和固定关键字
1、定位数据 类型
2、定位数据 元素
3、数据执行 关键字
4、数据必要参数
设计方案：
首先对每个关键字进行封装
读取excel文件中每个实例对应的关键字，注意使用json分析场景，关键字可对应到每个场景中
使用selenium
预计关键字，openurl，inputtext
'''
import inspect,time
from selenium.webdriver.common.by import By
from selenium import webdriver

testcase = {'row':1,'keyword':['openurl','inputtext'],'kwargs':{'url':'https://www.baidu.com','element':'kw','param':'python'}}

class Base:

    def __init__(self):
        self.driver = driver

    def openurl(self,url,*args,**kwargs):
        self.driver.get(url)

    def inputtext(self,element,param,*args,**kwargs):

        self.driver.find_element(*(By.ID,element)).clear()
        self.driver.find_element(*(By.ID,element)).send_keys(param)

    def __del__(self):
        time.sleep(4)
        self.driver.close()



driver = webdriver.Chrome()

kwargs = testcase['kwargs']
Func = Base()
for i in testcase['keyword']:
    func = Func.__getattribute__(i)
    args = inspect.getfullargspec(func).args
    data = {}
    for j in args:
        data[j] = kwargs.get(j)
    data.pop('self')
    # if data['driver'] ==None:
    #     data['driver'] = driver
    func(**data)





