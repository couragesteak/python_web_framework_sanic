# -*- coding:utf-8 -*-
"""
    @Author   ：有勇气的牛排
    @FileName : 02 Application context.py
    @desc     : 描述
"""
from sanic import Sanic
from sanic import Blueprint, json
m_app_context = Blueprint("my_app_context")


# http://127.0.0.1:8088/app_context
@m_app_context.route("/app_context", methods=['GET', 'POST'])
async def app_context(request):

    # 写入
    request.ctx.db = "cs"
    # 读取
    db = request.ctx.db
    print(db)

    return json({"code": 1, "msg": "Hello CourageSteak!", "data": ""})

