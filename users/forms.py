#!/usr/bin/env python
#coding:utf-8

from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"请输入用户名",
                "required":"required"}),max_length=50,error_messages={"required":"用户名不能为空",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"请输入密码",
                "required":"required"}),max_length=50,error_messages={"required":"密码不能为空",})

