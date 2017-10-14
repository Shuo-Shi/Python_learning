# -*- coding: utf-8 -*-

def triangles():
    L = [1]
    while True:
        yield L # 定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
		

# 上面完成了生成器generator triangles的编写，如果要调用，需要先生成一个generator对象，然后用next()函数不断获得下一个返回值：
# >>> t=triangles()
# >>> next(t)
# >>> [1]
# >>> next(t)
# >>> [1,1]
# >>> next(t)
# >>> [1,2,1]
# >>> next(t)
# >>> [1,3,3,1]

# generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# 另外一种调用生成器的办法如下：
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的。
