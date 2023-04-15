#!/usr/bin/env python
while True:
    try:
        size = int(input("Enter the number of integers you want in the list "))
        break
    except ValueError:
        print("Invalid input: please enter an integer! ")

my_list = []

for i in range(size):
    while True:
        try:
            value = int(input(f"enter integer {i+1}"))
            break
        except ValueError:
            print("Invalid input: Please enter an integer ")
    my_list.append(value)

print("The list is: ", my_list)