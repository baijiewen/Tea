#!/usr/bin/env python
#coding:utf-8

from django.shortcuts import render, render_to_response, redirect
from . import models
from . import forms
from django.http import HttpResponse
from django.template import RequestContext

from django.contrib.auth.models import User
import django.contrib.auth as auth
# Create your views here.


def register(request):

    regForms = forms.RegisterForm()
    # if request.method == 'POST':
    #     form = forms.RegisterForm(request.POST)
    #     if form.is_valid():
    #         user = form.cleaned_data["username"]
    #         pwd = form.cleaned_data["password"]
    #         user_list = models.UserInfo.objects.filter(username=user)
    #         if len(user_list) == 1:
    #             return HttpResponse('用户已注册请登录!!')
    #         else:
    #             models.UserInfo.objects.create(username = user, password = pwd)
    #             return HttpResponse('注册成功!!')
    #     else:
    #         return HttpResponse('请输入正确的格式!!')
    # else:
    #     return render(request, 'users/register.html', {'form': regForms})
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["username"]
            pwd = form.cleaned_data["password"]
            try:
                User.object.get(username=user)
                return HttpResponse("用户名已存在")
            except:
                User.objects.create(username=user, password=pwd)
                return HttpResponse("注册成功")
                return redirect('/user/login')
        else:
            return HttpResponse('请输入正确的格式!!')
    else:
        return render(request, 'users/register.html', {'form': regForms})


def loginView(request):
    reqForms = forms.RegisterForm()
    if request.method == 'POST':
        form1 = forms.RegisterForm(request.POST)
        if form1.is_valid():
            user_name = form1.cleaned_data["username"]
            pwd = form1.cleaned_data["password"]
            user = auth.authenticate(username=user_name, password=pwd)
            if user:
                print '登录成功'
                auth.login(request, user)
                return redirect('/users/index')
            else:
                print '登录失败'
        else:
            return HttpResponse('请输入正确的格式!!')
    return render(request, 'users/login.html', {'form1': reqForms})


def index(request):
    if request.user.is_authenticated():
        return render_to_response('users/index.html')
    else:
        print 'not login'
        return redirect('/users/login')







