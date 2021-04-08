# @Time : 2021/3/15 16:36 
# @Author : Smile_Mr
# @File : main.py 
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time,sys

def handle_option():
    chrome_options = Options()
    chrome_options.headless = False
    return chrome_options

class PageObjec():

    data = (By.CLASS_NAME, "s_newBtn")
    def __init__(self,url,keyword):
        self.browser = webdriver.Chrome(options = handle_option())
        self.keyword = keyword
    def get_and_clink(self,data):
        # print(data)
        # print(*PageObjec.data)
        self.browser.find_element(*data).click()
    def clear_and_send_keys(self,data,key_data):
        element = self.browser.find_element(*data)
        element.clear()
        element.send_keys(key_data)



class BaiduSpider(PageObjec):

    def __init__(self,url,keyword,other,*args,**kwargs):
        super().__init__(url,keyword)
        self.init_url = "https://image.baidu.com"
        self.browser.implicitly_wait(10)

    def open_web(self):

        self.browser.get(self.init_url)
        WebDriverWait(self.browser,5).until(EC.presence_of_element_located((By.CLASS_NAME,"s_btn_wr")))
        print(self.browser.title)
        self.search_web()

    def search_web(self):

        search_input = self.browser.find_element_by_id('kw')
        search_input.clear()
        search_input.send_keys(self.keyword)
        # self.browser.find_element_by_class_name('s_newBtn').click()
        try:
            self.get_and_clink((By.CLASS_NAME,"s_newBtn"))
        except Exception as e:
            raise e
        time.sleep(1)


    def push_web(self):

        for i in range(3):  # 测试三次下拉
            self.browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
            time.sleep(3)
        self.get_data()
    def get_data(self):
        elemetment_datas = self.browser.find_elements_by_xpath('//*[@id="imgid"]//li/div/a/img')
        for element in elemetment_datas:
            url = element.get_attribute('src')
            print(url)


    def __del__(self):
        self.browser.close()

if __name__ == '__main__':
    BaiduSpider('sfaf','唯美','1').open_web()