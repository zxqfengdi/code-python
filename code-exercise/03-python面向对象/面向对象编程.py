# -*- coding:utf-8 -*-

"""
Name: 面向对象编程.py
Author: fengdi
Datetime: 17:08 2019/5/8 
Description: 主要介绍python面向对象编程的相关内容，即类的相关内容。面向对象的设计思想是抽象出类，根据类创建实例。

"""

# 类和实例：类是一系列具有相同属性和方法的对象的集合。实例是一个具体的对象。
# 类定义：使用class关键字定义类 形式：class 类名(父类):默认最终都会继承与object类


class Animal(object):
    """define a animal class"""
    def __init__(self, name, age):   # 类创建实例时首先调用__init__方法初始化对象属性，self参数指向创建的实例本身
        self.name = name
        self.age = age

    def greet(self):   # 定义方法，第一个参数为self，指向创建的实例本身
        print('The dog\'s name is %s.' % self.name)


mydog = Animal('taidi', 8)   # 类的实例化过程
print(type(Animal), Animal)
print(type(mydog), mydog)

mydog.greet()  # 调用类里面定义的方法

# 访问限制：python通过变量形式表示权限。（以__开头的属性和方法为私有属性和方法，只能从内部访问；以__开头和__结尾的变量为特殊变量，可直接访问）
# 以_开头的变量默认被视为私有变量，不可随意访问


class Myanimal(object):
    """define a class"""

    def __init__(self, name, age, color):
        self.__name = name    # 私有变量
        self.__age__ = age    # 特殊变量
        self._color = color   # 私有变量

    def __getname(self):
        return 'The name is %s' % self.__name

    def get_name(self):
        return self.__getname()


dog = Myanimal('taidi', 5, 'blue')
print(type(dog), dog)
print(dir(dog))
print(type(Myanimal), Myanimal)
print(dir(Myanimal))

# print(dog.__name)    # __开头变量为私有变量，只能从内部访问
print(dog.__age__)   # 特殊变量，可直接访问
print(dog._color)    # 非私有变量，但不要随便访问

# print(dog.__getname()) # 以__开头的方法为私有方法，只能从外面访问
print(dog.get_name())


# 获取对象信息

# isinstance(obj, type):判断对象是否是某种类型--->True/False
print(isinstance(dog, Myanimal))

# hasattr():判断对象是否拥有某个属性或方法
print(hasattr(dog, "__age__"))
print(hasattr(dog, 'get_name'))

# getattr():获取对象属性的默认值，没有对应属性则返回默认值，未设置默认值报错

print(getattr(dog, '__age__'))
print(getattr(dog, 'get_name'))

# setattr():设置某个属性的值

setattr(dog, '__name', 'didi')
print(getattr(dog, '__name'))
