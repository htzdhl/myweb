# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField
class loginForm(forms.Form):
	username = forms.CharField(label = "账号",
							   max_length = 20,
							   min_length = 8,
							   error_messages={"required":"用户名不能为空",
											   "max_length":"用户名不能高于20个字符",
											   "min_length":"用户名不能低于8个字符"},
								widget=forms.widgets.TextInput(attrs={"class":"input","name":"username","placeholder":"请输入用户名"}))
	password = forms.CharField(label = "密码",
								max_length = 18,
								min_length=8,
								error_messages={"required":"密码不能为空",
												"max_length":"密码最大长度不能超过18个字符",
												"min_length":"密码最小长度不能低于8个字符"},
								widget=forms.widgets.PasswordInput(attrs={"class":"input","name":"password","placeholder":"请输入密码"})
								)
	auto_login = forms.CharField(label = "长期登录",
								widget = forms.widgets.CheckboxInput(attrs = {"name":"auto_login","id":"auto_login"}))
								

class registerForm(forms.Form):
	username = forms.CharField(label="账号",
								max_length=20,
								min_length = 8,
								error_messages={
									"required":"用户名不能为空",
									"max_length":"用户名不能高于20个字符",
									"min_length":"用户名不能低于8个字符"},
								widget = forms.widgets.TextInput(attrs={"class":"input","name":"username","placeholder":"请输入8-20个字符"}))
	password = forms.CharField(label = "密码",
								max_length = 18,
								min_length = 8,
								error_messages = {
									"required":"密码不能为空",
									"max_length":"密码最大长度不能超过18个字符",
									"min_length":"密码最小长度不能低于8个字符"},
								widget = forms.widgets.PasswordInput(attrs={"class":"input","name":"password","placeholder":"请输入8-18个字符"}))
	email = forms.EmailField(label = "邮箱",
							error_messages={
								"required":"邮箱不能为空"
							},
							widget = forms.widgets.TextInput(attrs={"class":"input","name":"email","placeholder":"请输入邮箱"}))
							
	captcha = CaptchaField()
	
	
	
								
								
								
								
								