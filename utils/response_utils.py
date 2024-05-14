#!/usr/bin/env python
# coding=utf-8
# Created by huangxy on 2024/5/10 17:58
# Copyright 2024 Qfun, Inc. All rights reserved.
# Description:
from django.http import JsonResponse

from config.code_config import APPResponseCode


class APPResponse(JsonResponse):

    def __init__(self, code=APPResponseCode.SUCCESS, message='Success', data=None):
        response_data = dict(code=code, message=message, data=data)
        super().__init__(data=response_data)
