#!/usr/bin/env python
# coding=utf-8
# Created by huangxy on 2024/5/7 10:58
# Copyright 2024 Qfun, Inc. All rights reserved.
# Description:
import os


class EnvironConfig:
    ENVIRON_DEV = 'DEV'
    ENVIRON_TEST = 'TEST'
    ENVIRON_PRODUCT = 'PRODUCT'


ENVIRON = os.environ.get('ENVIRON', EnvironConfig.ENVIRON_DEV)
