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
from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf .urls import url
from django.conf.urls.static import static

# path 匹配规则是ROUTEPATTEN
# RE_path 配戏规则是regexpattern
# url源码中return为re_path,后续可统一用url
urlpatterns = [
                  path(r'register', views.register),
                  # re_path('^$', views.register),
                  url(r'login=\d+$', views.login),
                  path(r'regist', views.regist),
                  path(r'change', views.change_pass),
                  path(r'dd_login', views.dd_login),
                  url(r'cd', views.caidan),
              ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
