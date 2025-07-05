# magic OOP class methods in python

class MyClass:
    # __init__ is called when instance of a class is created
    def __init__(self, n):
        self.n = n
        print(self.n)

    # __repr__ shows how class is represented
    def __repr__(self):
        return self

    # __add__ overloading class addition operator
    def __add__(self, other):
        return self.n + other

Egor = MyClass(20)
print(Egor+2)
