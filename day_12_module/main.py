
# ---------------------------------  Importing a Module  ------------------------------
import mymodule
print(mymodule.generate_full_name('Shivam', 'Keshri'))


# ------------------------------- Import Functions from a Module ----------------------------
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Nisha', 'Bharti'))
print(sum_two_nums(8, 9))
mass = 1000
weight = mass * gravity
print(weight)
print(person['skills'])
print(person)

# ------------------------------  Import Functions from a Module and Renaming ------------------------

from mymodule import generate_full_name as fullnames, sum_two_nums as total, person as p, gravity as g
print(fullnames('Chanda', 'Devi'))
print(total(30, 19))
mass = 2000
weight = mass * g
print(weight)
print(p['first_name'])

# ----------------------------  Import Built-in Modules  -----------------------------------

# 1. Math module

import math
print(math.sqrt(25))
print(math.pi)

# 2. random module

import random
print(random.randint(1, 10))

# 3. datetime module

import datetime
print(datetime.datetime.now())

# 4. json module

import json
print(json.loads('{"name":"Raj"}'))

# ---------------------------------- OS Module ------------------------------------------

import os

# 1. Check current working directory
print("Start:", os.getcwd())

# 2. Create directory (only if not exists)
folder_path = r"E:\python\30_day_python\day_12_module\directory_name"

if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print("Folder created:", folder_path)
else:
    print("Folder already exists:", folder_path)

# 3. Change directory
os.chdir(folder_path)
print("Changed to:", os.getcwd())

# 4. Go back to parent directory (IMPORTANT)
os.chdir("..")
print("Back to:", os.getcwd())

# 5. Remove directory
os.rmdir(folder_path)
print("Folder deleted:", folder_path)
