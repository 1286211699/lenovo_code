# import re
# wiste_url = "csdnbot/detail/2020-04-20/zhangsan"
# data = re.findall(r"csdnbot/detail/(\d+\-\d+\-\d+)/(\w+)",wiste_url)
# print(data)


'''
大小写
'''
# a = {'a':1,"b":2,"c":3}
# b = sorted(a.items(),key=lambda x:x[1])
# print(b)

# c = map(lambda x,y : x + y ,[1,2,3],[4,5,6])
# print(list(c))
# a = [1,2,3]
# b = [4,5,6]

'''
redi是支持的数据类型
string，hash, list ,set ,有序set
'''

'''
数字，字典，list，集合，元组，布尔
'''
'''
99乘法表
'''
# for i in range(1,10):
#
#     for j in range(1,i+1):
#
#         print('%s x %s = %s'%(j,i,i * j),end='\t')
#
#     print()

# import os,time,configparser
# configparser.ConfigParser()

# print(os.pwd())
# print(os.getcwd())
# for root,dirs,files in os.walk(os.getcwd()):
#     for file in files:
#         print(os.path.join(root,file))
# print(os.path.abspath(os.path.basename(__file__)))
import requests,time
from urllib.request import urlretrieve
from lxml import etree
from fake_useragent import UserAgent
from tqdm import tqdm

base_url = "https://www.gushiwen.org/gushi/songci.aspx"
header = {
    'user-agent': UserAgent().random
}


# print(response)

def get_page():

    try:
        response = requests.get(base_url,headers=header)
    except:
        return None
    if response.status_code == 200:
        poom_page = response.text
    path_poom_page = etree.HTML(poom_page)
    return path_poom_page

# def get_poom(url):
#
#     try:
#         response = requests.get(url,headers = header)
#     except:
#         raise Exception('解析错误')
#     xpath_data = etree.HTML(response.text)
#
#     poom = xpath_data.xpath('//*[@class="contson"]/p[2]/text()')
#
#     if poom:
#         d = "\n".join(poom)
#     # time.sleep(1)
#     return d



def parse_data(data):

    poom_data_list = data.xpath('//*[@class="typecont"]/span')
    result = []
    if poom_data_list:
        for poom_data in tqdm(poom_data_list):
            poom_author = poom_data.xpath("./text()")[0]
            poom_link = poom_data.xpath("./a/@href")[0]
            poom_title = poom_data.xpath("./a/text()")[0]
            response = requests.get(poom_link, headers=header)
            xpath_data = etree.HTML(response.text)
            poom = xpath_data.xpath('string(//*[@class="contson"])')
            # poom = xpath_data.xpath('//*[@class="contson"]/p/text()')
            # if poom:
            #     d = "\n".join(poom)
            # time.sleep(1)
            print(poom_link,poom)
            result.append(poom_title+':'+poom_author+'\n'+poom)

    return result



def wirte_data(pooms_list):
    with open('test.txt','a',encoding='utf-8') as f:
        for i in tqdm(pooms_list):
            f.write(i)
            f.write('\n')




if __name__ == '__main__':
    da = get_page()
    res = parse_data(da)
    print('爬取完毕')
    wirte_data(res)



























