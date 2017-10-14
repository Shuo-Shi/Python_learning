#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

def is_palindrome(n):
    s=str(n)
    return s[::1]==s[::-1] and len(s)>2 # 将输入的数字转换为字符串之后方便使用切片来进行筛选
	
# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))

def is_palindrome2(n):
    s=str(n)
    for i in range(len(s)//2): # '//'来表示整数除法，返回不大于结果的一个最大的整数
        if s[i]!=s[-i-1]: # 利用下标来定位对称位置字符并进行判断
            return False
    return True


# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。