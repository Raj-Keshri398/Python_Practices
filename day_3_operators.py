# day 3
'''
base = int(input("Enter Base : "))
height = int(input("Enter Height : "))
area_of_triangle = 1/2 * (base * height)
print("Area of Triangle is : ", area_of_triangle)


a = int(input("Enter Side a : "))
b = int(input("Enter side b : "))
c = int(input("Enter side c : "))
perimeter_of_triangle = a + b + c
print("Perimeter of Triangle : ", perimeter_of_triangle)


length = int(input("Enter length : "))
width = int(input("Enter width : "))
area_of_rect = length * width
print("Area of rectangle : ", area_of_rect)
perimeter_of_rect = 2 * (length + width)
print("Perimeter of Rectangle : ", perimeter_of_rect)


import math

radius = int(input("Enter Radius of circle : "))
area_of_circle = math.pi * radius ** 2
print("Area of circle : ", area_of_circle)
circumference_of_circle = 2 * math.pi * radius
print("Circumference of circle : ", circumference_of_circle)

'''

'''
# rule y = 2x - 2

m1 = 2 #slope
c = -2 #y_intercept


# Calculate x-intercept (when y = 0)
# 0 = m*x + c  => x = -c/m
x_intercept = -c / m1

# Display results
print("Slope (m):", m1)
print("Y-intercept (c):", c)
print("X-intercept:", x_intercept)

import math
x1, y1 = 2, 2
x2, y2 = 6, 10

#calculate slope
m2 = (y2 - y1) / (x2 - x1)

#calculate Euclidean distance
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Slope (m) : ", m2)
print("Euclidean Distance (d) : ", d)

compare = m1 == m2
print("comapre the slope 8 is (", m1, ") and slope 9 is (", m2, "): ", compare)



# Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at what x value y is going to be 0.

for x in range(-3, 1):
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}")


'''

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
'''print(len("python") != len("dragon"))'''


# Use and operator to check if 'on' is found in both 'python' and 'dragon'
'''if "on" in "python" and "dragon":
    print("True")
else:
    print("False")'''

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
'''sentence = "I hope this course is not full of jargon."
if "jargon" in sentence:
    print(True)
else:
    print(False)'''

# There is no 'on' in both dragon and python
word1 = "python"
word2 = "dragon"
#print('on' not in word1 and 'on' not in word2)

# Find the length of the text python and convert the value to float and convert it to string

python_len_float = float(len("python"))
#print("Python word length convert into float : ", type(python_len_float))

float_to_string = str(python_len_float)
#print("Float convert into string : ", type(float_to_string))


# Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python.

num = 8

# Check if number is even
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")



# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.\

result = (7 // 3) == int(2.7)
print(result)

# Check if type of '10' is equal to type of 10

result_string = type('10') ==  type(10)
print(result_string)

# Check if int('9.8') is equal to 10

nums = int(float('9.8')) == 10
print(nums)


'''
Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
'''

hour = int(input("Enter Hours : "))
rate = int(input("Enter rate per hour : "))
weekly_earning = hour * rate
print("Your Weekly Earning is", weekly_earning)

'''
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
'''


year = int(input("Enter number of year you have lived : "))
year_in_second = year * 365 * 24 * 60 * 60
print("You have lived for ", year_in_second)


'''
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''

n = int(input("Enter a Number : "))
for i in range(1, n):
    print(i, 1, i, i**2, i**3)



# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False