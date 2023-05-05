# -*- coding:utf-8 -*-
"""
    @Author   ：有勇气的牛排
    @FileName : test.py
    @desc     : 路由、参数
"""
from sanic import Blueprint
from sanic.response import json
from couragesteak_pyweb.sanic import request_get_arg

m_route = Blueprint("my_route")


# http://127.0.0.1:8088/get
@m_route.get("/get")
async def cs_get(request):

    # get方法 参数获取
    name = await request_get_arg(request, "name")
    print(name)

    return json({"code": 1, "msg": "get", "data": name})


# URL中的参数
# http://127.0.0.1:8088/get/cs
@m_route.get("/get/<name>")
async def cs_get1(request, name):
    print(name)
    return json({"code": 1, "msg": "get"})


# 路由参数指定类型，它将在匹配时进行强制类型转换
# http://127.0.0.1:8088/get1/1
@m_route.get("/get1/<id:int>")
async def cs_get2(request, id: int):
    print(id, type(id))
    return json({"code": 1, "msg": "get"})


# http://127.0.0.1:8088/post
@m_route.post("/post")
async def cs_post(request):
    return json({"code": 1, "msg": "post"})


# http://127.0.0.1:8088/put
@m_route.put("/put")
async def cs_put(request):
    return json({"code": 1, "msg": "put"})


# http://127.0.0.1:8088/delete
@m_route.patch("/delete")
async def cs_delete(request):
    return json({"code": 1, "msg": "delete"})


# http://127.0.0.1:8088/patch
@m_route.patch("/patch")
async def cs_patch(request):
    return json({"code": 1, "msg": "patch"})


# http://127.0.0.1:8088/head
@m_route.head("/head")
async def cs_head(request):
    return json({"code": 1, "msg": "head"})


# http://127.0.0.1:8088/options
@m_route.head("/options")
async def cs_options(request):
    return json({"code": 1, "msg": "options"})
