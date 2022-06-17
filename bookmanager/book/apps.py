from django.apps import AppConfig


class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book'
    # 后台应用，用中文显示
    verbose_name = "图书管理"
