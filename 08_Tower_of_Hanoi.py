#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

def move(n, a, b, c):
    if n==1:
        return print(a,'-->',c)
    else:
	# 把n看做当前需要移动的盘子数，a看作盘子移动的起始位置，b看作中间位置，c看作目标位置
	# 把所有盘子n分成最底下的盘子X和上面所以剩下的n-1个盘子Y
	# 分三步走：
	    # 第一步：把n-1个盘子Y移动到中间位置b
        move(n-1, a, c, b)
		# 第二步：把最大的盘子从起始位置a移动到最终位置c，并打印出来
        print('%s --> %s' % (a,c))
		# 第三步：把n-1个盘子Y从中间位置b移动到最终位置c，此时可以将中间位置b看作起始位置，而之前的起始位置a变成了中间位置
        move(n-1, b, a, c)
		
move(4,'A','B','C')
