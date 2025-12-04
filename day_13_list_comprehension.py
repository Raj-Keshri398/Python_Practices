# -----------------------------------------  List Comprehension  ----------------------------------------
'''
List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. 
List comprehension is considerably faster than processing a list using the for loop.


simple word:

List comprehension Python me ek short aur fast tarika hai jisse hum loop ka use karke ek new list ek hi line me bana sakte hain.

example:
[i for i in range(5)]

'''

# Example:1
# For instance if you want to change a string to a list of characters. You can use a couple of methods. Let's see some of them:

# method 1

language = 'Python'
lst = list(language)
print(type(lst)) # list
print(lst) # ['P', 'y', 't', 'h', 'o', 'n']

# method 2 list comprehension

language = 'Python'
lst = [i for i in language]
print(type(lst))
print(lst)

# Example:2
# For instance if you want to generate a list of numbers

# Generate numbers
print("------ Generating Numbers ------")
numbers = [i for i in range(11)]
print(numbers)

# It is possible to do mathematical operations during iteration like square etc

print("----- Square -----")
square = [i * i for i in range(11)]
print(square)

# # It is also possible to make a list of tuples

print("------- using list comprehension into tuples -------")
numbers = [(i, i*i) for i in range(11)]
print(numbers)


# Example: 3
# List comprehension can be combined with if expression

# Generating even numbers
print("----- Even Number -----")
even_num = [i for i in range(21) if i % 2 == 0]
print(even_num)

# Filter numbers: let's filter out positive even numbers from the list below
print("----- Positive Even Number ------")
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_number = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_number)

# Flattening a three dimensional array
print("------- Flattred List --------")
list_of_lists = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
flattered_list = [number for row in list_of_lists for number in row]
print(flattered_list)


# =============================================================================================================================



# ---------------------------------------------------------  Lambda Function  ----------------------------------------------------
'''
Lambda function is a small anonymous function without a name. It can take any number of arguments, but can only have one expression. 
Lambda function is similar to anonymous functions in JavaScript. We need it when we want to write an anonymous function inside another
function.


# syntax
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))

--------------------  lambda arguments: expression

Lambda = no-name function (anonymous)
Ek line ka function
One expression

Mostly used with:
map()
filter()
sort()
Another function ke andar

'''

# Example 1.

# normal function

def add(a, b):
    return a + b

# lambda function
adds = lambda a, b: a + b
print(adds(2, 3))

# lambda Square
square = lambda x : x * x
print(square(8))

# Lambda inside another function (IMPORTANT)
def myfun(n):
    return lambda x : x * n

double = myfun(4)
print(double(5))

# Lambda + map() → List ke har element pe operation
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
squared = list(map(lambda x : x * x, numbers))
print(squared)

# Lambda + filter() → Filtering
filtering = list(filter(lambda x : x % 2 == 0, numbers))
print(filtering)

# Lambda + sort()
students = [('Raj', 21), ('Keshri', 19), ('Amit', 25)]
students.sort(key=lambda x : x[1])
print(students)

# Multiple variables

multiple_variable = lambda a, b, c : a ** 2 - 3 * b + 4 * c
print(multiple_variable(3, 4, 5))


# ================================================  Exercises: Day 13  ==================================================

# 1. Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_neg_number = [i for i in numbers if i < 0]
print(f"Filter Negative Number from this list {numbers} to this list {filter_neg_number}")

# 2. Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[
    [[1, 2, 3]], 
    [[4, 5, 6]], 
    [[7, 8, 9]]
]

flattred_num_list = [number for row in list_of_lists for inner in row for number in inner]
print(f"Flattred List is {flattred_num_list}")

# 3. Using list comprehension create the following list of tuples:

result = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)

'''
Output :

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

'''

# 4. Flatten the following list to a new list:

countries = [
    [('Finland', 'Helsinki')], 
    [('Sweden', 'Stockholm')], 
    [('Norway', 'Oslo')]
]

flattred_country = [
                    [country.upper(), country[:3].upper(), capital.upper()] # value is in list
                    for row in countries 
                    for (country, capital) in row
                    ]
print(flattred_country) # output : [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]


# 5. Change the following list to a list of dictionaries:

countries = [
    [('Finland', 'Helsinki')], 
    [('Sweden', 'Stockholm')], 
    [('Norway', 'Oslo')]
]

flattred_country_dict = [{'country' : country.upper(), 'city' : city.upper()}
                         for row in countries
                         for (country, city) in row
                         ]
print(flattred_country_dict) # output : [{'country': 'FINLAND', 'city': 'HELSINKI'}, {'country': 'SWEDEN', 'city': 'STOCKHOLM'}, {'country': 'NORWAY', 'city': 'OSLO'}]


# 6. Change the following list of lists to a list of concatenated strings:


names = [
    [('Asabeneh', 'Yetayeh')], 
    [('David', 'Smith')], 
    [('Donald', 'Trump')], 
    [('Bill', 'Gates')]
]

flattered_list_concatenate = [
                            first_name +' ' + last_name
                            for row in names
                            for (first_name, last_name) in row
                            ]
print(flattered_list_concatenate) # output : ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']




# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.

slope = lambda x1, y1, x2, y2 : (y2 - y1) / (x2 - x1)
print(slope(2, 3, 5, 11))



