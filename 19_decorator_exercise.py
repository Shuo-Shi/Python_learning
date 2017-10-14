#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

# import logging
# from functools import wraps
# 
# def log(text):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             logging.warn("begin to call %s" % func.__name__)
#             return func(*args)
#         return wrapper
#     return decorator
# 
# @log('execute')
# def f():
#     print('function %s is under execution' % f.__name__)
#     logging.warn("call %s is ended" % f.__name__)
# 
# f()

import functools

def log(arg):
    def dec(func, txt = 'call'):
        @functools.wraps(func)
        def wrp(*args, **kw):
            print('%s %s():' % (txt, func.__name__))
            return func(*args, **kw)
        return wrp

    if callable(arg):
        return dec(arg)
    else:
        print('return dec(f,arg)')
        return lambda f: dec(f, arg)

@log # 相当于定义了whoru=log(whoru)，因为whoru是callable的函数，所以返回decorator函数，该函数的是decorator函数dec(whoru,'call')，第一个参数是whoru，第二个参数使用默认值'call'，返回值最终是wrp函数
def whoru():
    print('using @log\n')
whoru()

@log('EXEC') # 相当于定义了whoru=log('EXEC')(whoru): 首先执行log('EXEC')，not callable，所以返回的是decorator函数，此时(whoru)再作为函数参数输入，并赋值给f，从而生成函数dec(whoru,'EXEC')，返回值最终是wrp函数。
def whoru():
    print('using @log(\'EXEC\')\n')
whoru()


# import functools
# 
# def log(arg):
#     if isinstance(arg, str): # 对装饰器参数arg做一个判断，是否为字符串
#         def dec(func):
#             @functools.wraps(func)
#             def wrp(*args, **kw):
#                 print('%s %s():' % (arg, func.__name__))
#                 return func(*args, **kw)
#             return wrp
#         return dec
#     else:
#         @functools.wraps(arg)
#         def wrp(*args, **kw):
#             print('call %s():' % arg.__name__)
#             return arg(*args, **kw)
#         return wrp
# 
# @log
# def whoru():
#     print('i am who i am')
# whoru()
# 
# @log('EXEC')
# def whoru():
#     print('i am who i am')
# whoru()


