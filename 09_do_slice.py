#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack'] 


print('L[0:3] =', L[0:3]) 
print('L[:3] =', L[:3]) 
print('L[1:3] =', L[1:3]) 
print('L[-2:] =', L[-2:]) 


R = list(range(100)) 
print('R[:10] =', R[:10]) 
print('R[-10:] =', R[-10:]) 
print('R[10:20] =', R[10:20]) 
print('R[:10:2] =', R[:10:2])
print('R[:88:-2] =', R[:88:-2]) 
print('R[::5] =', R[::5]) 


# 表里面分别列出了使用正索引和负索引来定位字符的情况.
# 0  1  2  3
# a  b  c  d
# -4 -3 -2 -1

# 正向索引时,索引值开始于 0,结束于总长度减 1(因为我们是从 0 开始索引的)
# 在进行反向索引操作时,是从-1 开始,向字符串的开始方向计数,到字符串长度的负数为索引的结束。