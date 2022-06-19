from django.urls import path
from book.views import create_book, goods

urlpatterns = [
    path('create/', create_book),
    path('<cat_id>/<goods_id>', goods)
]
