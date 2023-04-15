#!/usr/bin/env python
#filtering in python


#This is the process of selecting a subset of elements from a collection based on a condition
#we use the built in function filter() to flter elements from a list, tuple or any other iterable object
#Example

#using the filter function to filter even numbers from a list of numbers
numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]

def is_even(number):
    return number % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers)



#Example 2
#This examples uses lambda() function to filter names from a list of strings based on a certain condition

names = ["Alice", "Fredrick", "David", "Charlie", "Bob", "Eve"]
short_names  = list(filter(lambda name: len(name) < 5, names))  #lamda takes name as argument and return True
print(short_names)


#we can also use list comtehension to arrive at the same results 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)


#Using functions to filter data set by implementing conditional statement that determine which element should 
#be included on the filtered set

#Example 1
#FILTERING A LIST OF NUMBERS GREATER THAN A CERTAIN  VALUE

def filter_greater_than(numbers, value):
    filtered_numbers = []
    for num in numbers:
        if num > value:
            filtered_numbers.append(num)
    return filtered_numbers


numbers = [2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = filter_greater_than(numbers, 10)
print(filtered_numbers)




#Example 2
#FILTERING A LIST OF STRINGS CONTAINING A CERTAIN SUBSTRING

def filter_substrings(strings, substring):
    filtered_strings = []
    for string in strings:
        if substring == string:
            filtered_strings.append(string)
    return filtered_strings


strings = ["banana", "mango", "cherry", "apple", "orange"]
filtered_strings = filter_substrings(strings, "an")
print(filtered_strings)




#Example 3
#FILTERING A LIST OF DICTIONARIES BASED ON A CERTAIN KEY VALUE PAIR

def filter_dict_list(dict_list, key, value):
    filtered_dict_list = []
    for item in dict_list:
        if item.get(key) == value:
            filtered_dict_list.append(item)
    return filtered_dict_list

dict_list = [{"name": "Alice", "age": 25}, {"name": "Fredrick", "age": 24}, {"name": "Bob", "age": 25}]
filtered_dict_list = filter_dict_list(dict_list, "age":25)
print(filtered_dict_list)


#Example 4
#FILTERING A LIST OF TUPLES BASED ON A CERTAIN CONDITION

def filter_tuple_list(tuple_list, condition_funct):
    filtered_tuple_list = []
    for item in tuple_list:
        if condition_funct(item):
            filtered_tuple_list.append(item)
    return filtered_tuple_list

tuple_list = [(1, 2), (3, 4), (5, 6)]
filtered_tuple_list = filter_tuple_list(tuple_list, lambda x: sum(x) > 5)
print(filtered_tuple_list)


#Example 4
#FILTERING PANDA DATAFRAME BASED ON A CERTAIN CONDITION

import pandas as pd
data = {"name": ["Alice", "Bob", "Charlie"], "age": [25, 30, 25]}
df = pd.DataFrame(data)
filtered_df = df[df[('age')] == 25]
print(filtered_df)





