#!/usr/bin/env python
#coding:utf-8

from django.shortcuts import render, render_to_response
from . import models
from . import forms
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.

def Register(request):
    regForms = forms.RegisterForm()

    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["username"]
            pwd = form.cleaned_data["password"]
            user_list = models.UserInfo.objects.filter(username=user)
            if len(user_list) == 1:
                return HttpResponse('用户已注册请登录!!')
            else:
                models.UserInfo.objects.create(username = user, password = pwd)
                return HttpResponse('注册成功!!')
        else:
            return HttpResponse('请输入正确的格式!!')
    else:
        return render(request, 'users/register.html', {'form':regForms})




