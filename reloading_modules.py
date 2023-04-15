#!/usr/bin/env python

#RELOADING MODULES IN PYTHON
#When a module is fi rst imported, any initialisation functions are run at that time. This may involve 
#creating data objects, or initiating connections. But, this is only done the fi rst time within a given session. 
#Importing the same module again won’t re-execute any of the initialisation code. If you want to have this 
#code re-run, you need to use the reload command. The format is ‘importlib.reload(modulename)’. Something to keep 
#in mind is that the dictionary from the previous import isn’t dumped, but only written over. This means that 
#any defi nitions that have changed between the import and the reload are updated correctly. But if you 
#delete a defi nition, the old one will stick around and still be accessible. There may be other side effects, so 
#lways use with caution, 

#suppose we have a module name my_module.py with the code below

def greet(name):
    print(f"Hello, {name}!")


#you then use this module in another file
import my_module
my_module.greet("Fredrick") #When you run this code the output will be Hello Fredrick!

#suppose we make changes to the code in my_module.py

def greet(name):
    print(f"Hi there, {name}!")

#if you run the file.py the output will still be the same
#Reloading the module using the statement importlib.reload(module name)

import importlib
import my_module

my_module.greet("Alice") #output the same value as the initial case

importlib.reload(my_module)
my_module.greet("Fredrick")




#Example 2
#suppose we have a module named my_math.py with the following code
def square(x):
    return x * x

#you the use this module in another file called file.py

import my_math
print(my_math.square(2)) # when you run the file file.py the output is 4

#suppose you make a change to the code in my_math.py

def square(x):
    return x ** 2
#if you run the file.py , the value will be 4 still because python as cached the old version of my_math module
#To apply the changes made to my_math.py you cab use the importlib.reload(module name) function like this

import importlib
import my_math
print(my_math(2))

#Reload the module my_math.py

importlib.reload(my_math)
print(my_math.square(2))





