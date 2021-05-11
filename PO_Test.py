# @Time : 2021/5/10 15:35 
# @Author : Smile_Mr
# @File : PO_Test.py 
# @Software: PyCharm
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseHandle():

    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def wait_element(self,loc):

        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(loc))
        except Exception as e:
            time.sleep(0.5)
            print(e)

    def get_element(self,loc):

        try:
            self.wait_element(loc)
            result = self.driver.find_element(*loc)
        except Exception as e:
            print(e)

        return result

    def click_element(self,loc):

        data =self.get_element(loc)
        data.click()

    def input_element(self,loc,a):

        data = self.get_element(loc)
        data.clear()
        data.send_keys(a)

    def get_element_text(self,loc):

        data = self.get_element(loc)
        return data.text

    def __del__(self):

        self.driver.close()

class ActionHandle(BaseHandle):

    def __init__(self,base_url):
        super(ActionHandle,self).__init__()
        self.driver.get(base_url)

    def find_and_click_element(self,loc):

        self.click_element(loc)

    def find_and_input_element(self,loc,data):

        self.input_element(loc,data)

    def get_page_title(self):

        return self.driver.title

if __name__ == '__main__':

    Baidu = ActionHandle('https://www.baidu.com')
    Baidu.find_and_input_element((By.ID,'kw'),'python')
    Baidu.find_and_click_element((By.ID,'su'))
    # time.sleep(10)
    print(globals()["Baidu"].get_page_title())