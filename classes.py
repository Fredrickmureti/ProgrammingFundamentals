#!/usr/bin/env python

#creating class examples
class Person:
    def __init__(self, name, age):
        self.name =  name
        self.age = age

    def say_hello(self):
        print("hello," self.name, "I'm," self.age "years old")


#creating objects
person1 = Person("Fredrick", 23)
person2 = Person("John", 22)

print(person1.say_hello)
print(person2.say_hello)


#Example 2
#Bank Account Class(this is an example of a class that simulates bank account)

class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, ammount):
        self.balance += ammount

    def withdraw(self, ammount):
        if ammount> self.balance:
            print("You have insufficient funds!")
        else:
            self.balance -= ammount


#creating objects

account1 = BankAccount("Fredrick", 1234, 1000)
account2 = BankAccount("Chris", 2345)

account1.deposit(500)
account1.withdraw(200)
print(account1.balance)

account2.deposit(1000)
account2.withdraw(1500)
print(account2.balance)



#cuboid CLASS
#This is an example of a class tha represent a cuboid. it has attributes length, width and height of the 
# rectangle as well as methods for calculating the area ,perimeter and volume

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.height
    

    def perimeter(self):
        return 2 * (self.width + self.length)
    

#creating objects
rect1 = Rectangle(10, 20)
rect2 = Rectangle(5, 5)

print(rect1.area)
print(rect1.perimeter)

print(rect2.area)
print(rect2.perimeter)




#CAR  CLASS
#This is an example of a class that represent a car, it has attributes for the car 
# model, year, and the color of the car as well as the methods for starting and stopping the car


class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine_started = False
    def start_engine(self):
        self.engine_started = True
    def stop_engine(self):
        self.engine_started = False


#creating objects


car1 = Car("Toyota", "Camry", 2021, "Red")
car2 = Car("Ford", "Mustang", 2022, "Blue") 

car1.start_engine
print(car1.engine_started)

car2.stop_engine
print(car2.engine_started)





#CLASS INHERITANCE IN PYTHON
#This is a way to create a new class by deriving it from an existing class
#This class will have all the properties and methods of the existing class 
# but can also add its own methods and properties or override the ones inherited
#from parent class

# you can add new methods to the child class, or overrride methods in the parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "generic animal sound"
    
class Dog(Animal):
    def make_sound(self):
        return "woof!"
    

#creating objects

dog = Dog("Fido")
print(dog.name)
print(dog.make_sound())



#Adding new methods to the child class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "generic animal sound"
    
class Dog(Animal):
    def make_sound(self):
        return "woof!"
    
def wag_tail(self):
    return "tail wagging"


dog = Dog("Fido")
print(dog.name)
print(dog.make_sound())
print(dog.wag_tail())



#Multiple inheritance in python

class Person:
    def __init__(self, name):
        self.name = name
    

    def greet(self):
        print("Hello, my name is ", self.name)


class Student:
    def __init__(self, student_id,):
        self.student_id = student_id

    def study(self):
        print("I am studying with ID", self.student_id)


class InternationalStudent(Person, Student):
    def __init__(self, name, student_id, country):
        Person.__init__(self, name)
        Student.__init__(self, student_id)
        self.country = country


    def display_info(self):
        self.greet()
        self.study()
        print("I am from", self.country)


#creating object

student = InternationalStudent("John", 1234, "Canada")
student.display_info()










    


