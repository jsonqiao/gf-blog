#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015 - jsonqiao <scqiaoyang@gmail.com>

from django.http import HttpResponse

# 博客首页
def home_page(request):
    return HttpResponse("This is home page")


def hello(requet):
    return HttpResponse("Hello World")