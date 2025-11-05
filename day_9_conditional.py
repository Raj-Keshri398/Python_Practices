
'''
Conditionals
By default, statements in Python script are executed sequentially from top to bottom.
 If the processing logic require so, the sequential flow of execution can be altered in two way:

Conditional execution: a block of one or more statements will be executed if a certain expression 
is true Repetitive execution: a block of one or more statements will be repetitively executed as 
long as a certain expression is true. In this section, we will cover if, else, elif statements. 
The comparison and logical operators we learned in previous sections will be useful here.

'''

# if Conditions
# In python and other programming languages the key word if is used to check if a condition is true 
# and to execute the block code. Remember the indentation after the colon.


a = 3
if a > 0:
    print('A is the positive number.')

# if else Condition

# If condition is true the first block will be executed, if not the else condition will run.

a = 3
if a < 0:
    print('A is a Negative Number')
else:
    print('A is a Positive Number')

# If Elif Else
# In our daily life, we make decisions on daily basis. We make decisions not by checking one or two
# conditions but multiple conditions. As similar to life, programming is also full of conditions. 
# We use elif when we have multiple conditions.

a = 0
if a > 0:
    print('A is a Positive Number')
elif a < 0:
    print('A is a Negative Number')
else:
    print('A is zero')

# Short Hand Code

a = 3
print('A is Positive Number') if a > 0 else print('A is negative Number') # first condition met, 'A is positive' will be printed

# Nested Conditon

a = 3

if a > 0:
    if a % 2 == 0:
        print('A is a Positive Even Number')
    else:
        print('A is a Positive Odd Number')
elif a == 0:
    print('A is zero')
else:
    print('A is Negative Number')


# If Condition and Logical Operators

a = -3
if a > 0 and a % 2 == 0:
    print('A is a Positive Even Integer')
elif a > 0 and a % 2 != 0:
    print('A is a Positive Odd Interger')
elif a == 0:
    print('A is Zero')
else:
    if a < 0 and a % 2 == 0:
        print('A is Negative Even Number')
    elif a < 0 and a % 2 != 0:
        print('A is a Negative Odd Integer')

# If and Or Logical Operators

user_name = 'Demo'
Access_level = 3
if user_name == 'Admin' or Access_level >= 4:
    print('Access Granted')
else:
    print('Access Denied')


# -------------------------------- Excercises Day 9 -----------------------------------------------

# Level 1

'''

1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough
to drive. If below 18 give feedback to wait for the missing amount of years. 

Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.

'''

age = int(input("Enter Your Age : "))

if age >= 18:
    print(f"Your age is {age}. You are old enough to learn to drive.")
else:
    year_left = 18 - age
    print(f"your age is {age}. You need {year_left} more year to learn to drive.")

'''
2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to 
print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text 
if my_age = your_age. 

Output:
    
'''

my_age = 25
your_age = int(input("Enter Your Age : "))
if my_age > your_age:
    diff = my_age - your_age
    if diff == 1:
        print(f"I am older than your by 1 year.")
    else:
        print(f"I am older than you {diff} year")
elif your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print("You are older than me by 1 year.")
    else:
        print(f"You are oldee than me by {diff} year")
else:
    print("We are of same age")

'''
3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
if a is less b return a is smaller than b, else a is equal to b. 

Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3

'''
a = int(input("Enter Number One : "))
b = int(input("Enter Number Two : "))
if a > b:
    print(f"A is {a} Greater than B is {b}.")
elif a < b:
    print(f"A is {a} less than B is {b}. ")
else:
    print(f"A is {a} Equal to B is {b}")



# -------------------------------------------------Exercises: Level 2 ---------------------------------

'''
1. Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F

'''

grade = int(input("Enter a Student Grade : "))
if grade >= 80 and grade <= 100:
    print("Grade A")
elif grade >= 70 and grade <= 79:
    print("Grade B")
elif grade >= 60 and grade <= 69:
    print("Grade C")
elif grade >= 50 and grade <= 59:
    print("Grade D")
elif grade >= 0 and grade <= 49:
    print("Grade F")
elif grade > 100:
    print("Big Number")
else:
    print("Negative Marks")

'''
2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or 
   November, the season is Autumn. December, January or February, the season is Winter. March, April or 
   May, the season is Spring June, July or August, the season is Summer

'''

month = input("Enter the Month : ").capitalize()
if month in ("September", "October", "November"):
    print("Season is Autumn")
elif month in ("December", "January", "February"):
    print("season is Winter")
elif month in ("March", "April", "May"):
    print("Season is Spring")
elif month in ("June", "July", "August"):
    print("Season is Summer")
else:
    print("Invalid Month")


'''
The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit 
exists print('That fruit already exist in the list')

'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit= input("Enter Fruit Name : ")


if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(fruits)



# --------------------------------- Exercises: Level 3 ---------------------------------------------

'''
Here we have a person dictionary. Feel free to modify it!
        person={
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

 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
 
 '''

person={
        'first_name': 'Rajeev',
        'last_name': 'Ranjan',
        'age': 250,
        'country': 'Finland',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills = person['skills']
    middle_Index = len(skills) // 2
    print(f"Middle Value of Person Skill is {skills[middle_Index]}")

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if 'Python' in person['skills']:
    print("Python does exist in skill section")
else:
    print("Python doesn't exist")

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person
# skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, 
# Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate
# results more conditions can be nested!

skills = person['skills']

if skills == ['JavaScript', 'React']:
    print("He is a Frontend Developer")
elif all(s in skills for s in ['Node', 'Python', 'MongoDB']) and not 'JavaScript' in skills:
    print("He is a Backend Developer")
elif all(s in skills for s in ['React', 'Node', 'MongoDB', 'Python', 'JavaScript']):
    print("He is a Full Stack Developer")
else:
    print("Unknown title")


# If the person is married and if he lives in Finland, print the information in the following format:
 
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")
