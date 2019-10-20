from django.shortcuts import render

import os
from stores.forms import LoginForm, UserForm, ChangeForm, RegForms
from stores.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from stores import models
import csv


# 定义URL相应函数
# Create your views here.
def dd_login(request):
    if request.method == "POST":
        login = LoginForm(request.POST)
        if login.is_valid():
            print("点击登录了")
    else:
        login = LoginForm()
    # prodect_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # return render(request, os.path.join(prodect_root, 'stores/templates',
    #                                     "login.html"), {"form": login})
    return render(request, "login.html", {"form": login})
    pass


def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            ##判断用户原密码是否匹配
            user = User.objects.filter(username=username)
            if user:
                info = '用户名已存在!'
            elif len(user) == 0:
                info = '注册成功!'
                user = User()
                user.username = username
                user.password = password
                user.save()

            return HttpResponse(info)
    else:
        uf = UserForm()

    return render_to_response('regist.html', {'uf': uf})


def login(request):
    if request.method == 'POST':
        ##获取表单信息
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            ##判断用户密码是否匹配
            user = User.objects.filter(username=username)
            if user:
                passwd = User.objects.filter(username=username, password=password)
                if passwd:
                    info = '登录成功！'
                else:
                    info = '请检查密码是否正确!'
            elif len(user) == 0:
                info = '请检查用户名是否正确!'

            return HttpResponse(info)
    else:
        uf = UserForm()

    return render('userlogin.html', {'uf': uf})


def change_pass(request):
    if request.method == 'POST':
        uf = ChangeForm(request.POST)
        print(uf.is_valid())
        if uf.is_valid():
            username = uf.cleaned_data['username']
            old_password = uf.cleaned_data['old_password']
            new_password = uf.cleaned_data['new_password']

            ##判断用户原密码是否匹配
            user = User.objects.filter(username=username)
            if user:
                passwd = User.objects.filter(username=username, password=old_password)
                if passwd:
                    User.objects.filter(username=username, password=old_password).update(
                        password=new_password)  ##如果用户名、原密码匹配则更新密码
                    info = '密码修改成功!'
                else:
                    info = '请检查原密码是否输入正确!'
            elif len(user) == 0:
                info = '请检查用户名是否正确!'

        return HttpResponse(info)
    else:
        uf = ChangeForm()
    return render('change.html', {'uf': uf})


# 注册
def register(request):
    if request.method == 'POST':
        # 实例化form对象的同时传入从网页通过post方式提交过来的参数
        form_obj = RegForms(request.POST)
        print(form_obj.is_valid())
        if form_obj.is_valid():
            print(form_obj.cleaned_data)
            models.objects.objects.create(**form_obj.cleaned_data)
            return HttpResponse("注册成功！")
        else:
            print("哈哈哈")
    else:
        # 实例化对象类
        form_obj = RegForms()

    return render(request, "register.html", {"form_obj": form_obj})


def store_index(request):
    type_list = ('手机', '平板&穿戴', '通用')
    name_list = ('荣耀', '畅玩', '华为', 'Mate','滚蛋')
    title = '你好?'
    # context = {'title': title, 'type_list': type_list, 'name_list': name_list}
    print(locals())
    return render(request, "huawei-shouye.html",context=locals(),status=200)


def download_register(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row', 'A', 'B', 'C'])
    return response
