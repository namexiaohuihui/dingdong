#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-
"""
@author: caopeng
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.

@contact: 704866169@qq.com
@Software : ubuntu PyCharm
@file: forms.py
@time: 18-10-12 下午9:29
@desc:
---------------------
ModelForm 所用django表单类的基类
"""

# 导入forms组件
from django.forms import widgets,ValidationError
from django.core.validators import RegexValidator

from django import forms


class LoginForm(forms.Form):
    # class Meta:
    #     model = LoginPost
    #     fields = "__all__"
    #     pass
    user_name = forms.CharField(label='用户账号')
    user_pws = forms.CharField(label='登录密码', widget=forms.PasswordInput())
    # RADIO_CHOICES = (
    #     ('none', "记录登录密码"),
    # )
    # aa1 = forms.ChoiceField(label="", widget=forms.RadioSelect, choices=RADIO_CHOICES)
    pass


##定义了UserForm表单用于注册和登录页面，ChangeForm表单用于修改密码页面
class UserForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密   码', widget=forms.PasswordInput())
    pass


class ChangeForm(forms.Form):
    username = forms.CharField(label='用户名')
    old_password = forms.CharField(label='原密码', widget=forms.PasswordInput())
    new_password = forms.CharField(label='新密码', widget=forms.PasswordInput())


class RegForms(forms.Form):
    title_top = forms.CharField(label='注册页面')
    title_op = forms.CharField(label='叮咚入口')
    name = forms.CharField(
        label="登录账号",
        max_length=16,
        # 自定义类的属性
        widget=widgets.TextInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "帐号不能为空"
        }
    )
    # 调用form组件内部方法创建一个长度不大于16且不小于8的密码文本框
    pwd = forms.CharField(
        label="输入密码",
        max_length=16,
        min_length=8,
        # 定义为密码文本,render_value设置为验证不通过时不把密码刷新掉
        widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        error_messages={
            "min_length": "密码不能少于8位数",
            "required": "密码不能为空"
        }
    )

    re_pwd = forms.CharField(
        label="确认密码",
        max_length=16,
        min_length=8,
        # 定义为密码文本,render_value设置为验证不通过时不把密码刷新掉
        widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        error_messages={
            "min_length": "密码不能少于8位数",
            "required": "密码不能为空"
        }
    )
    email = forms.EmailField(
        label="用户邮箱",
        widget=widgets.EmailInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "邮箱地址不能为空",
            # invalid 是校验格式是否正确
            "invalid": "邮箱地址格式错误",
        }
    )
    mobliphone = forms.CharField(
        label="绑定手机",
        widget=widgets.TextInput(attrs={"class": "form-control"}),
        # form 组件中用正则判断是否符合条件
        validators=[RegexValidator(r'^[0-9]+$', '请输入数字'), RegexValidator(r'^159[0-9]+$', '数字必须以159开头')],
        error_messages={
            "required": "手机号码不能为空",
        }
    )

    # # 单radio值为字符串
    # gender = forms.fields.ChoiceField(
    #     choices=((1, "男"), (2, "女"), (3, "保密")),
    #     label="性别",
    #     initial=3,
    #     widget=forms.widgets.RadioSelect()
    # )

    # 单选Select
    # hobbyc = forms.fields.ChoiceField(
    #     choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
    #     label="爱好",
    #     initial=3,
    #     widget=forms.widgets.Select()
    # )

    # 多选Select
    # hobbym = forms.fields.MultipleChoiceField(
    #     choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
    #     label="爱好",
    #     initial=[1, 3],
    #     widget=forms.widgets.SelectMultiple()
    # )

    # 单选checkbox
    keep = forms.fields.ChoiceField(
        label="同意协议",
        initial="checked",
        widget=forms.widgets.CheckboxInput(),
        error_messages={
            "keep": "一定要勾选协议",
        }
    )

    # 多选checkbox
    # hobby = forms.fields.MultipleChoiceField(
    #     choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
    #     label="爱好",
    #     initial=[1, 3],
    #     widget=forms.widgets.CheckboxSelectMultiple()
    # )

    def clean(self):
        """
        编写输入框输入的内容是否符合
        :return:
        """
        cleaned_data = super(RegForms, self).clean()
        clean_name = cleaned_data.get("name")
        print("------" + clean_name)
        from django.http import HttpResponse
        # return HttpResponse("注册成功！")
        # raise ValidationError("输入了")
        from django.shortcuts import render_to_response
        uf = ChangeForm()
        return render_to_response('change.html', {'uf': uf})