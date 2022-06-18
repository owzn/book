from django.db import models


# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = "bookinfo"  # 修改表名
        verbose_name = "书籍信息"  # admin 站点使用

    # 重写 str 方法
    def __str__(self):
        return self.name


class PepoleInfo(models.Model):
    # 有序字典
    GENDER_CHOICES = (
        (1, "male"),
        (2, "female")
    )
    name = models.CharField(max_length=20)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=1)  # 枚举字典
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)
    """
    外键 系统会自动为外键添加 _id
    外键的级联操作
    主表  和   从表
    1   对   多
    书籍  对   人物
    """
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = "peopleinfo"  # 修改表名
        verbose_name = "人物信息"  # admin 站点使用

    # 重写 str 方法
    def __str__(self):
        return self.name
