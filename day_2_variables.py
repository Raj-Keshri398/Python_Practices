# Day 2: 30 Days of Python Programming

# -----------------------------------------------
# Variable Declaration (Day 2: Variables)
# -----------------------------------------------

'''
# Storing personal information in variables
first_name = "Raj"          # string
last_name = "Keshri"        # string
full_name = "Raj Keshri"    # string
country = "India"           # string
age = 25                    # int
year = 2025                 # int
is_married = False          # bool
is_true = True              # bool
is_light_on = False         # bool

# Multiple variables declared on one line
a, b, c = 10, 20, 30        # int
'''

# -----------------------------------------------
# Checking the data type of each variable
# -----------------------------------------------
print(type(first_name))       # <class 'str'>
print(type(last_name))        # <class 'str'>
print(type(full_name))        # <class 'str'>
print(type(country))          # <class 'str'>
print(type(age))              # <class 'int'>
print(type(year))             # <class 'int'>
print(type(is_married))       # <class 'bool'>
print(type(is_true))          # <class 'bool'>
print(type(is_light_on))      # <class 'bool'>
print(type(a), type(b), type(c))  # <class 'int'> <class 'int'> <class 'int'>

# -----------------------------------------------
# String operations
# -----------------------------------------------
print(len(first_name))                     # Length of first_name
print(len(first_name) == len(last_name))  # Check if first_name and last_name have same length (True/False)

# -----------------------------------------------
# Arithmetic operations
# -----------------------------------------------
num_one = 5
num_two = 4

total = num_one + num_two
print("Total : ", total)

diff = num_one - num_two
print("Difference : ", diff)

product = num_two * num_one
print("Product : ", product)

division = num_one / num_two
print("Division : ", division)

remainder = num_two % num_one
print("Remainder : ", remainder)

exponent = num_one ** num_two
print("Exponent : ", exponent)

floor_division = num_one // num_two
print("Floor Division : ", floor_division)

# -----------------------------------------------
# Area and Circumference of a Circle
# -----------------------------------------------
import math

radius = 30
area = math.pi * radius ** 2
print("Area Of the Circle : ", area)

circumference = 2 * math.pi * radius
print("Circumference of the circle :", circumference)

# -----------------------------------------------
# Taking user input
# -----------------------------------------------
first_name = input("Your First Name : ")
last_name = input("Your Last Name : ")
age = int(input("Your Age : "))
country = input("Your Country : ")

print(first_name, last_name, age, country)

# -----------------------------------------------
# Printing all Python keywords
# -----------------------------------------------
import keyword

print("List of Python Keywords:")
print("--------------------------")

# Loop through the list of keywords and print each
for word in keyword.kwlist:
    print(word)

# Print total number of keywords
print("\nTotal number of keywords:", len(keyword.kwlist))
