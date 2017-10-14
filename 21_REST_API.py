#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# 有些REST API会把参数放到URL中，比如GitHub的API: 
# GET /users/:user/repos
# 调用时，需要把:user替换为实际用户名。请实现如下的链式调用:
# Chain().users('michael').repos


class Chain(object):

    def __init__(self,path=''):
        self._path=path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self,paras):  # Chain( ).users也是返回了一个Chain实例，所以可以用__call__来调用
        return Chain('%s/%s' % (self._path, paras))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().users('michael').repos)