#OOP Object-Oriented Programming --------------------------------------------------

#Classes and Instances ------------------------------------

from unicodedata import name


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hi, i am {self.name}"

p = Person("Xu Kai",29)
print(p.greet())

#Inheritance and super()---------------------------------------

class Employee(Person):
    def __init__(self, name: str, age: int, role: str):
        super().__init__(name, age)
        self.role = role
emp = Employee("v", 29, "Singer Good Boy")
print(emp.greet(), emp.role)

#Magic Methods & _repr_ ---------------------------------------

class Vector:
 def __init__(self, x, y):
  self.x, self.y = x, y
 def __add__(self, other):
  return Vector(self.x + other.x, self.y + other.y)
 def __repr__(self):
  return f"Vector({self.x}, {self.y})"


print(Vector(1, 2) + Vector(3, 4))

#Dataclasses -----------------------------------------------------------

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
print(Point(2, 3))

#Encapsulation, Properties -------------------------------------------------

class Bank:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

b = Bank(); b.deposit(100);print(b.balance)