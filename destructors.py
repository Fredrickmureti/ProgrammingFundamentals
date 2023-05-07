class MyClass:
    def __init__(self, name):
        self.name = name


    def __del__(self):
        print(f"Destructors called for {self.name}")


#Creating objects
obj1 = MyClass("Object1")
obj2 = MyClass("Object2")

#Deleting references to the objects
del obj1
del obj2


#Example 2
# Python program to illustrate destructor

class Employee:

	# Initializing
	def __init__(self):
		print('Employee created')

	# Calling destructor
	def __del__(self):
		print("Destructor called")

def Create_obj():
	print('Making Object...')
	obj = Employee()
	print('function end...')
	return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')

#Example 3
class A:
      def __init__(self, bb):
            self.b = bb

class B:
      def __init__(self):
            self.a = A(self)

      def __del__(self):
            print("Die")

def fun():
      b = B


fun()


#Recursion with destructors

class RecursiveFunction:
	def __init__(self, n):
		self.n = n
		print("Recursive function initialized with n =", n)

	def run(self, n=None):
		if n is None:
			n = self.n
		if n <= 0:
			return
		print("Running recursive function with n =", n)
		self.run(n-1)

	def __del__(self):
		print("Recursive function object destroyed")

# Create an object of the class
objec = RecursiveFunction(5)

# Call the recursive function
objec.run()

# Destroy the object
del objec






      



