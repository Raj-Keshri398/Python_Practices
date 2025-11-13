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


# --------------------------------------Break and Continue - Part 2----------------------------------

# * 1. Short reminder: Break: We use break when we like to stop our loop before it is completed.

print("------------------Break---------------------")
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break


# * 2. Continue: We use continue when we like to skip some of the steps in the iteration of the loop.

print("-----------------Continue---------------------------")
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')


# ------------------------------------The Range Function -----------------------------------
'''
The range() function is used list of numbers. The range(start, end, step) takes three parameters: 
starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence 
needs at least 1 argument (end). Creating sequences using range.

'''

print("----------------------- print range in list --------------------------")
print("")
lst = list(range(11))
print(lst)

print("---------------------- print range in set --------------------")
print("")
st = set(range(1, 11)) # 2 arguments indicate start and end of the sequence, step set to default 1
print(st)

print("-------------------------- print range in list with argument ---------------------")
print("")
lst = list(range(0, 11, 2))
print("list with 2 steps : ", lst)

print("-------------------------- print range in list with argument ---------------------")
print("")
st = set(range(1, 11, 2))
print("Set with 2 steps : ", st)

# ---------------------------------Nested For Loop -------------------------------------
# We can write loops inside a loop. 

# nested loop with dictonary

print("")
print("---------------nested loop with disctonary ---------------------")
person_dict = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person_dict:
    if key == 'skills':
        for skill in person_dict['skills']:
            print(skill)

