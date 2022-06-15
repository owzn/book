from django.db import models


# Create your models here.
class BookInfo(models.Model):
    """书籍模型[id,name]"""
    # id 系统自动创建为主键
    # 书名
    name = models.CharField(max_length=10)

    # 重写str方法，让admin后台显示书籍名
    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    """人物模型[id,name,gender,book]"""
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    # 重写str方法，显示字段名
    def __str__(self):
        return f"{self.name, self.gender, self.book}"
