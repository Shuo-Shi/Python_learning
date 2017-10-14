#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

class A:
    def __init__(self,url):
        self.url = url
    def out(self):
        return self.url


a = A('news.163.com')
print(a.out())

b = a.__class__('www.bccn.net')
print(b.out())


print(A)
print(a.__class__)

# 可以看出a.__class__就等效于a的类A