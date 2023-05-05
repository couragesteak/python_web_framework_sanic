# -*- coding:utf-8 -*-
"""
    @Author   ：有勇气的牛排
    @FileName : test.py
    @desc     : 描述
"""
from sanic import Blueprint, json

from couragesteak_pyweb.sanic import request_get_header

m_headers = Blueprint("my_headers")


# 请求头headers处理
# http://127.0.0.1:8088/request_headers
@m_headers.route("/request_headers", methods=['GET', 'POST'])
async def request_headers(request):
    # 输出headers
    print(request.headers)

    # 获取headers中的参数
    token = await request_get_header(request, "token")
    print(token)

    return json({"code": 1, "msg": "Hello CourageSteak!", "data": token})


# 请求头headers处理
# http://127.0.0.1:8088/response_headers
@m_headers.route("/response_headers", methods=['GET', 'POST'])
async def response_headers(request):
    # 在响应体中加入headers，其他响应类型于此雷同
    return json(
        {"code": 1, "msg": "Hello CourageSteak!", "data": ""},
        headers={"content-language": "en-US"}
    )
