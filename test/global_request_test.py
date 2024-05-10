#!/usr/bin/env python
# coding=utf-8
# Created by huangxy on 2024/5/10 17:02
# Copyright 2024 Qfun, Inc. All rights reserved.
# Description:
from django_middleware_global_request import get_request


def global_request_test():
    request = get_request()
    print(f'可以直接在自定义的函数或类中获取到当前请求对象：{request}')
