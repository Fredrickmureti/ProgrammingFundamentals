# Python program to
# demonstrate private members

# Creating a Base class

class Car:
    def __init__(self, make, model):
        self._make = make #private attributes
        self._model = model #private attributes


    #Defining getter functions
    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    #Defining setter method 
    def set_model(self, model):
        self._model = model



#Drive codes

car = Car("Toyota", "Camry")
print(car.get_make())
print(car.get_model())

#Modifying the private variable model using the setter method

car.set_model("Corolla")
print(car.get_model()) #output Corolla



#Example 2

class Base:
    def __init__(self):
        self._a = 2


#Derived class

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling the protected member of the base class", self._a)
        self._a = 3
        print("Calling the modified member outside class: ", self._a)


 
#Derive code

obj = Derived()
obj1 = Base()


print("Accessing the protected member of obj ", obj._a)
print("Acessing the protected member of obj1 ", obj1._a)

