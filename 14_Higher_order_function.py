# -*- coding: utf-8 -*-

from math import sqrt 

def same(x,*fs):
    s=[f(x) for f in fs] 
    return s

a = int(input('Please enter the number you want to calculate: '))

print('The sqrt and abs value for this number is:',same(a,sqrt,abs))


# 变量可以指向函数
# 函数名也是变量
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为传入函数。

def do_sth(x=[],*func):
    return [f(x_k) for x_k in x for f in func]

b = input(r'Please enter the number/numbers you want to calculate: ')

print(do_sth((int(t) for t in b),abs,sqrt))
print(do_sth([1,2,4,16],abs,sqrt))