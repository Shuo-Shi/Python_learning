#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

class Person(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, first_name, last_name):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
 
    #----------------------------------------------------------------------
    @property
    def full_name(self): # 通过property装饰器，将类的一个方法转换为了一个属性，在后面调用的时候就直接是person.full_name而不是person.full_name()
        """
        Return the full name
        """
        return "%s %s" % (self.first_name, self.last_name)

person = Person("Mike", "Driscoll")
print(person.full_name)