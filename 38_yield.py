#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# http://blog.csdn.net/haskei/article/details/54908853

def h():
    print('Wen Chuan')
	# yield这个表达式是分两次完成的，第一次执行后半段，把5赋值给m2，下次send时才执行前一半，即把后一次send的输入赋值给m1
    m1 = yield 5  # 停止并返回value 5，到send命令处，所以赋值给m2为5
    print(m1) # m1的值是下一个send函数中包含的值
    d1 = yield 12
    print('We are together!')
c = h()
m2 = c.send(None)  #
d2 = c.send('Fighting!')  # 此时将'Fighting!'返回给之前yield断点处，并赋值给m1
print('We will never forget the date', m2, '.', d2)
c.close()


def f():
    print('start')
    a = yield 1
    print(a)
    print('middle....')
    b = yield 2  # 2这个值只是迭代值，调用next时候返回的值
    print(b)  # 传入的参数是给当前yield的，也就是yield 2，因为当前函数走到了yield 2，所以传入的参数没有给yield 1
    print('next')
    c = yield 3
    print(c)

a = f()
next(a)
next(a)
a.send('msg')
a.close()