# @Time : 2021/5/6 14:19 
# @Author : Smile_Mr
# @File : 360_image_download_test.py 
# @Software: PyCharm
import requests
from fake_useragent import UserAgent
from urllib import request
from tqdm import tqdm

class ImageDownload(object):

    def __init__(self):

        self.base_url = 'https://m.image.so.com/j?q=%E7%BE%8E%E5%A5%B3&pq=&src=zixunhome&pn=180&sn=60&kn=50&gn=0&cn=0'
        # self.num  = None
        self.headers = {
            "User-Agent":UserAgent().random
        }

    def get_response(self,method):

        result = None
        try:
            response = requests.request(method,self.base_url,headers = self.headers)
            result = response.json()
            # print(result)

        except Exception as e:
            print(e)

        return result

    def parse_response(self,json_data):

        total = json_data.get('total')
        lastindex = json_data.get('lastindex')
        list = json_data.get('list')
        image_list = []

        for i in  list:
            image_url = i.get('thumb')
            image_list.append(image_url)

        return image_list

    def down_image(self,image_list):

        for i in tqdm(image_list):

            file_name = i[-13:]
            try:
                request.urlretrieve(i,"./360_image/" + file_name)
            except Exception as e:
                pass


if __name__ == '__main__':
    a = ImageDownload()
    result = a.get_response('get')
    # print(result)
    image_list = a.parse_response(result)
    a.down_image(image_list)