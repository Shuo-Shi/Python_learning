#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 


def print_scores(**kw): 
    print('      Name  Score') 
    print('------------------') 
    for name, score in kw.items(): # 字典items函数随机顺序以列表返回可遍历的(键, 值) 元组数组
        print('%10s  %d' % (name, score)) 
    print() 


print_scores(Adam=99, Lisa=88, Bart=77) 


data = { 
    'Adam Lee': 99, 
    'Lisa S': 88, 
    'F.Bart': 77 
} 

# 因为data是一个dict，所以print的时候会自动按照首字母顺序排序
print_scores(**data) 


def print_info(name, *, gender, city='Beijing', age): 
    print('Personal Info') 
    print('---------------') 
    print('   Name: %s' % name) 
    print(' Gender: %s' % gender) 
    print('   City: %s' % city) 
    print('    Age: %s' % age) 
    print() 


print_info('Bob', gender='male', age=20) 
print_info('Lisa', gender='female', city='Shanghai', age=18) 
