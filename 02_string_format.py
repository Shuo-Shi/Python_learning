# -*- coding: utf-8 -*-

s1 = 72
s2 = 85
r = (s2-s1)/s1*100
# %%表示此时%不是用来格式化字符串的运算符，而只是普通的%字符串
# %.1f表示转换为只保留小数点后一位的浮点数
print('growth rate: %.1f%%' % r)