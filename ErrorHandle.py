#!/usr/bin/env python

#in python you can use the 'try' and 'except' statements to handle errors and exceptions that might occur
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

#code to handle errors arising

def calculate_average(numbers):
    try:
        j
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except ZeroDivisionError:
        return 0.0
    

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print("The reciprocal of {} is {}".format(x, y))

except ValueError:
    print("You didn't  enter a valid integer.")
except ZeroDivisionError:
    print("you cant divide by zero!")
except:
    print("Something went wrong!")
