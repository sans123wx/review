from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=50 , verbose_name='名称')
    content = MDTextField()
    create_date = models.DateField(auto_now_add=True , verbose_name='创建日期')
    review_date = models.DateField(verbose_name='复习日期')
    days_between = models.IntegerField(verbose_name='时间间隔')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '笔记'
