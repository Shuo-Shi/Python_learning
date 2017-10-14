#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
# SQLAlchemy用一个字符串表示连接信息：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：
# 创建session对象:
session = DBSession() # DBSession对象可视为当前数据库连接。
# 创建新User对象:
new_user1 = User(id='5', name='Bob')
new_user2 = User(id='3', name='Allen')
# 添加到session:
session.add(new_user1)
session.add(new_user2)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user1 = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user1))
print('name:', user1.name)
# 关闭Session:
session.close()

# 如果一个User拥有多个Book，就可以定义一对多关系如下:
# class User(Base):
#     __tablename__ = 'user'
# 
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # 一对多:
#     books = relationship('Book')
# 
# class Book(Base):
#     __tablename__ = 'book'
# 
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # “多”的一方的book表是通过外键关联到user表的:
#     user_id = Column(String(20), ForeignKey('user.id'))
