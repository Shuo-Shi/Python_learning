#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，
# 这样，写代码更简单，不用直接操作SQL语句。
# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

' Simple ORM using metaclass '

# 先定义Field类，负责保存数据表的字段名和字段类型：
class Field(object): 

    def __init__(self, name, column_type): # __init__方法的第一个参数永远是self，表示创建的实例（对象）本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
        self.name = 'test1'+name # 绑定属性name到实例本身（name属性设置）
        self.column_type = column_type # 绑定属性column_type到实例本身（column_type属性设置）

    def __str__(self): # 通过__str__()方法来返回易阅读的字符串
        return '<%s><%s:%s>' % (self.column_type, self.__class__.__name__, 'test2'+self.name) # self.__class__表示该实例的类
        # __name__是特殊字段：
        # 1.如果模块是被导入，__name__的值为模块名字
        # 2.如果模块是被直接执行，__name__的值为’__main__’

# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field): # 继承类Field定义数据库字符串类型

    def __init__(self, name): # 实例化
        super(StringField, self).__init__('test3'+name, 'varchar(100)') 
        # 执行父类Field的实例化函数__init__()来创建字符串实例，必须传入与__init__方法匹配的参数，但self不需要传入，对应column_type此时传入默认类型为varchar(100)
        # 关于关键字super：
        # 1. super并不是一个函数，是一个类名，形如super(B, self)事实上调用了super类的初始化函数，产生了一个super对象；
		# 2. super类的初始化函数并没有做什么特殊的操作，只是简单记录了类类型和具体实例；
        # 3. super(B, self).func的调用并不是用于调用当前类的父类的func函数，而是沿着mro中该类的所有基类的类型序列依次调用。
        # 4. Python的多继承类是通过mro的方式来保证各个父类的函数被逐一调用，而且保证每个父类函数只调用一次（如果每个类都使用super）；
        # 5. 混用super类和非绑定的函数是一个危险行为，这可能导致应该调用的父类函数没有调用或者一个父类函数被调用多次。

class IntegerField(Field): # 继承类Field定义数据库整数类型

    def __init__(self, name):
        super(IntegerField, self).__init__('test4'+name, 'bigint')

# 定义Model类的类模板
class ModelMetaclass(type): # metaclass是类的模板，所以必须从’type’类型派生。

    def __new__(cls, name, bases, attrs): # 实例化类。
    # 固定写法，__new__()接收到的参数依次是：
    # 1. 当前准备创建的类，类似于self，但是self指向的是instance，而这里cls指向的是class
    # 2. 类的名字，也就是我们通常用类名.__name__获取的。
    # 3. 类继承的父类集合
    # 4. 类的方法集合 （属性的dict。dict的内容可以是变量(类属性），也可以是函数（类方法）。）
        if name=='Model': # 如果是类名是Model，则直接返回。即创建了该实例，但没有做任何方法的定义。
            return type.__new__(cls, name, bases, attrs)
        # 如果类名不是Model，则执行下面代码：
        print('Found model: %s' % name) # 输出打印类名（User类的类名User）
        mappings = dict() # 定义一个字典（key-value）
        print('\nbases=', bases)
        print('\noriginal attrs:', attrs)
        print('\n')
        for k, v in attrs.items(): # 遍历类的属性。字典items()函数以列表返回可遍历的(键, 值) 元组数组
            if isinstance(v, Field): # 判断v是否为Field类型的对象
                print('Found mapping: %s ==> %s' % (k, v)) # 是的话，输出属性名和值
                mappings[k] = v # 储存到mappings字典中
        print('\nmappings.keys()=', mappings.keys())
        print('\nmappings.values()=', mappings.values())
        for k in mappings.keys(): # 循环遍历删除attrs所有属性（User的四个属性）
            print('delete founded values %s from attrs dict' % attrs[k])
            attrs.pop(k) # pop(k)即删除下边（索引）为k的对象
        attrs['__mappings__'] = mappings # 保存筛选出来的User的属性和列的映射关系
        attrs['__table__'] = name # 保存该类的类名（User）为表名
        # 此时类的属性dict中所有关于User的属性都被删除并集合为一个新的属性dict：'__mapping__'中。
        # 同时还新增了一个属性__table__用来存储以该类名（User）命名的表名
        print('\nattrs after deletion:', attrs)
        return type.__new__(cls, name, bases, attrs)

# 使用类模板ModelMetaclass来创建类Model
class Model(dict, metaclass=ModelMetaclass): # 定义Model类

    def __init__(self, **kw): # kw是关键字参数，kw接收的是一个dict。
        super(Model, self).__init__(**kw) # 调用父类(dict)的实例化函数

    def __getattr__(self, key): # 根据key来查找value值，找不到则抛出异常
        try:
            print('self[key]=',self[key])
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value): # 给key赋值value
        self[key] = value

    def save(self): # 定义保存函数的方法
        fields = [] # 定义字段数组
        params = [] # 定义参数数组
        args = [] # 定义值
        print('\nself=',self)
        print('\nself.__mappings__.items()=',self.__mappings__.items())
        for k, v in self.__mappings__.items(): # 遍历实例的__mappings__属性（实例u,具备User类的属性）
            print('\nv.name=',v.name)
            fields.append(v.name) # 赋值属性名。此时v为具体的一个StringField或者IntegerField的实例，然后调用该实例的name属性，在两层实例化的时候分别添加了test3(4)和test1字符串
            params.append('?') # 赋值参数名
            args.append(getattr(self, k, None)) # 根据__mappings__中的k值获取实例u属性dict中的value值并赋值
            print('object v is:',v) # e.g. <StringField:username>，此处调用Field类中的__str__()私有函数，字符串test2在此时被添加
            print('str(k)=',str(k)) # e.g. name
            print('args=',args) # e.g ['Michael']
        print('\nGenerated fields:',fields)
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params)) # str.join(List):以str分隔List内元素
        print('SQL: %s' % sql) # 打印sql
        print('ARGS: %s' % str(args)) # 打印值

# 编写调用接口，即定义一个User类来操作对应的数据库表:
class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个User类的实例
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')

# 保存到数据库
u.save()

# 输出如下：
# Found model: User
# Found mapping: email ==> <StringField:email>
# Found mapping: password ==> <StringField:password>
# Found mapping: id ==> <IntegerField:uid>
# Found mapping: name ==> <StringField:username>
# SQL: insert into User (password,email,username,id) values (?,?,?,?)
# ARGS: ['my-pwd', 'test@orm.org', 'Michael', 12345]

# class Student(Model):
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#     classnumber = IntegerField('classnumber')
# 
# s = Student(id=67890, name='Allen', email='allen@orm.org', password='std-pwd', classnumber=5)
# 
# s.save()
