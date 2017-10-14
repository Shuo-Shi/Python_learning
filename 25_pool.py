#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Pool可以提供指定数量的进程，供用户调用，当有新的请求提交到pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；
但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来它。

pool.apply_async()用来向进程池提交目标请求
pool.join()是用来等待进程池中的worker进程执行完毕，防止主进程在worker进程结束前结束.但必pool.join()必须使用在pool.close()或者pool.terminate()之后。
其中close()跟terminate()的区别在于close()会等待池中的worker进程执行结束再关闭pool,而terminate()则是直接关闭。
result.successful()表示整个调用执行的状态，如果还有worker没有执行完，则会抛出AssertionError异常。
 '''


from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__': # name 是当前模块名，当模块被直接运行时模块名为 main 。这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
    print('Parent process %s.' % os.getpid())
    p = Pool(4) # 定义同时跑4个进程。
    for i in range(5): # 一共创建了5个进程，用同时只能跑4个进程的pool来执行
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close() # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.join() # 对Pool对象调用join()方法会等待所有子进程执行完毕
    print('All subprocesses done.')
