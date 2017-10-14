#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def consumer():
    r = ''
    while True:
        # 函数中包含yield，也就是说该函数是一个generator
		# consumer通过yield拿到消息，处理，又通过yield把结果传回
        n = yield r 
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = str('the %s time 200 OK' % n)

def produce(c):
    c.send(None) # 首先调用c.send(None)启动生成器，该语句与c.next()等同
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) # 把该函数中当前n的值传给consumer函数的对象c中去，并期待返回对象c中r计算的结果
        print('[PRODUCER] Consumer return: %s' % r)
    c.close() # produce决定不生产了，通过c.close()关闭consumer，整个过程结束

# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。	

c = consumer() # 把c设置成生成器，而不是调用函数
produce(c)