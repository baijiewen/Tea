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
    ret = {'status': '', }
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
            print 'check Ok!'
            if User.objects.filter(username=user):
                return render(request, 'users/register.html', {'form': regForms, 'status': '用户名已注册'})
            else:
                User.objects.create_user(username=user, password=pwd)
                print 'register OK!'
                #return HttpResponse("注册成功")
                return redirect('/users/login', status='注册成功请登录' )
        else:
            return HttpResponse('请输入正确的格式!!')
    else:
        print 'BUG'
        return render(request, 'users/register.html', {'form': regForms})


def login(request):
    reqforms = forms.RegisterForm()
    if request.method == 'POST':
        form1 = forms.RegisterForm(request.POST)
        if form1.is_valid():
            user_name = request.POST.get('username', None)
            pwd = request.POST.get('password', None)

            #user_name = form1.cleaned_data["username"]
            #pwd = form1.cleaned_data["password"]
            print user_name, pwd
            print 'check Ok!'
            user = auth.authenticate(username=user_name, password=pwd)
            print user
            if user is not None:
                print '登录成功'
                auth.login(request, user)
                return redirect('/users/index')
            else:
                return HttpResponse('用户不存在请注册')
                print '登录失败'
        else:
            return HttpResponse('请输入正确的格式!!')
    return render(request, 'users/login.html', {'form1': reqforms})


def index(request):
    if request.user.is_authenticated():
        return render_to_response('users/index.html')
    else:
        print 'not login'
        return redirect('/users/login')







