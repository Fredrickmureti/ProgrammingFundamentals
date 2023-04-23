#The yiels statements suspends a function execution and sends a value back to the caller 
#but returns enough state to enable the caller resumes where it left

#simple program to demonstrate working of yield
#A genetaror that yields 1 for the first time, 2 for the second time and  3 for the third time

def simpleGenerator():
    yield 1
    yield 2
    yield 3



#driver code to checks above the generator function
for value in simpleGenerator():
    print(value)




#A python generator to generate suares from 1 to 100

def squareGenerator():
    i = 1
    while True:
        yield i * i
        i += 1

for num in squareGenerator:
    if num > 100 :
        break
    print(num)



    