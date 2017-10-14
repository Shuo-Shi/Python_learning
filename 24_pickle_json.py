#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' 

把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling。

Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。

json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。
但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，
既做到了接口简单易用，又做到了充分的扩展性和灵活性。

'''

import pickle

d = dict(name='Bob', age=20, score=88)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)

import json

data = json.dumps(d)
print('JSON Data is a str:', data)
reborn = json.loads(data)
print(reborn)

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__) # 把任意class的实例变为dict，然后就可以序列化为JSON
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score'])) # 要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
print(rebuild)