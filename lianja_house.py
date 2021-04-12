# @Time : 2021/4/8 16:54 
# @Author : Smile_Mr
# @File : lianja_house.py 
# @Software: PyCharm

'''
链家二手房代码测试
'''

import requests,time
from urllib.request import urlretrieve
from fake_useragent import UserAgent
from lxml import etree
from tqdm import tqdm

headers = {
    'user-agent':UserAgent().random
}

def get_page(url):

    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response
    except:
        return None

def parse_page(response):

    xpath_page = etree.HTML(response.text)
    datas_list = xpath_page.xpath('//*[@class="sellListContent"]/li')
    for data in tqdm(datas_list):
        try:
            house_img_link = data.xpath('.//*[@class="lj-lazy"]/@data-original')[0]
            house_title = data.xpath('.//*[@class="title"]/a/text()')[0]
        except:
            pass
        if house_img_link:
            down_data(house_img_link)

def down_data(url):

    file_name = url[-30:]
    try:
        urlretrieve(url,"./image/"+ file_name)
    except:
        print("下载出错")



if __name__ == '__main__':
    response1 = get_page('https://cd.lianjia.com/ershoufang/pg/')
    # print(response1.text)
    parse_page(response1)
