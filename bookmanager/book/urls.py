from django.urls import path
from book.views import create_book, goods, register, json, phones, response, set_cookie
from django.urls.converters import register_converter


# 定义转换器
class MobileConverter:
    """自定义路由转换器：匹配手机号"""
    # 匹配手机号的正则
    regex = "1[3-9]\d{9}"

    def to_python(self, value):
        # 将匹配结果传递到视图内部
        return str(value)

    def to_url(self, value):
        # 将匹配结果用于反向解析传值
        return str(value)


# 注册转换器 converter,type_name 转换器类 转换器名
register_converter(MobileConverter, 'phone')
# 调用转换器
urlpatterns = [
    path('create/', create_book),
    path('<int:cat_id>/<phone:mobile>', phones),
    path('register/', register),
    path('json/', json),
    path('response/', response),
    path('setcookie', set_cookie)
]
