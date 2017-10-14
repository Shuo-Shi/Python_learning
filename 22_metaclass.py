#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# type()函数既可以返回一个对象的类型，又可以创建出新的类型，要创建一个class对象，type()函数依次传入3个参数：

# Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

#     class的名称；
#     继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#     class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# type()函数最大的好处是允许我们动态的创建类


# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# 通过metaclass来创建类，然后通过类来创建实例。metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”，而metaclass是类的模板。

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type): # 此处先定义了以个类的模板，具有方法add。
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list, metaclass=ListMetaclass): # 此处定义一个MyList类，继承类的模板ListMetaclass所有特性
    pass

# __new__()方法接收到的参数依次是：
#     当前准备创建的类的对象；
#     类的名字；
#     类继承的父类集合；
#     类的方法集合。

L = MyList([1,2])
L.add(3)

print(L)