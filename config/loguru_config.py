#!/usr/bin/env python
# coding=utf-8
# Created by huangxy on 2024/5/7 11:07
# Copyright 2024 Qfun, Inc. All rights reserved.
# Description:
# django_test/config/loguru_config.py
from loguru import logger
import os
from datetime import datetime
# from django_test.settings import BASE_DIR
from django.conf import settings


class LoguruConfig:

    @staticmethod
    def setup(name):
        log_directory = f"{settings.BASE_DIR}/logs/"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        today_str = datetime.now().strftime("%Y-%m-%d")
        log_filename = f"{log_directory}/{name}_{today_str}.log"

        # 自定义输出的日志格式
        log_format = ("<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | "
                      "<cyan>{extra[type]}</cyan> | <white>{message}</white>")

        # 设置一个文件记录器，使用过滤器确保只记录与此记录器相关的日志
        logger.add(
            os.path.join(log_directory, log_filename),
            filter=lambda record: record["extra"].get("type") == name,
            rotation="100 MB",
            retention="10 days",
            compression="zip",
            format=log_format
        )

        return logger.bind(type=name)


# 创建不同的日志记录器实例
main_logger = LoguruConfig.setup("main")  # 主业务逻辑日志
scheduler_logger = LoguruConfig.setup("scheduler")  # 定时器执行日志
api_logger = LoguruConfig.setup("api_performance")  # 接口性能耗时日志
