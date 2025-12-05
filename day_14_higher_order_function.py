# ====================================   Higher Order Functions   =========================================
'''
In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

A function can take one or more functions as parameters
A function can be returned as a result of another function
A function can be modified
A function can be assigned to a variable
In this section, we will cover:

Handling functions as parameters
Returning functions as return value from another functions
Using Python closures and decorators

Example : ----------------------

def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

'''

# Function return Value

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)
    
def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    
result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3)) 

# ====================================   Python Closures   ===================================================
'''
Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure. Let us have a look 
at how closures work in Python. In Python, closure is created by nesting a function inside another encapsulating function and then 
returning the inner function. See the example below.
'''

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add
closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))

# ===================================  Python Decorators  ===================================================

'''
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its 
structure. Decorators are usually called before the definition of a function you want to decorate.
'''

def greeting():
    return 'welcome to python'

def upper_decorator(text):
    def wrapper():
        func = text()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

p = upper_decorator(greeting)
print(p())



#This decorator function is a higher order function that takes a function as a parameter

def upper_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@upper_decorator
def greeting():
    return 'welcome to python two'
print(greeting())

# These decorator functions are higher order functions that take functions as parameters


'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON


def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')