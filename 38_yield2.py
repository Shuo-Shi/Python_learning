#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# http://www.cnblogs.com/fangyuan1004/p/4571304.html

def i_yield_whatever_input_is():
    input = 0
    while True:
        print("1: before gi yield input=%s" % input)
        input = yield input
        print("2: after gi yield input=%s" % input)

# def wrap_generator1():
#     for i in i_yield_whatever_input_is():
#         print("3: before g1 yield i=%s" % i)
#         yield i
#
# g = wrap_generator1()
# print("4: after send None return: %s" % g.send(None))
# print("4: after send 1 return: %s" % g.send(1))
# print("4: after send 2 return: %s" % g.send(2))

# Output result:
# 1: before gi yield input=0
# 3: before g1 yield i=0
# 4: after send None return: 0
# 2: after gi yield input=None
# 1: before gi yield input=None
# 3: before g1 yield i=None
# 4: after send 1 return: None
# 2: after gi yield input=None
# 1: before gi yield input=None
# 3: before g1 yield i=None
# 4: after send 2 return: None

# 由于send的输入到wrap_generator后，无法输入给子生成器，因此，子生成器i_yield_whatever_input_is的输入是None，只能yield None。

def wrap_generator2():
    yield from i_yield_whatever_input_is()

g = wrap_generator2()
print("4: after send None return: %s" % g.send(None))
print("4: after send 1 return: %s" % g.send(1))
print("4: after send 2 return: %s" % g.send(2))

# Output result:
# 1: before gi yield input=0
# 4: after send None return: 0
# 2: after gi yield input=1
# 1: before gi yield input=1
# 4: after send 1 return: 1
# 2: after gi yield input=2
# 1: before gi yield input=2
# 4: after send 2 return: 2

