#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print('Original list is:')
print(L)

def by_name(t):
    return t[0] 

L1 = sorted(L, key=by_name) # key=by_name这个是指取出这个list的每一个（key,value）元素，可以看成t=(key,value),t[0]就是key，t[1]就是value
print('Sorted by name:')
print(L1)

def by_score(t):
    return t[1]

L2 = sorted(L1,key=by_score,reverse=True)
print('Sorted first by name, then by score:')
print(L2)
