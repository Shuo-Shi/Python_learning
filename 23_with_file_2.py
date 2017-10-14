#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 定义一个函数，打印当前目录下所有包含str字符串的文件
def prtstr(current_path,str):
    dirlist = os.listdir(current_path) # 获取current_path目录下所有文件和目录，以list形式储存
    key = 0

    while True:
        if (key < len(dirlist)) and (str in dirlist[key]):
            print(os.path.join(current_path,dirlist[key]))
        key += 1
        if key == len(dirlist):
            break


str = input('Please input the str you want to search:\n')
current_path = os.getcwd()

# 定义一个函数，打印当前目录的所有子目录下包含str字符串的文件
def sub_prtstr(current_path,str):
    for root, dirs, files in os.walk(current_path): # 遍历current_path目录，root为目录路径，dirs为该目录下所有子目录的list，files为该目录下所有文件的list
        if len(dirs)>0:
            k=0
            while k < len(dirs):
                prtstr(os.path.join(root,dirs[k]),str)
                sub_prtstr(os.path.join(root,dirs[k]),str)
                k += 1
            if k == len(dirs):
                break
        
        else:
            pass

prtstr(current_path,str)
sub_prtstr(current_path,str)
