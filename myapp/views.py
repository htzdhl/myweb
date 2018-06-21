# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from myforms import *
from cache import *
import redis
# Create your views here.

conn = redis.StrictRedis()



def index(request):
	form = loginForm()
	if "username" not in request.COOKIES:
		return render(request,"loginPage.html",{"form":form})
	
def login(request):
	if request.method == "POST":
		form = loginForm(request.POST)
		if form.is_valid:
			username = request.POST["username"]
			password = request.POST["password"]
			login_redis_lua = script_load(login_lua)
			#if login_redis_lua(conn,["user:"+username],[password]):
			if conn.exists("user:"+username):
				return render(request,"main.html",{"user":username})
			message = "账号或密码错误"
			return render(request,"loginPage.html",{"from":form,"message":message})
		form = loginForm()
		return render(request,"loginPage.html",{"form":form})