#!/usr/bin/env python
# coding=utf-8
# Created by huangxy on 2024/5/13 15:11
# Copyright 2024 Qfun, Inc. All rights reserved.
# Description:
from django.db import models
import datetime
from django.db.models import QuerySet


class BaseQuerySet(QuerySet):
    """重写QuerySet"""

    def update(self, **kwargs):
        if 'update_time' not in kwargs:
            kwargs.update(update_time=datetime.datetime.now())
        return super().update(**kwargs)


class BaseManager(models.Manager):
    """重写对象管理类"""

    def get_queryset(self):
        return BaseQuerySet(self.model, using=self._db)


class BaseModel(models.Model):
    create_time = models.DateTimeField(
        '创建时间', auto_now_add=True)
    update_time = models.DateTimeField(
        '更新时间', auto_now=True)

    objects = BaseManager()

    class Meta:
        abstract = True

    @classmethod
    def bulk_create(cls, data_list):
        """批量更新"""
        objects_to_insert = [cls(**data) for data in data_list]
        cls.objects.bulk_create(objects_to_insert)
