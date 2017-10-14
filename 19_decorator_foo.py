#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

##########简单装饰器##########
# decorator的基本作用：以函数为参数，并且输出一个装饰后的新函数

import logging

def outer(somefunc):
    def inner():
        print('have not run', somefunc.__name__, end='\n')
        result = somefunc()
        print(result + ' finished')
    return inner
	
def foo(): # 该函数foo()为基本函数，上面的函数outer(somefunc)则为装饰器函数，用来给予基本函数插入新的功能
    return 'I am foo'

decorator = outer(foo)
decorator()

# 上述函数执行后输出：
# have not run foo
# I am foo finished

def use_logging(func): # 函数use_logging就是装饰器，它把执行真正业务方法的func包裹在函数里面，看起来像bar被use_logging装饰了。

    def wrapper(*args,**kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*args)
    return wrapper

@use_logging # @符号是装饰器的语法糖，在定义函数的时候使用，避免再一次赋值操作
def bar():
    print("I am bar")

bar() # 运用语法糖可以省去bar=use_logging(bar)这一句了，直接调用bar()即可得到想要的结果。

# 如果有其他的类似函数，可以继续调用装饰器来修饰函数，而不用重复修改函数或者增加新的封装。这样，就提高了程序的可重复利用性，并增加了程序的可读性。


##########带参数的装饰器##########
# 装饰器的语法允许我们在调用时，提供其他参数，比如@decorator(a)。这样，就为装饰器的编写和使用提供了更大的灵活性。

def use_logging2(level): # 带参数的装饰器，对原有装饰器的一个函数封装，并返回一个装饰器。可以理解为一个含有参数的闭包。
    def decorator(func):
        def wrapper(*args,**kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging2(level="warn") # 将默认值为"warn"的参数level传递到装饰器环境中
def foo2(name='foo'):
    print("I am %s" % name)

foo2()


##########functolls.wraps##########
# wraps本身也是一个装饰器，它能把原函数的元信息拷贝到装饰器函数中，这使得装饰器函数也有和原函数一样的元信息了。

from functools import wraps
# 或者import functools

def logged(func):
    @wraps(func)
    def with_logging(*args,**kwargs):
        print(func.__name__ + " was called")
        return func(*args,**kwargs)
    return with_logging

@logged
def f(x):
    """does some math"""
    return x + x*x

print(f.__name__) # prints 'f', 如果没有调用wraps装饰器，则返回'with_logging'
print(f.__doc__) # prints 'does some math', 如果没有调用wraps装饰器，则返回None

