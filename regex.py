#Tthis is a sequence  of characters that define a search patttern. 
#it is made possible by a module called (re module) wchich provides different functions used 
#to manipulate strings and work with regular expressions
#matching a specific word
import re
string = "Hello, World!!"
pattern = r"Hello"
match = re.search(pattern, string)
if match:
    print("pattern found!!")

else:
    print("pattern not match!!")


#Example 2
#Extracting data using groups
string = "My email is fredrickmureti612@gmail.com"
pattern = r"(\w+)@(\w+)\.com"
match = re.search(pattern, string)

if match:
    username = match.group(1)
    domain = match.group(2)
    print(f"username: {username}")
    print(f"domain: {domain}")

else:
    print("Email not found!!")

#matching a specific pattern with their groups
import re

text = "Fredrick Doe: 25 years old"
pattern = r'(\w+): (\d+) years old'
matches = re.findall(pattern, text)
print(matches)


#matching digit
import re

text = "I have 5 apples"
pattern = r'\d' 
matches = re.findall(pattern, text)
print(matches)

#Matching more than one digit

import re

text = "I have 5 apples and 13 mangoes"
pattern = r'\d+'
matches = re.findall(pattern, text)
print(matches)


#Replacing text using Reagex
text = "Hello, World"
pattern = r'World'
replacement = "Universe"
new_text = re.findall(pattern, replacement, text)
print(new_text)


#using [re.compile()]
#a re.compile() functions in python allows you to compile a regular expressions pattern 
#into a regex object which van be reused for various matching operations

#Example
import re
pattern = r'd+'
regex = re.compile(pattern)
string = "There are 123 apples and 456 oranges"
matches = regex.findall(string)
print(matches)    #output is ['123', '456']
#Explanation
#In the above example pattern +d is compiled using re.compile() into a regex object called regex
#The regex object is then used to find all occurences of one or more digits in the given text using findall() method

#[re.split()] function






