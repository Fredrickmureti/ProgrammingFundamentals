#Python program to demonstrate
#creation of array
#importing array module for array creation

import array as arr
my_array = arr.array('i', [1, 2, 3])

#printing the original array
print("The new created array is:", end=" ")
for i in range(0, 3):
    print(my_array[i])
print()

#creating aerray with double type
double_array = arr.array('d', [2.5, 3.2, 3.3])
print("\nThe new created array is: ", end=" ")
for i in range(o, 3):
    print(double_array[i], end=" ")




#You can also use the len function
my_array = arr.array('i', [1, 2,  3])
#printing the original array
print("The new created array is : ", end=" ")
for i in len(my_array):
    print(my_array[i], end=" ")
print()

# Python program to demonstrate
# Adding Elements to a Array

# importing "array" for array creations
import array as arr

# array with int type
a = arr.array('i', [1, 2, 3])


print("Array before insertion : ", end=" ")
for i in range(0, 3):
	print(a[i], end=" ")
print()

# inserting array using
# insert() function
a.insert(1, 4)

print("Array after insertion : ", end=" ")
for i in (a):
	print(i, end=" ")
print()

# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

print("Array before insertion : ", end=" ")
for i in range(0, 3):
	print(b[i], end=" ")
print()

# adding an element using append()
b.append(4.4)

print("Array after insertion : ", end=" ")
for i in (b):
	print(i, end=" ")
print()



# Python program to demonstrate
# accessing of element from list

# importing array module
import array as arr

# array with int type
a = arr.array('i', [1, 2, 3, 4, 5, 6])

# accessing element of array
print("Access element is: ", a[0])

# accessing element of array
print("Access element is: ", a[3])

# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# accessing element of array
print("Access element is: ", b[1])

# accessing element of array
print("Access element is: ", b[2])





#Python program to demonstrate

# Adding Elements to a Array

# importing "array" for array creations

import array as arr

# array with int type

a = arr.array('i', [1, 2, 3,4,5])

#printing original array

print("The before array extend : ", end =" ")

for i in range (0, 5):

	print (a[i], end =" ")
	
print()

#creating an array with using extend method

a.extend([6,7,8,9,10])

#printing original array

print("\nThe array after extend :",end=" ")

for i in range(0,10):

	print(a[i],end=" ")
	
print()





#Python program to demonstrate

# Creation of Array

# importing "array" for array creations

import array as arr

#creating an array with integer type

a=arr.array('i',[1,2,3,4,5,6])

# printing original array

print("The Before extend array is :",end=" ")

for i in range(0,6):

	print(a[i],end=" ")
	
print()

# creating an array with using extend method

a.extend([7,8,9,10,11,12])

# printing original array

print("\nThe After extend array is :",end=" ")

for i in range(0,12):

	print(a[i],end=" ")

print()

#array with float type

b = arr.array('d', [2.1,2.2,2.3,2.4,2.5,2.6])

print("\nThe before extend array is :",end=" ")

for i in range(0,6):

print(b[i],end=" ")

print()

#extend function using pass the elements

b.extend([2.6,2.7,2.8,2.9])

print("\nThe after extend array is :",end=" ")

for i in range(0,9+1):

print(b[i],end=" ")

print()





