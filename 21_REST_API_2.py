#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# 有些REST API会把参数放到URL中，比如GitHub的API: 
# GET /users/:user/repos
# 调用时，需要把:user替换为实际用户名。请实现如下的链式调用:
# Chain().users('michael').repos


class Chain(object):

    def __init__(self, path=''): # 帮助定制类的特殊函数：初始化函数
        self._path = path

    def __getattr__(self, path): # 当我们调用类的方法或属性时，如果不存在，就会报错，此时可以用__getattr__()方法，动态返回一个属性

        if path == 'users':
            return lambda user: Chain('%s/users/%s' % (self._path, user)) # 如果碰到函数名users，则返回新的链式调用Chain(之前已经录入的path+/users/，参数user作为新的path)

        return Chain('%s/%s' % (self._path, path))

    def __str__(self): # 通过__str__()方法，方便打印实例，返回一个好看的字符串
        return self._path

    __repr__ = __str__ # __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的

print(Chain().users('michael').repos)

# 如果path里有users，而非users(), 则此种方法会出现问题