from django.db import models
"""
添加模型层数据类的文件
from django.db import models 所有django模型类必须继承自它.
"""
# Create your models here.
from django.db import models
from django import forms

class LoginPost(models.Model):
    title = models.TextField(max_length=150,default="用户登录")
    user_name = models.CharField(max_length=150,)
    user_pws = models.CharField(max_length=150)

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    last_login = models.DateTimeField(blank=True)

    def __unicode__(self):
        return self.username
