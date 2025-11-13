'''
Defining a Function

A function is a reusable block of code or programming statements designed to perform a certain task. 
To define or declare a function, Python provides the def keyword. The following is the syntax for defining
a function. The function block of code is executed only if the function is called or invoked.
'''

# -----------------------------------------------------------------------------------------------------
'''
Declaring and Calling a Function

When we make a function, we call it declaring a function. When we start using the it, we call it calling 
or invoking a function. Function can be declared with or without parameters.
'''

# syntax

# Declaring a function
def function_name():
    print('code')

# Calling a function
function_name()


# ----------------------------------------- Function without parameter -----------------------------

print("--------------------function without returning statement ------------------")
def generate_full_name():
    first_name = 'Shivani'
    last_name = 'Kumari'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name() # calling the function

def add_two_num():
    one = 5
    two = 9
    sum = one + two
    print(sum)

add_two_num() # calling the function


'''
Function Returning a Value - Part 1


Function can also return values, if a function does not have a return statement, the value of the 
function is None. Let us rewrite the above functions using return. From now on, we get a value from
a function when we call the function and print it.

'''
print("-----------------Function with return statement ------------------------")
def generate_full_name():
    first_name = 'Shivani'
    last_name = 'Kumari'
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name()) # calling the function

def add_two_num():
    one = 5
    two = 9
    sum = one + two
    return sum

print(add_two_num())# calling the function


print("-------------- explainations ----------------------------")
def without_return():
    print("Hello")

def with_return():
    return "Hello"

x = without_return()  # prints Hello but returns None
y = with_return()     # returns "Hello" which can be stored, printed and reuse the calue of another inside the another function

print(x)  # Output: None
print(y)  # Output: Hello


'''
Function with Parameters

In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set)
as a parameter.

'''

# Single Parameter: If our function takes a parameter we should call our function with an argument

print("------------------Single Parameter Function -------------------")

def greetings(name):
    Message = 'Hello, ' + name + ' Thankyou for visit my site.'
    return Message
print(greetings('Raj'))


def add_num(num):
    ten = 20
    total = num + ten
    print(greetings('Shivam')) # it is the example of we can easily use same function inside the another fucntion bcoz we using return statement
    return total  
print(add_num(30))


def square_number(x):
    square = x * x
    return square
print(square_number(10))


def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(5))


# sum of number 1 to 10 inside the block of function
def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total

print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
