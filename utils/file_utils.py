#!/usr/bin/env python
# coding=utf-8
# Created by huangxy on 2024/5/14 16:49
# Copyright 2024 Qfun, Inc. All rights reserved.
# Description:
from csv import DictWriter
from io import StringIO
import codecs
from django.http import HttpResponse
import csv


def parser_csv(key_title_tuple, csv_data):
    """
    生成CSV数据
    :param key_title_tuple: 键和标题
    :param csv_data: 导出数据列表
    :return:
    """
    io = StringIO()

    fieldnames = [key for key, title in key_title_tuple]
    writer = DictWriter(io, fieldnames=fieldnames)

    writer.writerow(dict(key_title_tuple))
    for row in csv_data:
        writer.writerow({key: row[key] for key in fieldnames})

    return io.getvalue()


def export_data(data, filename='data'):
    """
    直接访问浏览器导出文件数据
    :param data:
    :param filename:
    :return:
    """
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(filename)
    response['Content-Type'] = 'text/csv'
    response.write(codecs.BOM_UTF8)
    writer = csv.writer(response)
    for item in data:
        writer.writerow(item)
    return response
