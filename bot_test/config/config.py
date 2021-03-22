# 配置文件
# Excel 读取规则配置
import os


class ExcelConfData:
    caseid = '0'
    casename = '1'
    caselevel = '2'  #优先级
    automated = '4'  # Yes 是自动运行， No 是非自动运行
    header = '6'
    method = '7' #请求方法
    authtype = '8'  # 0:admin, 1:common user, 2:not login
    data = '9' #请求内容 Payload
    url = '10' #请求地址
    expect = '12' #验证内容
    output = '14' #output
    # preconditions = '3'
    # testcontent = '4'
    # casecategory = '6'
    caseuniqueid = '0'  # 8
    # statuscode = '13'
    # checkpoints = '14'
    validate = '11'
    # parameterize = '16'
    # result = '17'


class UserInfo:
    admininfo = ''
    commoninfo = ''



# class EnvConf:
#     host = 'localhost'
#     port = '9097'
#     # name = 'lena_de'

class Header:
    headers = ''

# PROJECT_PATH=r"D:/pycharm/BotTest/BotTest"
PROJECT_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 存储路径
# Filename = "sample_data.xlsx"
# 决定读取 excel 中的sheet
# Sheet_id = 0