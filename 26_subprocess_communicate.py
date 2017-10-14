#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n') # communicate() 参数是标准输入，返回标准输出和标准出错
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

'''
Popen对象的方法函数：

http://blog.csdn.net/wirelessqa/article/details/7778761

poll() 检查是否结束，设置返回值

wait() 等待结束，设置返回值

communicate() 参数是标准输入，返回标准输出和标准出错

send_signal() 发送信号 (主要在unix下有用)

terminate() 终止进程，unix对应的SIGTERM信号，windows下调用api函数TerminateProcess()

kill() 杀死进程(unix对应SIGKILL信号)，windows下同上

stdin
stdout 参数中指定PIPE时，有用
stderr 

pid 进程id
 
returncode 进程返回值

其他参考：(Python多进程相关概念及解释 )
http://blog.go2live.cn/article-detials/17
'''
