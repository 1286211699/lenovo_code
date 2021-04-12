# @Time : 2021/4/8 10:29 
# @Author : Smile_Mr
# @File : test.py 
# @Software: PyCharm

import requests,os,time

'''
输出1到100之间所有的偶数

输出1到100之间所有的奇数

输出1+2+3+4+…+99+100的和
'''

# data = [i for i in range(1,100) if i % 2 == 0]
# # print(data)
# #
# # data2 = [i for i in range(1,100) if i % 2 != 0]
# # print(data2)
# #
# # data3 = sum(range(1,100))
# # print(data3)

# password = 1
#
# num = 0
# data = True
# while num <= 2:
#     user_pwd = int(input('请输入你的密码:'))
#
#     if user_pwd == password:
#         print('恭喜正确')
#         break
#     else:
#         print('输入错误')
#     num += 1
# else:
#     print('输入错误三次')
#
# import random
# rand_list = [random.randrange(1000) for i in range(10) ]
# print(rand_list)
# time.sleep()
# from openpyxl import Workbook
# from openpyxl import load_workbook

'''
斐波那契数列
1,1,2,3,5,8
'''

# def fiebo(n):
#     if n <= 2:
#         return 1
#     return fiebo(n-1) + fiebo(n-2)
#
# if __name__ == '__main__':
#     print(fiebo(6))
'''
单例模式
'''
#
# class Test(object):
#
#     first_data = True
#     _instance = None
#
#     def __init__(self,name,age):
#
#         self.name = name
#         self.age = age
#
#     def __new__(cls,name,age,*args, **kwargs):
#
#         if cls.first_data:
#
#             cls._instance =  object.__new__(cls)
#             cls.first_data = False
#
#         return cls._instance
#
# a = Test('for',18)
# b = Test('afa',19)
# print(b.name)
#
# print(id(a))
# print(id(b))

# class MoliTest(object):
#
#     def __init__(self):
#         pass
#
#     def __del__(self):
#         pass

'''
年少不知愁滋味，欲上层楼，欲上层楼，为赋新词强说愁

'''


