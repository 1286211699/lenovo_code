# @Time : 2021/4/12 16:32 
# @Author : Smile_Mr
# @File : arg_parser_test.py 
# @Software: PyCharm
import argparse

parser = argparse.ArgumentParser(description = "一个测试用例")
parser.add_argument('-p', '--pixelimage', help = 'Path to image with pixelated rectangle', default="for", required=True)
parser.add_argument('-s', '--searchimage', help = 'Path to image with patterns to search', default="test",required=True)

args = parser.parse_args()

print(args)
print(args.pixelimage)