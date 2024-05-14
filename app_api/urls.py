#!/usr/bin/env python
# coding=utf-8
# Created by huangxy on 2024/5/10 17:31
# Copyright 2024 Qfun, Inc. All rights reserved.
# Description:
from django.urls import path

from .views import test_global_request, test_multiple_language, test_api_performance, test_recycle_db


urlpatterns = [
    # 测试全局访问请求对象
    path('/test_global_request', test_global_request),
    # 测试多语言
    path('/test_multiple_language', test_multiple_language),
    # 测试接口耗时
    path('/test_api_performance', test_api_performance),
    # 测试回收断掉的数据库链接
    path('/test_recycle_db', test_recycle_db),
]
