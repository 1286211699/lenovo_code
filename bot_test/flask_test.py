#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/7 9:57
# @Author  : Smile_Mr
# @File    : flask_test.py
from flask import request,jsonify
from flask import Flask
import json
app = Flask(__name__)
#请求样例
'''
{ "appId": "test_bot_13008888", "params": { "platform":"微信小程序", "shopName":"佳贝艾特微信小程序", "consultTime":1575510765000,
"eventType":"买赠", "eventGroup":"双十一", "queryType":"规则", "productBrands":["佳贝艾特","爱益森"], "productSeries":["悦白系列","悠装系
列"], "sectionNumber":["零段","一段"], "milkPowderCategory":["儿童","妈妈"], "size":["150g","400g"] }, "timestamp": 1575510765,
"requestId": "4cdbc040-657a-4847-b266-7e31d9e2c3d1", "sign": "354c191ac0786473a80d8e52d9a55e00" }
'''
# { "platform":"微信小程序", "shopName":"佳贝艾特微信小程序", "eventType":"买赠",
# "eventName":"买一赠礼品001", "eventDesc":"购买店铺内任意一罐奶粉，可任选一款礼品：不倒翁玩具/儿童画板/丘比特动物绕珠/儿童玩具车/飞机玩
# 具", "eventRule":"买赠活动无法同时参与赠品活动", "eventGroup":"双十一", "eventStartTime":1575510765000, "eventEndTime":1578510765000,
# "userGroup":"全部用户", "productsName":["澳优能立多2段400g婴儿配方奶粉","澳优能立多3段400g婴儿配方奶粉"] }


#响应样例
'''
{ "status": 200, "info":"success", "data": [ { "platform":"微信小程序", "shopName":"佳贝艾特微信小程序", "eventType":"买赠",
"eventName":"买一赠礼品001", "eventDesc":"购买店铺内任意一罐奶粉，可任选一款礼品：不倒翁玩具/儿童画板/丘比特动物绕珠/儿童玩具车/飞机玩
具", "eventRule":"买赠活动无法同时参与赠品活动", "eventGroup":"双十一", "eventStartTime":1575510765000, "eventEndTime":1578510765000,
"userGroup":"全部用户", "productsName":["澳优能立多2段400g婴儿配方奶粉","澳优能立多3段400g婴儿配方奶粉"] }], "requestId": "4cdbc040-657a-4847-b266-7e31d9e2c3d9" }
'''

@app.route("/event/list", methods=['POST'])
def event_list():
    # print(request.status)
    if request.method == "GET":
        data = request.args
    else:
        data = request.json
    params = data.get('params')
    platform = params.get('platform')
    shopName = params.get('shopName')
    ruleType = params.get('ruleType')
    eventGroup = params.get('eventGroup')

    status = "200"
    result = {}
    result['status'] = status
    result['info'] = 'success'
    result['requestId'] = '4cdbc040-657a-4847-b266-7e31d9e2c3d9'

    result['data'] = []
    result_params = {
        "platform":platform,
        "shopName":shopName,
        "ruleType":ruleType,
        "eventName":"001",
        "eventDesc":"测试的优惠活动请知悉",
        "eventRule":"",
        "eventGroup":eventGroup,
        "eventStartTime":1575510765000,
        "eventEndTime":1578510765000,
        "userGroup":"",
        "productsName":["2400g","3400g"],
        "eventImgUrl":"https://moli.lenovo.com/QAimg/fact.images/ver.Sept.2.2019/moto_z2_play.jpg",
        "eventPriority":3
        }

    result['data'].append(result_params)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)