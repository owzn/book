from django.urls import path
from book.views import create_book, goods, register, json

urlpatterns = [
    path('create/', create_book),
    path('<cat_id>/<goods_id>', goods),
    path('register/', register),
    path('json/', json)
]
