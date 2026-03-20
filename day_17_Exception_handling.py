# =================================== Exception Handling ===================================

# Exception handling is a mechanism to handle runtime errors in a controlled manner. 
# It allows you to write code that can gracefully handle errors without crashing the program.

# Example of exception handling using try-except block
'''
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Division by zero is not allowed.")    
# Output: Error: Division by zero is not allowed.
'''

'''
try:
    print(10 + '5')
except:
    print("Error: Invalid operation.")
# Output: Error: Invalid operation.
'''

'''
try:
    print(10 + 5)
except:
    print("Error: Invalid operation.")
# Output: 15
'''


# You can also catch multiple exceptions in a single except block by using a tuple of exception types

'''
try:
    # Code that might raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
except (ZeroDivisionError, ValueError):
    # Code to handle the exceptions
    print("Error: Invalid input or division by zero is not allowed.")
# Output: Error: Invalid input or division by zero is not allowed.
'''

'''
try:
    name = input("Enter your name: ")
    year_born = int(input("Enter your year of birth: "))
    age = 2026 - year_born
    print(f"Hello {name}, you are {age} years old.")
except:
    print("Error: Invalid input. Please enter a valid name and year of birth.")
# Output: Hello John, you are 30 years old. (if valid input is provided)
'''

'''
from datetime import datetime

try:
    name = input("Enter your name: ")
    dob_input = input("Enter your DOB (DD-MM-YYYY): ")

    # string ko datetime me convert karo
    dob = datetime.strptime(dob_input, "%d-%m-%Y")

    today = datetime.now()

    # age calculation
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    # adjust negative days
    if days < 0:
        months -= 1
        # previous month ke days add karo
        prev_month = (today.month - 1) or 12
        prev_year = today.year if today.month != 1 else today.year - 1
        days_in_prev_month = (datetime(today.year, today.month, 1) - datetime(prev_year, prev_month, 1)).days
        days += days_in_prev_month

    # adjust negative months
    if months < 0:
        years -= 1
        months += 12

    print(f"Hello {name}, your exact age is {years} years, {months} months, {days} days.")

except:
    print("Error: Invalid input. Please use format DD-MM-YYYY")

'''
    
# You can also use the finally block to execute code regardless of whether an exception occurred or not
'''
try:    
    # Code that might raise an exception
    result = 10 / 2
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Division by zero is not allowed.")
finally:
    # Code to execute regardless of whether an exception occurred or not
    print("This will always be executed.")  
# Output:
# This will always be executed. 
'''


# more Examples of exception handling

# Example 1: Handling multiple exceptions but it type error occured example.

'''
try:
    name = input("Enter your name : ")
    born_year = input("Enter your year of birth : ")
    age = 2026 - born_year
    print(f"Hello {name}, you are {age} years old.")
except TypeError:
    print("Error: Invalid input. Please enter a valid name and age. It is type error occurred.")
except ValueError:
    print("Error: Invalid input. Please enter a valid name and age. it is value error occurred.")
except ZeroDivisionError:
    print("Error: Invalid input. Please enter a valid name and age. it is zero division error occurred.")
except:
    print("Error: Invalid input. Please enter a valid name and age. it is some other error occurred.")
'''


# it is type error occurred example improvised using int() function to convert string to integer of born_year

'''
try:
    name = input("Enter your name : ")
    born_year = input("Enter your year of birth : ")
    age = 2026 - int(born_year)
    print(f"Hello {name}, you are {age} years old.")
except TypeError:
    print("Error: Invalid input. Please enter a valid name and age. It is type error occurred.")
except ValueError:
    print("Error: Invalid input. Please enter a valid name and age. it is value error occurred.")
except ZeroDivisionError:
    print("Error: Invalid input. Please enter a valid name and age. it is zero division error occurred.")
except:
    print("Error: Invalid input. Please enter a valid name and age. it is some other error occurred.")

'''

# example 2: Handling multiple exceptions but use finally and else block also to show how it works with try block

'''
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2026 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')


# It is also shorten the above code as follows 

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2026 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

'''

# ==================================== Packing and Unpacking Arguments in Python ====================================

'''
We use two operators:

* for tuples
** for dictionaries

Packing: It is the process of collecting multiple values into a single variable.
Unpacking: It is the process of extracting values from a collection and assigning them to individual variables.

Example of packing and unpacking with tuples:
'''

# Unpacking a tuple

def sum_of_numbers(a, b, c):
    return a + b + c

lst = [1, 2, 3]
# result = sum_of_numbers(lst)  # This will raise a TypeError because the function expects three separate arguments, not a single list.

# To fix this, we can unpack the list using the * operator:

result = sum_of_numbers(*lst)  # This will unpack the list into three separate arguments.
print(result)  # Output: 6

# We can also use unpacking in the range built-in function that expects a start and an end.

numbers = range(1, 10) # normal call with separate arguments
print(list(numbers))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
args = [1, 10]
numbers = range(*args)  # call with arguments unpacked from a list
print(list(numbers))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


# A list or a tuple can also be unpacked like this:

countries = ['India', 'USA', 'UK', 'Germany', 'France', 'Italy', 'Spain', 'Australia', 'Japan', 'China']
Ind, Us, U, Ger, *rest = countries
print(Ind, Us, U, Ger, rest)  # Output: India USA UK Germany ['France', 'Italy', 'Spain', 'Australia', 'Japan', 'China']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, *middle, last = numbers
print(first, middle, last)  # Output: 1 [2, 3, 4, 5, 6, 7, 8] 9

# Unpacking Dictionaries

def print_person_info(name, age, city, country):
    print(f"He is {name} his age is {age} he lives in {city} his country name is {country}")

person_info = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'country': 'USA'
}
print_person_info(**person_info)  # Output: He is John his age is 30 he lives in New York his country name is USA


# ================================== Packing ===================================

'''
Packing

Sometimes we never know how many arguments need to be passed to a python function. 
We can use the packing method to allow our function to take unlimited number or arbitrary 
number of arguments.

'''

# packing list of arguments using *args


def sum_of_numbers(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
result = sum_of_numbers(1, 2, 3, 4, 5)
result2 = sum_of_numbers(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(result)  # Output: 15
print(result2)  # Output: 550

# Packing Dictionaries using **kwargs

def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_person_info(name='John', age=30, city='New York', country='USA')
# Output: 
# name: John
# age: 30   
# city: New York
# country: USA


# ===================================  Spreading in Python ==============================

# Spreading is a technique used to unpack elements from an iterable (like a list, tuple, or set) 
# and insert them into another iterable or function call.
print('-----------------------------------------------')
lst_one = [1, 2, 3]
lst_two = [4, 5, 6]
# Using the * operator to spread the elements of lst_one and lst_two into a new list
combined_list = [*lst_one, *lst_two]
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]

country_lst_one = ['India', 'USA', 'UK']
country_lst_two = ['Germany', 'France', 'Italy']
# Using the * operator to spread the elements of country_lst_one and country_lst_two into a new list
combined_country_lst = [*country_lst_one, *country_lst_two]
print(combined_country_lst)  # Output: ['India', 'USA', 'UK', 'Germany', 'France', 'Italy']

# ==================================== Enumerate ====================================

# The enumerate() function in Python is a built-in function that allows you to loop over an iterable
# (like a list, tuple, or string) and have an automatic counter.
# It returns an enumerate object that contains pairs of index and value for each item in the iterable


print('-----------------------------------------------')
countries = ['India', 'USA', 'UK', 'Germany', 'France']
for index, country in enumerate(countries):
    print(f"{index}: {country}")
# Output:
# 0: India
# 1: USA
# 2: UK
# 3: Germany
# 4: France


for index, num in enumerate([2, 3, 4]):
    print(f"Index is {index} and Number is {num}")
# Output:
# Index is 0 and Number is 2
# Index is 1 and Number is 3
# Index is 2 and Number is 4


countries = ['India', 'USA', 'UK', 'Germany', 'France']
for index, i in enumerate(countries):
    if i == 'Germany':
        print(f"Index of Germany found on index No. {index}")

# =======================================  Zip Function =====================================

# The zip() function in Python is a built-in function that takes multiple iterables 
# (like lists, tuples, or strings) and returns an iterator of tuples.
# Each tuple contains the elements from the input iterables that are at the same index.

print('-----------------------------------------------')
countries = ['India', 'USA', 'UK']
capitals = ['New Delhi', 'Washington D.C.', 'London']
# Using the zip() function to combine the countries and capitals into a list of tuples
country_and_capitals = []
for cou, cap in zip(countries, capitals):
    country_and_capitals.append({'country': cou, 'capital': cap})
print(country_and_capitals)
# Output: [{'country': 'India', 'capital': 'New Delhi'}, {'country': 'USA', 'capital': 'Washington D.C.'}, {'country': 'UK', 'capital': 'London'}]
