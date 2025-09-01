
#Control Flow (if/elif/else)-----------------------------------------------

score = 78
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
print(grade)

#loops in python--------------------------------------------------------

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

n = 5
while n > 0:
    print(n) 
    n -= 1 

# Tuples (immutable)----------------------------------------------
t = ("x", 1, True)
print(t[0], len(t))

#Sets (unique, unordered)-----------------------------------------------
s = {1, 2, 2, 3}
s.add(4)
print(s, 2 in s)

# Dictionaries (key-value pairs)---------------------------------------
d = {"name": "Alice", "age": 30}
print(d["name"], d.get("age"))

student = {"name": "Radha", "age": 10}
student["city"] = "Mumbai"
for k, v in student.items():
    print(k, v)

#Comprehensions--------------------------------------------------------
squares = [x*x for x in range(6)]
odd_map = {x: "odd" for x in range(10) if x % 2}
print(squares, odd_map)
