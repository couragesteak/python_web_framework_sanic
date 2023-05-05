# -*- coding:utf-8 -*-
"""
    @Author   ：有勇气的牛排
    @FileName : test.py
    @desc     : 描述
"""
from sanic import Blueprint, json

from couragesteak_pyweb.sanic import request_post_arg

m_index = Blueprint("my_index")

# http://127.0.0.1:8089
@m_index.route("/", methods=['GET', 'POST'])
async def index(request):
    name = await request_post_arg(request, "name")
    print("====== 您访问了首页 ======")
    print(name)
    return json({"code": 1, "msg": "Hello CourageSteak!!!"})