#!/usr/bin/env python
# coding=utf-8
# Created by huangxy on 2024/5/11 17:56
# Copyright 2024 Qfun, Inc. All rights reserved.
# Description:
import time
from functools import wraps
from config.loguru_config import api_logger
from django.db import connections


def track_performance(threshold=0):
    """
    装饰器：用于跟踪函数的执行时间，单位毫秒
    :param threshold: int 或 float, 函数执行时间的报告阈值，单位为毫秒
    :return:
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000  # 将秒转换为毫秒
            # 如果执行时间超过阈值，则记录或报告
            if elapsed_time > threshold:
                api_logger.error(
                    f"track_performance function '{func.__name__}' took {elapsed_time:.2f} ms to complete, "
                    f"which exceeds the threshold of {threshold} ms.")
            return result
        return wrapper
    return decorator


def recycle_db_conns(func):
    """回收断掉的数据库链接"""
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        for conn in connections.all():
            conn.close_if_unusable_or_obsolete()
            # 真实检查一下连接是否可用，不可用就关闭，下次使用的时候自动创建
            if conn.connection and not conn.is_usable():
                conn.close()
        return func(*args, **kwargs)
    return func_wrapper
