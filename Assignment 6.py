#Iterables,Generators,Decorators,Context,Managers-----------------------------------------

#1) Iterables-----------------------------------
nums = [1, 2, 3]
it = iter(nums)
print(next(it), next(it), next(it))

# 2) Generators-----------------------------------
def countdown(n):
    while n:
        yield n
        n -= 1
for x in countdown(3):
    print(x)

# 3) Generator Expressions--------------------------------------------
squares = (x*x for x in range(5))
print(sum(squares))

# 4) Decorators--------------------------------------------------

from time import perf_counter
def timed(fn):
    def wrapper(*a, **k):
        t0 = perf_counter()
        r = fn(*a, **k)
        print(f"{fn._name_} took {perf_counter()-t0:.6f} s")
        return wrapper
    
    @timed
    def work():
        return sum(range(1_000_00))
    
# 5) Context Managers-----------------------------------------------

from contextlib import contextmanager    
@contextmanager
def opened(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()
with opened("file.txt", "w") as f:
    f.write("Hello, world!")


    
