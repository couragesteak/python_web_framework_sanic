# -*- coding:utf-8 -*-
"""
    @Author   ：有勇气的牛排
    @FileName : http_request.py
    @desc     : 描述
"""
# -*- coding:utf-8 -*-
"""
    @Author   ：有勇气的牛排
    @FileName : test.py
    @desc     : 描述
"""
from sanic import Blueprint
from sanic.response import text
from sanic.response import json
from sanic.response import html
from sanic.response import file
from sanic.response import file_stream
from sanic.response import raw
from sanic.response import redirect
from sanic.response import empty

m_response = Blueprint("my_response")


# http://127.0.0.1:8088/return_text
@m_response.get("/return_text")
async def return_text(request):
    return text("Hi 有勇气的牛排 😎")


# http://127.0.0.1:8088/return_json
@m_response.get("/return_json")
async def return_json(request):
    return json({"code": 1, "msg": "Hello CourageSteak!!!"})


# http://127.0.0.1:8088/return_html
@m_response.get("/return_html")
async def return_html(request):
    return html('<!DOCTYPE html><html lang="en"><meta charset="UTF-8"><div>Hi 有勇气的牛排😎</div>')


# http://127.0.0.1:8088/return_file
@m_response.get("/return_file")
async def return_file(request):
    import os
    filename = os.getcwd() + os.sep + "resource" + os.sep + "pub.jpg"
    print(filename)
    return await file(filename)


# http://127.0.0.1:8088/return_bigfile
@m_response.get("/return_bigfile")
async def return_bigfile(request):
    import os
    filename = os.getcwd() + os.sep + "resource" + os.sep + "2.mp4"
    print(filename)
    # return await file(filename)
    return await file_stream(filename)


# http://127.0.0.1:8088/return_raw
@m_response.get("/return_raw")
async def return_raw(request):
    return raw(b"raw bytes")

# http://127.0.0.1:8088/return_redirect
@m_response.get("/return_redirect")
async def return_redirect(request):
    return redirect("/login")

# http://127.0.0.1:8088/return_empty
@m_response.get("/return_empty")
async def return_empty(request):
    return empty()




