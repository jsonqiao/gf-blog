#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015 - jsonqiao <scqiaoyang@gmail.com>

from django.db import models

# 博客文章
class Post(models.Model):
    id = models.BigIntegerField(primary_key=True)
    create_date = models.DateTimeField() # 创建时间
    modify_date = models.DateTimeField() # 最后修改时间
    author = models.CharField(max_length=50) # 作者
    title = models.TextField() # 文章标题
    content = models.TextField() # 文章内容
    status = models.IntegerField() # 文章状态 0-未发布 1-发布
    public_status = models.IntegerField() # 文章公开状态 0-公开 1-密码访问 2-私密
    comment_count = models.BigIntegerField() # 文章评论统计

# 需要密码访问的文章密码
class Post_Password(models.Model):
    id = models.BigIntegerField(primary_key=True)
    create_date = models.DateTimeField() # 创建时间
    modify_date = models.DateTimeField() # 最后修改时间
    post_id = models.ForeignKey(Post) # 博客
    password = models.CharField(max_length=50) # 密码