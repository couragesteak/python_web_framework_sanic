# -*- coding:utf-8 -*-
"""
    @Author   ：有勇气的牛排
    @FileName : test.py
    @desc     : 描述
"""
from sanic import Blueprint, json
from sanic.response import text

from couragesteak_pyweb.sanic import request_get_cookie

m_cookies = Blueprint("my_cookies")


# 写cookie
# http://127.0.0.1:8088/write_cookie
@m_cookies.route("/write_cookie", methods=['GET', 'POST'])
async def write_cookie(request):
    response = text("There's a cookie up in this response")
    response.cookies["cs"] = "It worked!"
    # 指定 Cookie 的有效域。显式指定的域必须始终以点开始
    response.cookies["cs"]["domain"] = "www.couragesteak.com"
    # 指定 Javascript 是否无法读取 Cookie。
    response.cookies["cs"]["httponly"] = True
    # Cookie 在客户端浏览器上失效的时间。
    # response.cookies["cs"]["expires"] =
    # Cookie 应生存的秒数。
    # response.cookies["cs"]["max-age"] =

    response.cookies["name"] = "couragesteak"
    response.cookies["sex"] = "1"

    return response


# 读cookie
# http://127.0.0.1:8088/read_cookie
@m_cookies.route("/read_cookie", methods=['GET', 'POST'])
async def read_cookie(request):
    # 输出所有cookie信息
    print(request.cookies)

    # 获取指定cookie
    name = request_get_cookie(request, "name")
    sex = request_get_cookie(request, "sex")
    print(name, sex)

    return json({"code": 1, "msg": "Hello CourageSteak!", "data": ""})
