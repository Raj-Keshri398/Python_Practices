'''
Loops

Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle 
repetitive task programming languages use loops. Python programming language also provides the following 
types of two loops:

 * while loop
 * for loop


While Loop

We use the reserved word while to make a while loop. It is used to execute a block of statements 
repeatedly until a given condition is satisfied. When the condition becomes false, the lines of code 
after the loop will be continued to be executed.

  # syntax
while condition:
    code goes here
'''

# Example
print("----------------- Syntax ---------------------")
count = 0
while count < 5:
    print(count)
    count = count + 1

print("----------------- Comdition ---------------------")
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)



# Break and Continue - Part 1

# * 1. Break: We use break when we like to get out of or stop the loop

print("----------------- Break ---------------------")
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# * 2. Continue: With the continue statement we can skip the current iteration, and continue with the next:

print("----------------- Continue ---------------------")
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

'''
For Loop
A for keyword is used to make a for loop, similar with other programming languages, but with some syntax
differences. Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a 
set, or a string).

'''

# For Loop with List

print("--------------------For Loop with list -------------------")
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

print("-----------------------Loop with String------------------")

language = 'Python'
for letter in language:
    print(letter)

print("---------------------")
for i in range(len(language)):
    print(language[i])


# For loop with tuple

print("-----------------For loop with tuple --------------------")
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# For loop with dictionary Looping through a dictionary gives you the key of the dictionary.

print("-------------------Dictonary ------------------------------")
person = {
    'first_name' : 'shivam',
    'last_name'  : 'keshri',
    'age'        : 26,
    'contury'    : 'india',
    'is_married' : False,
    'skills'     : ['Javascript', 'Python', 'Css', 'Html', 'Bootstrap', 'Mysql'],
    'address'    : {
        'street_address' : 'malsami',
        'pincode'        : '800009'
    }
}


for key in person:
    print(key)

print("-----------------key and Value -----------------")

for key, value in person.items():
    print(key, value)

# loop with set

print("------------------- loop with sets -----------------------")

companies = {'google', 'facebook', 'deloitte', 'hcl', 'tcs'}
for company in companies:
    print(company)

