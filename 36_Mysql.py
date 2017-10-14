#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector

# change root password to yours:
conn = mysql.connector.connect(user='root', password='password', database='test')

cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()

#############################

# mysql> show databases;
# mysql> create database test;
# mysql> use test;
# mysql> show tables;
# mysql> describe user;
# mysql> select database();
# mysql> select * from user;
# mysql> select * from user where id=3;
# mysql> select * from user by id desc;
# mysql> insert into books (id, book_name) values('3', 'C++_learning')

# mysql> show variables like 'port';
# mysql> show variables like 'character%';
# character_set_client      为客户端编码方式；
# character_set_connection  为建立连接使用的编码；
# character_set_database    为数据库的编码；
# character_set_results     为结果集的编码；
# character_set_server      为数据库服务器的编码；
# mysql> status;
# mysql> show status like 'Threads%';
# Threads_cached : 代表当前此时此刻线程缓存中有多少空闲线程。
# Threads_connected :代表当前已建立连接的数量，因为一个连接就需要一个线程，所以也可以看成当前被使用的线程数
# Threads_created :代表从最近一次服务启动，已创建线程的数量。
# Threads_running :代表当前激活的（非睡眠状态）线程数。并不是代表正在使用的线程数，有时候连接已建立，但是连接处于sleep状态，这里相对应的线程也是sleep状态。
# mysql> show variables like '%datadir%';

# Mysql 命令大全
# http://www.cnblogs.com/zhangzhu/archive/2013/07/04/3172486.html

