from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
"""
所谓的视图，其实就是python函数
有两个要求：
    1、视图函数的第一个参数，就是接收请求，这个请求就是 HttpRequest 的类对象
    2、必须返回一个响应
我们期望用户输入 http://127.0.0.1:8000/index/ 来访问视图函数
"""


def index(request):
    # render 渲染模板
    # request,template_name,context=None
    # request 请求
    # template_name 模板名字
    # context = None
    # 模拟数据查询
    context = {
        "name": "百度一下"
    }
    return render(request, "book/index.html", context=context)
