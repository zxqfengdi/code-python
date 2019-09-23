# -*- coding:utf-8 -*-

"""
Name: 面向对象高级编程.py
Author: fengdi
Datetime: 8:23 2019/5/9 
Description:主要介绍面向对象编程的继承、多态特点及类方法、魔法方法等。

"""

# 面向对象的程序设计的特点：封装、继承、多态
# 继承：继承的类称为父类或基类，新生成的类称为子类
# 继承的特点：子类拥有父类的所有属性（类属性、实例属性）和方法；实例属性优先级高，同名的实例属性屏蔽类属性；可重新定义子类属性，重写方法；可为子类追加新的属性和方法


class Animal(object):
    """define a Animal class"""

    name = '动物'    # 类属性（可通过类名或实例访问）

    def __init__(self, age, behavior):    # 魔法方法：实例初始化时自动调用该方法
        self.age = age
        self.behavior = behavior

    def run(self):
        print('I am running!')


class Dog(Animal):   # 继承自Animal类，其实例拥有类属性和run方法
    """define a dog class, inherit from Animal class"""

    pass


class Cat(Animal):
    """define a cat class, inherit from Animal class"""

    def __init__(self, name):   # 重写父类中的初始化方法，子类name属性覆盖父类name属性
        self.name = name

    def run(self):
        print('I am a cat.I am running!')


print(Animal.__bases__, Dog.__bases__, Cat.__bases__)
print(Animal.name)   # 类属性可通过类名访问

dog = Dog(5, 'run')
print(dog.name, dog.age, dog.behavior)   # dog实例没有name属性，会向父类中查找name属性（类属性）；age behavior属性继承自父类
dog.run()  # 继承父类方法

cat = Cat('fengdi')   # 覆盖父类同名属性
print(cat.name)
cat.run()


# 多态：指对不同类型的对象进行相同的操作，表现出不同的行为

class Animal(object):
    """define a Animal class"""

    def __init__(self, name):
        self.name = name

    def greet(self):
        return 'Hello, I am %s.' % self.name


class Dog(Animal):  # 继承自Animal类，重写greet方法
    def greet(self):
        return '汪汪，I am %s.' % self.name


class Cat(Animal):  # 继承自Animal类，重写greet方法
    def greet(self):
        return '喵喵，I am %s.' % self.name


def hello(animal):
    return animal.greet()


dog = Dog('dog')   # Dog类实例化
dog_info = hello(dog)
print(dog_info)

cat = Cat('cat')
cat_info = hello(cat)
print(cat_info)

# 类方法和静态方法：类中定义的方法一般只能通过实例访问，类方法可被类直接访问
# 类方法：使用内置装饰器@classmethod方法放在定义的函数前面，表示这是个类方法；函数参数为cls；类方法可被类和实例访问


class Animal(object):
    """define a Animal class"""

    def __init__(self, name):
        self.name = name

    @classmethod   # 类方法
    def get_name(cls):
        return 'The name is %s.' % cls


dog = Animal('fengdi')
print(dog.get_name())
print(Animal.get_name())

# 静态方法：使用内置装饰器@staticmethod方法放在定义的函数前面，表示这是个静态方法；函数无参数；静态方法可被类和实例访问


class Animal(object):
    """define a Animal class"""
    name = 'fengdi'

    @staticmethod   # 静态方法
    def get_name():
        return 'The name is %s.' % Animal.name


dog = Animal()
print(dog.get_name())
print(Animal.get_name())

# 定制类和魔法方法：魔法方法（特殊方法，以__开头__结尾）可以提供特殊功能给
# __new__方法：类创建实例过程：类调用__new__(cls)类方法创建实例，再调用__init__(self)方法初始化实例。
# 可重载__new__方法来控制实例的创建过程


class Animal(object):
    """define a Animal class"""

    def __new__(cls, *args, **kwargs):  # 重载__new__方法，验证创建实例会调用__new__方法（主要时调用父类的__new__方法来创建当前类的实例）
        print('__new__ called.')
        return super().__new__(cls)

    def __init__(self, name, age):
        print('__init__ called.')
        self.name = name
        self.age = age

    def get_info(self):
        return 'The name is %s. The age is %d' % (self.name, self.age)


cat = Animal('yuxi', 5)
print(cat)
print(cat.get_info())


# __str__魔法方法：使用print打印对象时自动调用对象的__str__方法（默认只打印对象的内存地址）


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 返回对象的描述信息
    def __str__(self):
        # 返回一个字符串信息
        return "名字：%s   年龄：%d" % (self.name, self.age)


# person = Person('yuxi', 25)
person = Person(name='fengdi', age=24)
print(person)


# __del__魔法方法：对象释放时自动调用__del__方法（程序退出，程序中使用的变量全部销毁；当前对象的内存地址没有被使用，对象被销毁）


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("对象被释放！", self)


person = Person('fengdi', 24)
print(person)

del person   # 引用计数为1会调用__del__方法释放变量


# __slots__方法：定义类时可定义属性方法，创建类的实例后，可动态地给实例绑定任意属性
# __slots__特殊变量可以限制添加的属性，仅对当前类有效，对子类无效。若子类也定义__slots__变量，则子类可添加的属性为子类父类__slots__变量允许的并集。

class People(object):
    """define a People class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age


people = People('fengdi', 24)
print(people.name, people.age)
people.name = 'yuxi'   # 修改属性
print(people.name)
people.city = '武汉'  # 动态绑定新属性
print(people.city)


class People(object):
    """define a People class"""
    __slots__ = ('name', 'age')

    def __init__(self, name):
        self.name = name


people = People('fengdi')
print(people.name)
people.age = 24
print(people.age)
# people.city = '武汉'   动态添加__slots__不允许的属性会报错
# print(people.city)


# @property：内置装饰器@property实现将类中的方法转变为属性，同时生成一个@转变的方法名.setter装饰器，属性赋值时会调用该装饰器装饰的函数执行赋值操作。


class Score(object):
    """define a Score class"""

    def __init__(self, score):
        self.__score = score    # __score为私有属性

    def get_score(self):
        return self.__score

    def set_score(self, value):
        print('call func set_score:')
        self.__score = value


score = Score(80)
# print(score.__score)   # 私有属性只能在类内部访问
print(score.get_score())
score.set_score(95)   # 调用实例方法给属性重新赋值
print(score.get_score())


class Exam(object):
    """define a Exam class"""

    def __init__(self, score):
        self.__score = score    # __score为私有属性

    @property   # 将方法转变为属性
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        print('call func set_score:')
        self.__score = value


exam = Exam(65)
print(exam.score)
exam.score = 98
print(exam.score)


# 在子类调用父类方法
# 子类中使用类名调用父类方法


class Animal(object):
    def run(self):
        print("动物跑起来了")


class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def wang(self):
        self.run()   # 若本类中无要调用父类方法的同名方法可使用此方法调用（若本类中有，则会调用本类）
        Animal.run(self)   # 可使用父类名调用父类方法，传入参数
        super().run()     # 可使用super()函数调用父类方法（super(class, self)指定类class在类继承链self中的下一个类中的方法）
        print('汪汪汪！')


dog = Dog('yuxi')
dog.wang()


class Animal(object):
    """define a Animal class"""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print('Hello, I am %s.' % self.name)


class Cat(Animal):

    def get_name(self):
        super().get_name()
        print('哈哈哈哈！')


cat = Cat('fengdi')
cat.get_name()


# 多重继承：通过多重继承子类可获得多个父类的所有功能。方法解析顺序表（MRO：类继承顺序决定方法调用顺序）


class Animal(object):
    pass


class Cat(Animal):
    pass


print(Cat.mro())


class Base(object):
    def __init__(self):
        print('enter Base class')
        print('leave Base class')


class A(Base):
    def __init__(self):
        print('enter A class')
        super().__init__()
        print('leave A class ')


class B(Base):
    def __init__(self):
        print('enter B class')
        super().__init__()
        print('leave B class ')


class C(A, B):
    def __init__(self):
        print('enter C class')
        super().__init__()
        print('leave C class ')


print(C.mro())
c = C()
