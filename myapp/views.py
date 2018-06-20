# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import redis
# Create your views here.

conn = redis.StrictRedis()
def index(request):
	if "username" not in request.COOKIES:
		return render(request,"loginPage.html",{})
	
