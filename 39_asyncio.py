#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import asyncio
#
# # @asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# import threading
# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

import asyncio

async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(10.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
tasks = [print_sum(1, 2), print_sum(3, 4)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 先执行print_sum(3,4）（这边tasks额执行顺序我不是非常理解，我多加了很多task测验，发现都是从第二个开始执行，然后最后执行第一个task，没懂是为什么）
# 将3,4扔给compute，在compute中，sleep(10.0)挂起，此时不等待sleep(10.0)执行完毕，直接执行tasks中的另一个task，print_sum（1,2），
# 将1,2扔给compute，在compute中，sleep(10.0)挂起，
# 由于已经没有其他的task，所以等待第一个sleep（10.0)执行完毕以后返回3+4的结果为7，执行result = await compute(3, 4)后面的程序，即打印出3 + 4 = 7
# 执行完毕以后，第二个sleep（10.0）也差不多返回了，因此回到原来挂起的result = await compute(1, 2)，打印出1 + 2 = 3.
# 所有task执行完毕，loop complete并且close
