#!/usr/bin/env python
#ENUMERATING
#This is a built in function that allows you to iterate over a sequence(such as a list or a tuple)
#and keep track of the index of the current item being processed
#We use the enumerate() function
#Examples

my_list = ['red', 'green', 'blue']
for i, color in enumerate(my_list):
    print(f"{i+1} :{colour}")


#or

my_list = ['red', 'green', 'blue']
for i, color in enumerate(my_list, start=1):
    print(f"{i} : {color}")  
