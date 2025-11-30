# ------------------------------------------------- Modules ---------------------------------------------------

# ----------------------------------   What is a Module   ---------------------------
'''
A module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file 
containing a single variable, a function or a big code base.

-------- Simple Word ----------

Module ek dabba (box) jaisa hota hai jisme useful code rakha hota hai. Hum jab chahen us box ko import karke uska code use kar 
lete hain.
'''

# --------------------------------- Creating a Module ---------------------------------------

'''

To create a module we write our codes in a python script and we save it as a .py file. Create a file named mymodule.py inside your 
project folder. Let us write some code in this file.

# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
    
''' 

# --------------------------------  Importing a Module  ----------------------------------------

'''
To import the file we use the import keyword and the name of the file only.

# main.py file
import mymodule
print(mymodule.generate_full_name('Shivam', 'Keshri')) # Shivam Keshri

'''

# ------------------------------ Import Functions from a Module -------------------------------

'''
We can have many functions in a file and we can import all the functions differently.

# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100;
weight = mass * gravity
print(weight)
print(person['firstname'])

'''

# --------------------------- Import Functions from a Module and Renaming -----------------------------

'''
During importing we can rename the name of the module.

# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

'''

# ----------------------------------------  Import Built-in Modules ------------------------------------

'''
Like other programming languages we can also import modules by importing the file/function using the key word import. 
Let's import the common module we will use most of the time. Some of the common built-in modules: math, datetime, os,sys, 
random, statistics, collections, json,re


# Simple meaning

Built-in module = Python ke andar pehle se bana hua ready-made code.

Matlab:
1. Python already written the code
2. we can use #import to use the in-build code which is made by python
3. this is the type of library.

-----------------------------------------------------------------------------------------

1. Math module

import math
print(math.sqrt(25))  # 5
print(math.pi)        # 3.14159....

2. random module

import random
print(random.randint(1, 10))  # 1 to 10 random number

3. Date module

import datetime
print(datetime.datetime.now())

4. json module

import json
print(json.loads('{"name":"Raj"}'))

'''


# --------------------------------------------- OS Module  -------------------------------------------------

'''
Using python os module it is possible to automatically perform many operating system tasks. The OS module in Python provides functions 
for creating, changing current working directory, and removing a directory (folder), fetching its contents, changing and identifying the 
current directory.


----------------------------------------------------------

Original Line:

“The OS module in Python provides functions for creating, changing current working directory, and removing a directory (folder), 
fetching its contents, changing and identifying the current directory.”

Simple Meaning:

OS module ke andar kuch ready-made functions hote hain jinke through hum:

✔ 1) Naya folder bana sakte hai

os.mkdir("folder_name")

✔ 2) Current working directory change kar sakte hai

os.chdir("path")

✔ 3) Folder delete kar sakte hai

os.rmdir("folder_name")

✔ 4) Folder ke andar kya-kya files/folders hain woh dekh sakte hai

os.listdir()

✔ 5) Abhi hum kaun se folder (directory) me hai, woh pta laga sakte hai

os.getcwd()

'''