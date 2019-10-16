from django.db import models

# Create your models here.


class Person(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

    class Mate:
        db_table = 'you_app_name'  # 修改数据库表名称

    class Meta:
        verbose_name_plural = '个人'  # 修改模型类名称
