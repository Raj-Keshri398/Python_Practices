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

# Two Parameter: A function may or may not have a parameter or parameters. A function may also have two or more parameters. 
# If our function takes parameters we should call it with arguments. Let us check a function with two parameters:

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name('Saurabh', 'keshri'))

def sum_of_two_num(first_num, second_num):
    sum = first_num + second_num
    return sum
print("Sum of Two Number is ", sum_of_two_num(3 , 7))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print("Current Age is ", calculate_age(2025, 1999))


def weight_of_object (mass, gravity):
    weight = str(mass * gravity) + ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))


# --------------------------------- Function Returning a Value - Part 2 ---------------------------------------

# * Returning String 

def names(name):
    return name
print(names('shivam'))

# * Returning Value

def subtraction_two_num(first_num, second_num):
    subtract = first_num - second_num
    return subtract
print("Subtraction two no. values : ", subtraction_two_num(45, 21))

# * Returning Boolen

def is_even(n):
    if n % 2 == 0:
        return True
    return False
print(is_even(45))
print(is_even(46))

# * Returning List

def find_even_num(n):
    even= []
    for i in range(n + 1):
        if i % 2 == 0:
            even.append(i)
    return even
print(find_even_num(11))


'''
Arbitrary Number of Arguments


If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of 
arguments by adding * before the parameter name.
'''

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(3, 5, 6, 7, 1)) # numberious of numbers pass in only one agrumwnt of the function using * sign which is called arbitrary

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))


#You can pass functions around as parameters
def square_number (n):
    return n * n * n

def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27


# three function use f key word to print another fucntion data
def square(n):
    return n * n

def cube(n):
    return n * n * n

def apply_twice(f, x):
    return f(f(x))   # f ke andar f()

print(apply_twice(square, 2))


# =============================================== Exercises: Level 1 =========================================================

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(first_num, second_num):
    sum = first_num + second_num
    return sum
print(f'Sum of {3} and {4} is', add_two_numbers(3, 4))

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area
print("Area of Cicle is : ", area_of_circle(30))

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback

def sum_all_numbers(*nums):
    total = 0
    for item in nums:
        # check if item is int or float
        if not isinstance(item, (int, float)):
            return f"Error: This item is '{item}' not a number"
        total += item
    return total
print("Sum all Numbers : ", sum_all_numbers(3 , 4, 5, 6, 1, 2))
print("Sum all numbers : ", sum_all_numbers(3, 'hell', 4, 5, 'hjdf'))


def add_all_nums(*args):
    total = 0
    for x in args:
        # check if item is any string value then skip and add only number value
        if isinstance(x, (int, float)):
            total += x
    return total

print(add_all_nums(1, 2, "hello", 4))  # Output: 7


def add_all_nums(*args):
    total = 0
    for x in args:
        if isinstance(x, (int, float)):
            total += x
        else:
            print(f"Error: '{x}' is not a number.")
    return total

print("Total =", add_all_nums(1, 2, "hello", 4))


# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, 
# convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit
print("Conver the C degree to F degree : ", convert_celsius_to_fahrenheit(40))

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    month = month.lower()

    if month in ['may', 'june', 'july']:
        return "Summer"
    elif month in ['august', 'september', 'october']:
        return "Autumn"
    elif month in ['november', 'december', 'january']:
        return "Winter"
    elif month in ['february', 'march', 'april']:
        return "Spring"
    else:
        return "Invalid month"

print("Season is:", check_season('august'))

#  6. Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)."
    
    slope = (y2 - y1) / (x2 - x1)
    return slope

print(calculate_slope(2, 3, 6, 15))

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic 
# equation, solve_quadratic_eqn.

def solve_quadratic_eqn(a, b, c):
    # Equation: ax² + bx + c = 0
    # Formula: x = (-b ± √(b² − 4ac)) / (2a)

    d = b*b - 4*a*c     # b² - 4ac

    if d < 0:
        return "No real solutions"

    x1 = (-b + (d)**0.5) / (2*a)
    x2 = (-b - (d)**0.5) / (2*a)

    return x1, x2

print("Result:", solve_quadratic_eqn(1, 5, 6))


# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(items):
    for element in items:
        print(element)
print_list([1, 2, 3, "hello", 5])


'''
9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
# 
# '''

def reverse_list(items):
    new_rev_list = []
    for i in range(len(items) - 1, -1, -1):
        new_rev_list.append(items[i])
    print(new_rev_list)

reverse_list([1, 2, 3, 4, 5, 6])
reverse_list(['A', 'B', 'C'])

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_item(items):
    new_list = []
    for item in items:
        new_list.append(item.capitalize())
    return new_list

print(capitalize_list_item(['mango', 'banana', 'apple']))

'''
11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

'''

def add_item(items, item):
    items.append(item)
    return items

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))
