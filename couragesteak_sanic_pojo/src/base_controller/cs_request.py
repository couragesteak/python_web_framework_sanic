# -*- coding:utf-8 -*-
"""
    @Author   ：有勇气的牛排
    @FileName : http_request.py
    @desc     : 描述
    pip install couragesteak_pyweb
"""

from sanic import Blueprint
from sanic import json

from couragesteak_pyweb.sanic import request_post_arg

m_request = Blueprint("my_request")


# curl 127.0.0.1:8089 -d '{"name": "有勇气的牛排"}'
# http://127.0.0.1:8089/request_json
@m_request.get("/request_json")
async def index(request):
    name = await request_post_arg(request, "name")
    print("====== json数据 ======")
    print(name)
    return json({"code": 1, "msg": "Hello CourageSteak!!!"})
