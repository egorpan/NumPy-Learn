#function decorator
def decorator(func):
    def wrapper():
        print('decorator func before')
        func()
        print('decorator func after')
    return wrapper

@decorator
def greet():
    print('hello world!')

greet()

#method decorator

def method_decorator(func):
    def wrapper(self, *args,**kwargs):
        print('aaa')
        res = func(self, *args, **kwargs)
        print('bbb')
        return res
    return wrapper

class MyClass:
    @method_decorator
    def method(self):
        print('method class')

me = MyClass()
me.method()

#class decorators
def class_decorator(cls):
    cls.class_name = cls.__name__
    return cls

@class_decorator
class Person:
    pass

print(Person.class_name)

#staticmethod used to be called on the class itself

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

# Using the static method
res = MathOperations.add(5, 3)
print(res)

#class method is used on all instances of the class

class Egor:
    raise_amount = 20.00
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

me = Egor()
Egor.set_raise_amount(1.00)
print(me.raise_amount)

#property defines method as a property so method is accesibble as attribute

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.15*(self.radius)

myC = Circle(20)
print(myC.area)

#returning function from another function
def smth(f):
    def x(a):
        return f * a
    return x

a = smth(10)
print(a(100))

