#for loops (used to iterate over sequence of values such as list, tuple or a string)
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(numbers)


#using the len() to count over the indices of the elements

for i in range(len(numbers)):
    print(numbers)


for i in range(len(numbers)):
    numbers[i] *=2
print(numbers)   #This code will double the elements of numbers list and print the modified list

#others are if else statements,  nested if else statements, switch statements 