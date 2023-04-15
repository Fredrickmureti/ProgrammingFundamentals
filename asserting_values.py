#!/usr/bin/env python
#in python assertions are statements that checks if a given condition is 
#true and if not raises an AssertionError with a specified error message
#They are often used during testing and debugging to ensure that the code behaves as expected

#Example
#define a function that adds tow numbers
def add_numbers(x, y):
    return x + y

#test the function with valid inputs
assert add_numbers(5, 5) == 10
assert add_numbers(7,5) == 12

#test the funtion with invalid inputs

assert add_numbers('a', 'b') == ('ab')  #this should raise as AssertionError