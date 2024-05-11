#!/usr/bin/env python
# coding=utf-8
# Created by huangxy on 2024/5/10 17:31
# Copyright 2024 Qfun, Inc. All rights reserved.
# Description:
from django.urls import path

from .views import test_global_request, test_multiple_language


urlpatterns = [
    # 测试全局访问请求对象
    path('/test_global_request', test_global_request),
    # 测试多语言
    path('/test_multiple_language', test_multiple_language),
]
