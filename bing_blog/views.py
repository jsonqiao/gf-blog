#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015 - jsonqiao <scqiaoyang@gmail.com>
import logging

from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.shortcuts import render_to_response

from models import Post


logger = logging.getLogger(__name__)

# 博客首页
def home_page(request):
    """
    分页查询博客 status = 1 已发布的
    :param request:
    :return:
    """
    posts = Post.objects.filter(status='1');
    paginator = Paginator(posts, 20)  # 每页20条
    pageNo = request.GET.get("pageNo");

    try:
        posts = paginator.page(pageNo)
    except PageNotAnInteger:  # 页码不是整数
        logger.error("page no isn't integer")
        posts = paginator.page(1)
    except EmptyPage:  # 页面太大没有相应记录
        logger.error("page no more than the max no")
        posts = paginator.page(paginator.num_pages)

    return render_to_response('index.html', {'post': posts})


def hello(requet):
    return HttpResponse("Hello World")