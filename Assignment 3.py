# defining Function & Defaults ---------------------------------->
def greet(name: str = "World") -> str:
    return f"Hello, {name}!"

print(greet(), greet("Aditi"))

#args/kwargs --------------------------------------------------------->
def add_all(*nums):
    total = 0
    for n in nums:
        total += n
        return total
print(add_all(1,2,3,4))

def show(**info):
    for k, v in info.item():
        print(k, v)

show(name="Kahul", city="Pune")

#Ductings and Annotations ------------------------------------------>

def area_circle(r: float) -> float:
    """Returns area of a circle given radius r."""
    from math import pi
    return pi * r * r

print(area_circle.__doc__)

#Modules and Imports ----------------------------->
#file: utils.py
def double(x):
    return 2 * x
# file: main.py
# from utils import double  
# print(double(5))

