#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-
"""
@author: caopeng
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.

@contact: 704866169@qq.com
@Software : ubuntu PyCharm
@file: urls.py
@time: 18-10-12 下午9:29
@desc:
---------------------
包路径的定义
"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path(r'register', views.register),
                  path(r'login', views.login),
                  path(r'regist', views.regist),
                  path(r'change', views.change_pass),
                  path(r'dd_login', views.dd_login),
              ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
