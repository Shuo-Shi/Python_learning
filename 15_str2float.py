#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

from functools import reduce

def str2float(s):
    return reduce(lambda x,y:x*10+y, map(int, s[:s.index('.')]))+reduce(lambda x,y:x*0.1+y, map(int, s[:s.index('.'):-1]))*0.1

print('str2float(\'123.456\') =', str2float('123.456'))


# 其他练习：
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

# -*- coding: utf-8 -*-

# def normalize(name):
#     name.lower()
#     return name.capitalize()

# 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

# -*- coding: utf-8 -*-

# from functools import reduce

# def prod(L):
#     def fn(x,y):
#         return x*y
#     return reduce(fn, L)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))