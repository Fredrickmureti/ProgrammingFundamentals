#!/usr/bin/env python
 #creating a list
my_list = [1, 2, 3, 'a', 'b', 'c']

#accessing elements (we access the elements by referreing them to their indexes)
print(my_list[0]) 
print(my_list[3])

#adding elements (We use the apppend()method )
my_list.append('d')
print(my_list)

#Removing the elements (we use the remove()method)
my_list.remove(2)
print("my list=", my_list)

#sorting elemets(we use the sort() method which sorts the elements in ascending order by default)
my_list1 = [8, 7, 6, 5, 4, 4, 3]
my_list1.sort()
print(my_list1)

#reversing the elements(we use the reverse()method which reverses the order of the elements)
my_list1.reverse
my_list.reverse
print(my_list)
print(my_list1)

#copying elements (we use the copy()method)
new_list1 = my_list1.copy()
new_list = my_list.copy()
print(new_list)
print(new_list1)

#lenth of a list(which uses len()to get the number of elements in a list

print(len(my_list1))
print(len(my_list))
print(len(new_list1))
print(len(new_list))


#DICTIONARIES
#creating dictionary
my_dict = {'name': 'John', 'age': 23, 'city': 'Nairobi'}

#accesing values

print(my_dict["name"])
print(my_dict['age'])

#adding or updating values

my_dict['email'] = 'fredrickmureti612@gmail.com'
print(my_dict)

my_dict['age'] = 25
print(my_dict)
#removing values(using the del keyword)

del my_dict['name']
print(my_dict)

#using the pop()method
age = my_dict.pop('age')
print(my_dict)


#checking for keys and values (using the 'in' and 'not' keyword whoch returns a  bool)

if 'name' in my_dict:
    print("name is present in the dictionary.")
else:
    print("name not present")

if 'city' not in my_dict:
    print("city not in my dictionary")
else:
    print("city present")

#copying a dictionary

new_dict = my_dict.copy()
print(new_dict)


#getting all keys or values
keys = my_dict.keys()
print(keys)

values = my_dict.values()
print(values)


#TUPLES

#creating a tuple
my_tuple = (1, 2, 3, 4, 5)

#accesseing values(by referring the elements by their indexes)

print(my_tuple[0])
print(my_tuple[4])

#Tuples are immutable

my_tuple[0] = 10 #This will display TypeError: 'tuple' object does not support item assignment

#concenating Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
new_tuple = tuple1 + tuple2
print(new_tuple)

#multiplying tuples
my_tuple1 = ('a', 'b')
new_tuple1 = my_tuple1 * 3
print(new_tuple1)

#Tuple unpacking
my_tuple2 = ('Fredrick', 'Mureti', 24)
first_name, last_name, age = my_tuple2
print(first_name)
print(last_name)
print(age)#checking if element is in a tuple(we use the 'in' keyword)

if 'Fredrick' in my_tuple2:
    print("name Fredrick present in the dictionary")
else:
    print("name not present")

