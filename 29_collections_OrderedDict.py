#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import OrderedDict
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity): # capacity：容量
        # 调用父类OrderedDict的构造函数，下面要用到父类的popitem等方法
        super().__init__()
        self._capacity = capacity
    def __setitem__(self, key, value):
        # containsKey=1时表示key已存在，则执行修改操作
        # containsKey=0时表示key不存在，则执行添加操作
        containsKey = 1 if key in self else 0
        # 当已达最大容量，当新加key不存在时，会运行这段，先删除最先添加的
        # 当key存在时，不会运行这段，会运行第2个if进行修改
        if len(self) - containsKey >= self._capacity:
            # popitem移除键值对并返回，last=true时按LIFO顺序返回
            # last=false时按FIFO顺序返回
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        # 调用父类的__setitem__方法写入键值对
        OrderedDict.__setitem__(self, key, value)

m_od = LastUpdatedOrderedDict(2)
# 容量为2，输入3个值时，会先将最先存入的删除再添加新的
m_od['a'] = 1
m_od['b'] = 2
m_od['c'] = 3
m_od['b'] = 4
print(m_od)
