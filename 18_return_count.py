#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs  # 每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了，返回的函数并没有立刻执行，而是直到调用了f()才执行。

f1, f2, f3 = count() # 创建的3个函数依次指向三个函数

print(f1(),f2(),f3())

# 你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是全部都是9！
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def count2():
    def f(j):
        def g():
            return j*j
        return g # 返回的是一个函数，这个函数完成平分计算，并且该函数的参数为平方计算当前的值
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
	
f1, f2, f3 = count2()

print(f1(),f2(),f3())

# 小结：一个函数可以返回一个计算结果，也可以返回一个函数。返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。


