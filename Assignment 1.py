#here we will see Variables,Type and Printing 


#1.1 Variables Types And Printing 
name = "Aditi"
age = 22
height = 1.63
is_student = True
print(name, age, height , is_student)
print(f"{name} is {age} years old.")

# Numbers and Operators
num1 = 10
num2 = 5
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}.")

a,b = 10,2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# Strings
s = "Python Mastery"
print(s.lower())
print(s.upper())
print(s.title())
print(s.split())

print(s[0])
print(s[-1])
print(s[7:])

print("Master" in s)
print("-".join(["2025", "08", "29"]))

# Booleans & Comparisons
#comment out input()when running as a script without std in 
#user = input("Your name: ")
user = "Rakhumai"
print("hi", user)

#collection & Core Data Structures

#List
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[1:])

nums = [1, 2, 3]
nums.append(4)
nums.extend([5, 6])
nums.insert(0, 0)

print(nums)
print(nums[2:5])

