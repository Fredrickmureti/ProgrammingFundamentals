#!/usr/bin/env python

#IMPORTING MODULES
#python modules are reusable peaces of code that contains functions, classes or variables
#Ways of importing python modules

#1. importing the entire module using the import statement
#importing  tha math module

import math
print(math.sqrt(16))

#2 . importing a specific funtion or variable from a module
#Random module

from random import randint
print(randint(1, 10))

#3. importing the entire module with an alias
#Pandas module

import pandas as pd
data = pd.read_csv("data.csv")

#Example importing more than one module
# importing datetime module, os module, numpy module

import datetime
print(datetime.datetime.now())


from os import path
if path.exists("file.txt"):
    print("file exist")
else:
    print("file does  not exist!")


from numpy import array, sqrt
a = array([1, 2, 3])
print(sqrt(a))



#MORE EXAMPLES ON MODULES IMPORTING
#datetime module, datetime, numpy modules
import os
new_directory = "my_new_directory"
if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print(f"Directory {new_directory} created")
else:
    print(f"Directory {new_directory}, not created")




#datetime module
import datetime
now = datetime.datetime.now()
print(f"current time and date : {now}")


#numpy module

import numpy as np #importing numpy to acces the array functions
a = np.array([1, 2, 3]) #creating an array a 
b = np.array([4, 5, 6]) #creating an array b
c = a + b #adding the two arrays together
print(f"c= {c}")

