#!/usr/bin/env python

#REDUCTION IN PYTHON
#in python reduction is an operation that takes an iterable  and returns a single value by successively applying
#a function to each element in the iterable, 
#The function can  be any function that takes two argument and returns a single value such as addition,
#multiplication, maximum or minimum

#Python provides the built in function ('reduce()' from the 'functools' module) that is functools.reduce()

#EXAMPLEs on how to use the reduce function
#exemple1

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda(x, y: x+y, numbers))
print(sum_of_numbers) #output the total of numbers in the number_object

#example 2 Multiplying a list of numbers

from functools import reduce
numbers = [2, 3, 5, 6]
multiplied_numbers = reduce(lambda(x,y:x * y, numbers))
print(multiplied_numbers) #outputs the multiplication of the numbers in the list

#Example2 Finding minimum value

from functools import reduce
numbers = [2, 3, 5, 6, 7]
minimum_value = reduce(lambda(x,y: x if x<y else y, numbers))
print(minimum_value) #output the minimum value which is 2

#Example 3 Finding Maximum value

from functools import reduce
numbers = [1, 2, 5, 6, 7]
max_value = reduce(lambda(x,y: x if x>y else y, numbers))
print(max_value) #outputs the maximum value which is 7

#Example 4 concatenating a list of strings into a single string

from functools import reduce
my_list = ["hello, world", "this", "is", "reduction"]
concatenated_string = reduce(lambda(x,y: x+y, my_list))
print(concatenated_string) #outputs (hello, world this is reduction)

#Example 5 Flattening a list of lists
from functools import reduce
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = reduce(lambda(x,y:x+y, my_list))
print(flattened_list) #outputs 1, 2, 3, 4, 5, 6, 7, 8, 9


#Example 6 Counting the number of occurence of a particular element on a list
from functools import reduce
number_list = [1, 2, 2, 2, 2, 3, 4]
count = 0
count = reduce(lambda(x,y:x +(y==2), my_list))
print(count)
