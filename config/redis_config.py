#!/usr/bin/env python
# coding=utf-8
# Created by huangxy on 2024/5/7 11:19
# Copyright 2024 Qfun, Inc. All rights reserved.
# Description:
import os


REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
DEFAULT_REDIS_DB = 1
OTHER_REDIS_DB = 2
