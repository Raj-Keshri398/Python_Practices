def generate_full_name(firstname,  lastname):
    return firstname + ' ' + lastname


def sum_two_nums(a, b):
    return a + b

person = {
    'first_name' : 'raj',
    'last_name'  : 'Keshri',
    'age'        : 26,
    'country'    : 'India',
    'is_married' : False,
    'skills'     : ['python', 'html', 'css', 'javascript', 'reactjs', 'bootstrap', 'mysql', 'sql', 'php'],
    'address'    : {
        'pincode' : 800001,
        'street'  : 'boring road'
    }
}

def weight_of_object (mass, gravity):
    weight = str(mass * gravity) + ' N' # the value has to be changed to a string first
    return weight


gravity = 4

# ------------------------------------  Sys Module -----------------------------------------------
'''
The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. 
Function sys.argv returns a list of command line arguments passed to a Python script. The item at index 0 in this list 
is always the name of the script, at index 1 is the argument passed from the command line.

Example of a script.py file:


Example 1.....

import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print("Sum =", num1 + num2)

Run karte time terminal me: python add.py 10 20

Example 2.........

import sys

age = 15

if age < 18:
    print("Not allowed!")
    sys.exit()

print("Welcome inside!")


print("Version =", sys.version) `           # check the vesrion
print("Path =", sys.path)                   # check the path of the python
print("Maxsize=", sys.maxsize)              # check the size
sys.stdout.write("Hello World\n")           # write the string on terminal

'''

# -----------------------  Statistics Module  ------------------------------

'''
The statistics module provides functions for mathematical statistics of numeric data. The popular statistical functions which 
are defined in this module: mean, median, mode, stdev etc.

Simple meaning ---------------------

Python ka statistics module numeric data par basic statistical calculation karne ke liye use hota hai—matlab maths me jo average, 
middle value, common value, variation wagaira nikalte hain, un sabka ready-made function mil jata hai.

Example -------------------------

    * mean → average
    * median → calculate middle number
    * mode → sabse zyada baar aane wala number
    * stdev → standard deviation (numbers kitne spread hain)

1. mean -> average

import statistics
data = [10, 20, 30, 40]
print(statistics.mean(data))

2. median -> middle value

import statistics
data = [4, 1, 7, 2]   # sorted = [1,2,4,7]
print(statistics.median(data))

3. mode -> most repeated value

import statistics
data = [2, 2, 3, 4, 2, 5]
print(statistics.mode(data))

4. stdev → Standard Deviation

    * Agar values ek dusre ke close hon → stdev small
    * Agar values far-far hon → stdev large

import statistics
data = [2, 4, 4, 4, 5, 5, 7, 9]
print(statistics.stdev(data))


from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
'''

# -----------------------------------   Math Module  ------------------------------------------------------
'''
Module containing many mathematical operations and constants.

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base



It is also possible to import multiple functions at once

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2


If we want to import all the function in math module we can use * .

from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2

When we import we can also rename the name of the function.

from math import pi as  PI
print(PI) # 3.141592653589793

'''

# ----------------------------------------------  String Module  --------------------------------------------
'''

A string module is a useful module for many purposes. The example below shows some use of the string module.

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

'''

# ---------------------------------------------- Random Module ---------------------------------------------

'''
The random module has lots of functions but in this section we will only use random and randint.

from random import random, randint
print(random())             # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20))       # it returns a random integer number between [5, 20] inclusive

'''


# =============================================  Exercises: Level 1  =================================================

# 1. Write a function which generates a six digit/character random_user_id.


print("---------Generate 6-digit random number with string-----------")
import string
import random
def random_user_id():
    # All uppercase + lowercase letters + digits
    characters = string.ascii_letters + string.digits

    user_id = ' '.join(random.choice(characters) for _ in range(6))
    return user_id
  
print(random_user_id()); #'1ee33d'

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two 
# inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed 
# to be generated.


print("--------- Generate digits with strings ---------")
def user_id_gen_by_user():
    length = int(input("Enter a Number of a character of each ID : "))
    count = int(input("Enter how many IDs to generate : "))

    characters = string.ascii_letters + string.digits
    
    # Number of Generate IDs
    for _ in range(count):
        user_id = ' '.join(random.choice(characters) for _ in range(length))
        print(user_id)

user_id_gen_by_user() # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
user_id_gen_by_user() # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr


# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

print("---------- Generate 6-digit rgb color and append on list -----------")
import random
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return f"rgb({r},{g},{b})"
print(rgb_color_gen()) # rgb(125,244,255) - the output should be in this form

# ===============================================  Exercises: Level 2  ==============================================

# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written
# after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for 
# output examples).

print("------------ Generate 6-digit hexadecimal string ------------")
import random
import string

def list_of_hexa_colors(n):
    hexa_char = string.hexdigits.lower()[:16] # generate hexadecimal string with digit
    colors = [] # list

    for _ in range(n):
        color = '#' + ' '.join(random.choice(hexa_char) for _ in range(6))
        colors.append(color)
    return colors
print(list_of_hexa_colors(3))

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

import random

def list_of_rgb_colors(n):
    rgb_colors = []

    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        rgb_color = f"rgb({r},{g},{b})"
        rgb_colors.append(rgb_color)

    return rgb_colors

print(list_of_rgb_colors(3))

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.

import random
import string
def generate_colors(chars, n):
    colors = []

    if chars == 'hexa':
        for _ in range(n):
            hexa_char = string.hexdigits.lower()[:16]
            color = '#' + ' '.join(random.choice(hexa_char) for _ in range(6))
            colors.append(color)
        print(colors)
    elif chars == 'rgb':
        for _ in range(n):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            rgb_color = f"rgb({r},{g},{b})"
            colors.append(rgb_color)
        print(colors)


generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
generate_colors('hexa', 1) # ['#b334ef']
generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
generate_colors('rgb', 1)  # ['rgb(33,79, 176)']


# =============================================  Exercises: Level 3 =================================================

# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

import random

def shuffle_list(lst):
    new_list = lst[:]
    random.shuffle(new_list)
    return new_list
print(shuffle_list([2, 3, 4, 5, 6]))

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

import random

def seven_random_number():
    numbers = set()

    while len(numbers) < 7:
        random_num = random.randint(0, 9)
        numbers.add(random_num)
    return numbers

print(seven_random_number())





