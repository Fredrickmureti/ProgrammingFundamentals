#!/usr/bin/env python

#FUNCTIONS IN PYTHON

#simple functions that add two numbers

def add_number(x, y):
    results = x+y
    return results

#calling the function

sum = add_number(3,4)
print(sum)

#FUNCTIONS WITH DEFAULT VALUES
def greet(name, greeting="hello"):
    print(greeting, name)
# calling the function
greet("Fredrick")
greet("Mary", "Hello")

#FUNCTIONING RETURNING MULTIPLE VALUES USING TUPLES

def square_and_cube(num):
    return num**2, num**3

#calling the function through tuple unpacking 

square, cube = square_and_cube(3)
print(square)
print(cube)

#function accepting arbitrary number of arguments using args and **kwargs

#args
#used to pass a variable number of positional arguments

def multiply_numbers(*args):
    product = 1
    for arg in args:
        product = product * arg
    return product

#calling the function

result = multiply_numbers(2, 3, 4)
print(result)

# **kwargs
#used to pass a variable number of keyword arguments to a function

def print_person_info(**kwargs):
    for key, value in kwargs.item():
        print(f"{key}: {value}")

#calling the function
print_person_info(name="Fredrick", age=30, city="New York")


#*args and **kwargs at the same time
def my_funtion(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} :{value}")

my_funtion(1, 2, 3, name="Fredrick", age=30, city="New York")

