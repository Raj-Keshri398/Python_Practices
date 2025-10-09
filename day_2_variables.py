# Day 2: 30 days  of python programming

'''
first_name = "Raj"          #string
last_name = "Keshri"        #string
full_name = "Raj Keshri"    #string
country = "India"           #string
age = 25                    #int
year = 2025                 #int
is_married = False          #bool
is_true = True              #bool
is_light_on = False         #bool
a, b, c = 10, 20 ,30        #int
'''

'''
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a), type(b), type(c))
'''

'''
print(len(first_name))
print(len(first_name) == len(last_name))

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
print("Floor Division : ",floor_division)
'''

'''
import math
radius = 30
area = math.pi * radius ** 2
print("Area Of the Circle : ", area)

circumference = 2 * math.pi * radius
print("Circumference of the circle :", circumference)

first_name = input("Your First Name : ")
last_name = input("Your Last Name : ")
age = int(input("Your Age : "))
country = input("Your Country : ")
print(first_name, last_name, age, country)
'''

import keyword

# Print list of Python keywords
print("List of Python Keywords:")
print("--------------------------")

for word in keyword.kwlist:
    print(word)

# Print total number of keywords
print("\nTotal number of keywords:", len(keyword.kwlist))




