
from typing import override


class Parent1:
    def greet(self):
        print("from Parent1")

class Parent2:
    def greet(self):
        print("from Parent2")

class Child(Parent1, Parent2):
    @override
    def greet(self):
        Parent2.greet(self)


c = Child()
print(Child.mro())
c.greet()

