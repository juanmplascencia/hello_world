# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index( request ):
    return render(request, "HelloWorld/index.html")

def login(request):
	return render(request, "HelloWorld/login.html")
