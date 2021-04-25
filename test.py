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
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
示例 1：
输入：nums = [10,2]
输出："210"
示例 2：

输入：nums = [3,30,34,5,9]
输出："9534330"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# num = [3,30,34,5,9]
# str_num = "".join([str(i) for i in num])
# datas = [int(j) for j in str_num]
# a = sorted(datas,reverse=True)
# result = int(''.join([str(z) for z  in a]))
# print(result)


'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
'''
# from copy import deepcopy
# ord_data = []
# data = []
# s = "babad"
# for i in s:
#     if i not in data:
#         data.append(i)
#     else:
#         c = deepcopy(data)
#         ord_data.append(c)
#         data.clear()
#         data.append(i)
# else:
#     c = deepcopy(data)
#     ord_data.append(c)
# print(ord_data)


# d = dict([('a',1)])
# print(d)
'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
'''

# nums1 = [1,2]
# nums2 = [3]
#
# nums3 = sorted(nums1+nums2)
# if len(nums3) % 2 == 0:
#     n = len(nums3) / 2
#
#     speace_data = (nums3[int(n)] + nums3[int(n-1)]) / 2
# else:
#     n = len(nums3)//2
#     speace_data = nums3[int(n)]
#
# print(speace_data)


'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

'''
# nums = [-1,0,1,2,-1,-4]
#
# for i in range(len(nums)):
#     z = nums[i]
#     data = nums[i+1:]
#     for j in range(len(data)):
#         d = data[j]
#         next_data = data[j+1:]
#         # print("next_data",next_data)
#         for x in next_data:
#             if x + d + z == 0:
#                 print(x,d,z)
#
# for i in range(len(nums)):
#     data = nums[i+1:]
#     if data:
#         for j in range(len(data)):
#             next_data = data[j+1:]
#             if next_data:
#                 for x in next_data:
#                     if nums[i] + data[j] + x == 0:
#                         print(nums[i],nums[i],x)
'''
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

'''
# s = "barfoothefoobarman"
# words = ["foo", "bar"]
# for i in words:
#     print(s.index(i))

'''
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

'''

# import re
# s = ")()()()()()()()()()()())"
# data = re.findall(r'(?:\(\))+',s)
# print(data)
'''
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。
'''

# nums = [1,2,3]
#
# def hand_num(n):
#     m = len(n)
#     if m == 0:
#         return []
#     for i in range(m):

'''
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
'''
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
'''
00,01,02,12,22,21,20,10,11
'''

# row_len = len(matrix[0])
# col_len = len(matrix)
# data = []
# for i in range(3):
#     if i == 0:
#         for j in range(3):
#             data.append(matrix[i][j])
# print(data)
# data = []
# for i in range(col_len):
#     if i == 0:
#         data.append(matrix[0])
#     if i == col_len - 1:
#         data.append(matrix[::-1])

#
# for i in range(row_len):
#     if i > 0:
#         for j in range(col_len):
#             if j > 1:
#                 print(matrix[i][j])
#             elif
#     else:
#         for j in range(col_len):
#             print(matrix[i][j])

    # if i + 1 >= row_len:



'''

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6]
'''
from copy import copy
# print(1 in range(1,2))
# intervals = [[1,3],[2,7],[7,16],[15,18]]
# nums = len(intervals)
# merged=[]
# data = intervals[0].copy()
# for i in range(1,nums):
#
#     if data[1] >= intervals[i][0]:
#         data[1]=intervals[i][1]
#     else:
#         merged.append(data)
#         data = intervals[i].copy()
# merged.append(data)
# print(merged)
'''
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
示例 1：
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
'''
# import copy
# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
#
# intervals.append(newInterval)
# a = sorted(intervals,key=lambda x:x[0])
# datas = []
# data = copy.copy(a[0])
# for i in range(1,len(a)):
#     x,y = a[i]
#     if data[1] in range(x,y+1):
#         data[1] = a[i][1]
#     else:
#         datas.append(data)
#         data = copy.copy(a[i])
# datas.append(data)
# print(datas)
'''
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 
'''

# nums = [2,7,11,15]
# target = 9
# list_data = []
# for i in range(1,9):
#     for j in range(1,9):
#         if i + j == 9:
#             list_data.append([i,j])
#
# for x,y in list_data:
#     if x in nums and y in nums:
#         print(nums.index(x),nums.index(y))

'''
示例 1：
输入：nums = [1,2,0]
输出：3
示例 2：
输入：nums = [3,4,-1,1]
输出：2
示例 3：
输入：nums = [7,8,9,11,12]
输出：1

'''

# nums = [1,2,0]
# sort_nums = sorted(nums)
# max_num = max(sort_nums)
# min_num = min(sort_nums)
# start_num =0 if min_num > 0 else min_num
# data = []
# for i in range(start_num,max_num+1):
#     if i not in nums:
#         data.append(i)
# else:
#     data.append(max_num+1)
# print(list(filter(lambda x:x>0,data))[0])

#


















