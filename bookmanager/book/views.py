from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo
from django.http import JsonResponse


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
