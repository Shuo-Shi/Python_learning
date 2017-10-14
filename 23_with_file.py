#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from datetime import datetime
# 
# with open('test.txt', 'w') as f: # 'w'表示可写
#     f.write('今天是 ')
#     f.write(datetime.now().strftime('%Y-%m-%d'))
# 
# with open('test.txt', 'r') as f: # 'r'表示只读
#     s = f.read()
#     print('open for read...')
#     print(s)
# 
# with open('test.txt', 'rb') as f: # 'rb'表示以二进制读取，并且只读
#     s = f.read()
#     print('open as binary for read...')
# print('%s\n' % s)
# 
# with open('test.txt', mode='a+') as f: # 'a'表示以追加模式打开。'+'表示读写
#     print(f.tell())  # 这种方法简单地返回文件的当前位置读/写指针在文件.
#     f.seek(0)  # 指定文件读取指针的位置为0
#     print(f.read())
#     f.write(" append something")

f = open('test.txt', 'r')

result = list()

for line in f.readlines(): # 依次读取每行
    line = line.strip() #　去掉每行开头和结尾的空白字符
    if not len(line) or line.startswith('#'): # 如果该行为空白行或者注释行
        continue # 是的话跳过不处理
    result.append(line) # 不是的话，保存
# result.sort()

print('\n%s' % result)

open('test.txt','w').write('%s' % '\n'.join(result)) # 将数组形式

# .readline() 和 .readlines() 之间的差异是后者一次读取整个文件，象 .read() 一样。
# .readlines() 自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for ... in ... 结构进行处理。
# 另一方面，.readline() 每次只读取一行，通常比 .readlines() 慢得多。仅当没有足够内存可以一次读取整个文件时，才应该使用 .readline()。
