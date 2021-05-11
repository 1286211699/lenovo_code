# @Time : 2021/3/22 11:17 
# @Author : Smile_Mr
# @File : unit_test.py 
# @Software: PyCharm

# import configparser
# parser = configparser.ConfigParser()
# from tqdm import tqdm
# import time
#
# for i in tqdm([1,2,3]):
#     time.sleep(1)
import time
from threading import Thread
'''
多线程-多并发-单个cpu多道技术
并发：主要是在一段时间内，交替执行实现多任务，避免资源浪费
并行：在一段时间内，多个任务同时执行
异步/同步：强调的是状态，比如排队买东西，然后我拿个号码继续逛街之后等到我时候再回去
阻塞/非阻塞
'''

# def test_a(n):
#     time.sleep(1)
#     print(n)
#
# thread_list = []
#
# for i in range(5):
#     t = Thread(target= test_a,args=(i,))
#     thread_list.append(t)
#
# for x in thread_list:
#     x.start()
#
# for j in thread_list:
#     j.join()
# num1 = '123'
# num2 = '2131'
# #
# # result = eval(num1 + '*' + num2)
# # print(result)
# # print(123*2131)

'''
pytest 的hook文件 
argsparse 模块
sys.argv 
'''
print(*(1,2))