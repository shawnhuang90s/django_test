#!/usr/bin/env python
# coding=utf-8
# Created by huangxy on 2024/5/7 11:21
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


def redis_test():
    from django.core.cache import caches

    # 获取 default 缓存
    default_cache = caches['default']
    default_cache.set('key', 'value', timeout=300)
    print(default_cache.get('key'))

    # 获取 other_cache 缓存
    other_cache = caches['other_cache']
    other_cache.set('another_key', 'another_value', timeout=300)
    print(other_cache.get('another_key'))


if __name__ == '__main__':
    import_env()
    redis_test()
