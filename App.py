# -*- coding:utf-8 -*-
"""
    @Author   ：有勇气的牛排
    @FileName : App.py
    @desc     : 描述
"""

from sanic import Sanic

# 实例化
app = Sanic("my_sanic")

# 定义静态资源
app.static('/', 'resource')

# 注册蓝图
from couragesteak_sanic_pojo.src.base_controller.cs_application_context import m_app_context
from couragesteak_sanic_pojo.src.base_controller.cs_index import m_index
from couragesteak_sanic_pojo.src.base_controller.cs_request import m_request
from couragesteak_sanic_pojo.src.base_controller.cs_response import m_response
from couragesteak_sanic_pojo.src.base_controller.cs_route import m_route
from couragesteak_sanic_pojo.src.base_controller.cs_headers import m_headers
from couragesteak_sanic_pojo.src.base_controller.cs_cookies import m_cookies
from couragesteak_sanic_pojo.src.advanced_controller.cs_class_view import m_class_view
app.blueprint(m_app_context)
app.blueprint(m_index)
app.blueprint(m_request)
app.blueprint(m_response)
app.blueprint(m_route)
app.blueprint(m_headers)
app.blueprint(m_cookies)
app.blueprint(m_class_view)     # 类视图

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8088, debug=True)
    # app.run(host="0.0.0.0", port=80, debug=False, access_log=False)

