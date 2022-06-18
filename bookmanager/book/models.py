from django.db import models


# Create your models here.

class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍信息'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    name = models.CharField(max_length=10)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=1)
    description = models.CharField(max_length=400, null=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name
