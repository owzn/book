from django.urls import path
from book.views import create_book, goods, register, json, phones, response, set_cookie, get_cookie, delete_cookie
from django.urls.converters import register_converter
from book.views import set_session, get_session
from book.views import RegisterView, OrderView


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
    path('setcookie/', set_cookie),
    path('getcookie/', get_cookie),
    path('deletecookie/', delete_cookie),
    path('setsession/', set_session),
    path('getsession/', get_session),

    # 类视图，需带括号调用 View.as_view() takes 1 positional argument but 2 were given
    path('reg/', RegisterView.as_view()),
    path('order/', OrderView.as_view())
]
