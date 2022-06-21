from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo
from django.http import JsonResponse
from django.views import View


# Create your views here.

def create_book(request):
    BookInfo.objects.create(
        name="Python入门",
        pub_date="2022-1-1",
        readcount=100,
        commentcount=200
    )
    return HttpResponse("create")


def goods(request, cat_id, goods_id):
    query_params = request.GET
    # 1键1值，用 get('键', 默认值)，键不存在返回默认值，无默认值返回 None
    key1 = query_params.get('key1', 'hello')
    # 1键多值，用 getlist('键', 默认值)
    key2 = query_params.getlist('key2', 'world')
    return JsonResponse({'cat_id': cat_id, 'goods_id': goods_id, 'key1': key1, 'key2': key2})


def register(request):
    data = request.POST
    return JsonResponse(data)


def json(request):
    # Json数据不能通过 request.POST 获取
    body = request.body
    # b'{\r\n "username":"ow.z",\r\n "password":123\r\n}'
    # 字节码转为字符串
    body_str = body.decode()
    # <class 'str'>
    import json
    # JSON形式的字符串 可以转为 Python的字典
    body_dict = json.loads(body_str)
    return JsonResponse(body_dict)


def phones(request, cat_id, mobile):
    return JsonResponse({'cat_id': cat_id, 'mobile': mobile})


def response(request):
    person = [
        {'name': 'ow.z', 'gender': 1},
        {'name': 'mary', 'gender': 0}
    ]
    return JsonResponse(data=person, safe=False)


def set_cookie(request):
    # 获取查询字符串
    username = request.GET.get('username')
    password = request.GET.get('password')
    # 设置cookie
    response = HttpResponse('set_cookie')
    response.set_cookie('username', username)
    response.set_cookie('password', password)
    return response


def get_cookie(request):
    # 获取cookies字典数据
    print(request.COOKIES)
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    return JsonResponse({'username': username, 'password': password})


def delete_cookie(request):
    response = HttpResponse('delete_cookie')
    # 删除浏览器保存的cookie
    response.delete_cookie("username")
    response.delete_cookie("password")
    return response


def set_session(request):
    # 获取查询字符串
    username = request.GET.get('username')
    # 获取模型数据 UserInfo.objects.filter(name__exact=username)
    user_id = 1
    # 设置session信息
    request.session['user_id'] = user_id
    request.session['username'] = username
    # 返回响应
    return HttpResponse('set_session')


def get_session(request):
    # 获取并解析浏览器携带的sessionid，cookie信息
    # 方式1，sessionid不存在时，报KeyError错误，程序崩溃
    # user_id = request.session['user_id']
    # username = request.session['username']
    # 方式2，sessionid不存时，返回 None
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    return JsonResponse({'user_id': user_id, 'username': username})


class RegisterView(View):
    """类视图，处理注册"""

    def get(self, request):
        """处理GET请求，返回注册信息"""
        return HttpResponse('get请求')

    def post(self, request):
        """处理POST请求，实现注册逻辑"""
        return HttpResponse('post请求')


"""
- 我的订单，个人中心页面，如果是登录用户，可以访问，如果是未登录用户，应跳转到登录页面
- 定义一个订单，个人中心，类视图，以登录后台站点为例，测试登录与未登录
"""
from django.contrib.auth.mixins import LoginRequiredMixin


# 多继承 LoginRequiredMixin 用来判断用户是否登录，只有登录用户才可以访问页面
class OrderView(LoginRequiredMixin, View):
    """类视图，处理订单"""

    def get(self, request):
        """处理GET请求，返回订单信息"""
        return HttpResponse("get请求订单信息")

    def post(self, request):
        """处理POST请求，返回订单逻辑"""
        return HttpResponse("post请求，订单逻辑")
