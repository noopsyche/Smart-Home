#!/usr/bin/python
# -*- coding: utf-8 -*-


def debug(msg):
    print("调试：" + msg)


def normal(msg):
    print("正常：" + msg)


def warning(msg):
    print("警告：" + msg)


def error(msg):
    print("错误：" + msg)


def exp(msg, e):
    print("异常：" + msg + " \n 异常信息：", e)

