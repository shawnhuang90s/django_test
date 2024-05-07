#!/usr/bin/env python
# coding=utf-8
# Created by huangxy on 2024/5/7 11:08
# Copyright 2024 Qfun, Inc. All rights reserved.
# Description:
def import_env():
    import os
    import sys
    from pathlib import Path
    import django

    root_path = str(Path(__file__).resolve().parent.parent)
    sys.path.insert(0, root_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_test.settings")
    print(f'root_path:{root_path}')

    django.setup()


def log_test():
    from config.loguru_config import main_logger, api_logger, scheduler_logger

    main_logger.debug("This is a debug log message.")
    main_logger.info("This is an info log message.")
    main_logger.warning("This is a warning log message.")
    main_logger.error("This is an error log message.")
    main_logger.critical("This is a critical log message.")
    api_logger.info("111111111111111111")
    scheduler_logger.info("222222222222222222")


if __name__ == '__main__':
    import_env()
    log_test()
