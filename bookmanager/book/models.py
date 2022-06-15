from django.db import models


# Create your models here.
class BookInfo(models.Model):
    """书籍模型[id,name]"""
    # id 系统自动创建为主键
    # 书名
    name = models.CharField(max_length=10)


class PeopleInfo(models.Model):
    """人物模型[id,name,gender,book]"""
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
