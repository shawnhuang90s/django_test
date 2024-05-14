#!/usr/bin/env python
# coding=utf-8
# Created by huangxy on 2024/5/10 17:58
# Copyright 2024 Qfun, Inc. All rights reserved.
# Description:
from django.http import JsonResponse, HttpResponse

from config.code_config import APPResponseCode


class APPResponse(JsonResponse):

    def __init__(self, code=APPResponseCode.SUCCESS, message='Success', data=None):
        response_data = dict(code=code, message=message, data=data)
        super().__init__(data=response_data)


class DownloadResponse(HttpResponse):

    def __init__(self, filename, **kwargs):
        super().__init__(**kwargs)
        self["Content-Type"] = "application/octet-stream"
        self['Content-Disposition'] = f"attachment; filename*={filename}"
        self["Access-Control-Expose-Headers"] = "Content-Disposition"

        self["Access-Control-Allow-Origin"] = "*"
        self["Access-Control-Allow-Methods"] = "POST,GET,OPTIONS,HEAD"
        self["Access-Control-Max-Age"] = "1000"
        self["Access-Control-Allow-Credentials"] = "true"
        self["Access-Control-Allow-Headers"] = "*"
