#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，
它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，

多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，
所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。


当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。
锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，
坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，
只能靠操作系统强制终止。

Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，
然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，
所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。
所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。
不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。
'''

# import threading
# 
# balance = 0
# lock = threading.Lock()
# 
# def run_thread(n):
#     for i in range(100000):
#         # 先要获取锁:
#         lock.acquire()
#         try:
#             # 放心地改吧:
#             change_it(n)
#         finally:
#             # 改完了一定要释放锁:
#             lock.release()

			
import threading
import time

def target():
    print('the curent threading  %s is running' % threading.current_thread().name)
    time.sleep(1)
    print('the curent threading  %s is ended' % threading.current_thread().name)

print('the curent threading  %s is running' % threading.current_thread().name)
t = threading.Thread(target=target)

t.setDaemon(True) # 把子线程设置为daemon
t.start()
t.join() # join就是等待该线程执行完成
print('the curent threading  %s is ended' % threading.current_thread().name)

# python的主线程会在即将退出时检查所有的非daemon且alive的线程,一个一个调用join方法。所以设置子线程为daemon，并用join等待线程完成，之后主线程才能够结束

# 上述程序输出为：
# the curent threading MainThread is running
# the curent threading Thread-1 is running
# the curent threading Thread-1 is ended
# the curent threading MainThread is ended

# 更详细参考：
# http://blog.go2live.cn/article-detials/16
