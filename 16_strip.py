#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

def not_empty(s):
    return s and s.strip() # 此处做了一个判断，如果元素即存在原始序列中，有存在去空之后的序列中，则返回True，否则False

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。