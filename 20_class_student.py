#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

class Student(object): # (object)，表示该类是从哪个类继承下来的，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

    def __init__(self, name, score): # 在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
        self.name = name # Student类对应的object实例具有初始化姓名和分数的__init__的private method私有方法，以及定义的属性name，score
        self.score = score

    def print_score(self): # 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
        print('%s: %s' % (self.name, self.score))

    def get_grade(self): #　这些封装数据的函数get_grade()是和Student类本身是关联起来的，我们称之为类的方法(Method)
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.name)
print('bart.score =', bart.score)
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())

bart.age=21 # 根据类（Student）创建的实例（bart）可以任意绑定属性（age）
print('age of Bart:',bart.age)

def set_age(self,age): # 创建一个方法
    self.age=age

Student.set_age=set_age # 给类Student绑定这个创建的方法

bart.set_age(25) # 对应类的实例就可以调用这个方法
print('age of Bart:',bart.age)

# 通常情况下，上面的set_age方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。