# -*- coding:utf-8 -*-
"""
    @Author   ：有勇气的牛排
    @FileName : test.py
    @desc     : 基于类的视图是一种实现了响应请求行为的类，该类提供了一种在
                同一路由上分隔处理不同 HTTP 请求类型的方法。
"""
from sanic import Blueprint
from sanic.response import json
from sanic.views import HTTPMethodView

m_class_view = Blueprint("my_class_view")


class AdminView(HTTPMethodView):
    def get(self, request):
        return json({"code": 1, "msg": "get方法"})

    # 也可以使用异步的方式
    async def post(self, request):
        return json({"code": 1, "msg": "post方法"})


m_class_view.add_route(AdminView.as_view(), "/admin")
