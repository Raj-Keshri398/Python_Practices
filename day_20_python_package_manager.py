# ===========================  What is PIP ? ===============================================

# PIP stands for Preferred installer program. We use pip to install different Python packages. 
# Package is a Python module that can contain one or more modules or other packages. A module or
# modules that we can install to our application is a package. In programming, we do not have to
# write every utility program, instead we install packages and import them to our applications.

# ============================ Installing PIP ================================================

# pip install pip
# Check if pip is installed by writing
# pip --version


# ============================ Installing Python Packages =====================================

# Let us try to install numpy, called numeric python. It is one of the most popular packages in machine 
# learning and data science community.

        # 1. NumPy is the fundamental package for scientific computing with Python. It contains among other things:
        # 2. a powerful N-dimensional array object
        # 3. sophisticated (broadcasting) functions
        # 4. tools for integrating C/C++ and Fortran code
        # 5. useful linear algebra, Fourier transform, and random number capabilities


import numpy  # numpy library import kar rahe hain

# numpy ka version print karega
print(numpy.__version__)

# 0 se 9 tak numbers ki list banayega
my_list = list(range(10))
print(my_list)

# list ko numpy array me convert kar rahe hain
np_array = numpy.array(my_list)

# numpy array print karega
print(np_array)

# array ka type batata hai (numpy.ndarray)
print(type(np_array))

# array ka shape (kitne rows/columns hain)
print(np_array.shape)

# array ka dimension (1D, 2D, etc.)
print(np_array.ndim)

# array ki total length (kitne elements hain)
print(len(np_array))

# har element ko 2 se multiply karega
print(np_array * 2)

# array ko khud se add karega
print(np_array + np_array)

# har element ko 2 se divide karega
print(np_array / 2)

# array ko khud se subtract karega (result 0 aayega)
print(np_array - np_array)

# har element ka square (power 2)
print(np_array ** 2)

# har element ka remainder jab 2 se divide kare (even/odd check)
print(np_array % 2)

# floor division (integer division by 2)
print(np_array // 2)

# sab elements ka total sum
print(np_array.sum())

# average (mean) value
print(np_array.mean())

# sabse chhota value
print(np_array.min())

# sabse bada value
print(np_array.max())

# standard deviation (data ka spread)
print(np_array.std())

# variance (spread ka square)
print(np_array.var())

# cumulative sum (step by step add)
print(np_array.cumsum())

# cumulative product (step by step multiply)
print(np_array.cumprod())

# elements ke sorted order ke index return karega
print(np_array.argsort())

# sabse chhote element ka index
print(np_array.argmin())

# sabse bade element ka index
print(np_array.argmax())


# =========================== Pandas Package ===============================================
print("\n\n\n\n\n")  # thoda space dene ke liye
print("---------------------------- Pandas Package-----------------------\n")
# Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures
# and data analysis tools for the Python programming language. Let us install the big brother of numpy,
# pandas:

import pandas as pd  # pandas library import kar rahe hain, aur uska short name pd rakh rahe hain

# pandas ka version print karega
print(pd.__version__)

# ek simple data frame banayenge, jisme 3 columns aur 5 rows hain
data = {
    'Name': ['Shivam', 'Amit', 'Priya', 'Rohit', 'Sneha'],
    'Age': [25, 30, 22, 28, 24],
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata']
}

df = pd.DataFrame(data)  # data frame banayenge
print(df)  # data frame print karega


print("\n\n")  # thoda space dene ke liye

import pandas as pd

# Series banana
data = [10, 20, 30, 40]
s = pd.Series(data)
print(s)

print("\n\n")  # thoda space dene ke liye

# Top rows dekhna
print(df.head())

# Column select karna
print(df["Name"])

# Ek row select karna
print(df.iloc[0])

# Shape (rows, columns)
print(df.shape)

# Info (data type etc.)
print(df.info())

print("\n\n")  # thoda space dene ke liye

# ============================== Webbrowsing Package ===============================================

# Let us import a web browser module, which can help us to open any website. We do not need to install 
# this module, it is already installed by default with Python 3. For instance if you like to open any 
# number of websites at any time or if you like to schedule something, this webbrowser module can be 
# used.


# import webbrowser  # webbrowser library import kar rahe hain
# # Google kholne ke liye
# webbrowser.open("https://www.google.com")

# url_list = {
#     "Google": "https://www.google.com",
#     "YouTube": "https://www.youtube.com",
#     "Facebook": "https://www.facebook.com",
#     "Twitter": "https://www.twitter.com",
#     "LinkedIn": "https://www.linkedin.com"
# }

# # sabhi websites kholne ke liye loop
# for name, url in url_list.items():
#     print(f"Opening {name}...")
#     webbrowser.open(url)
    

# # 1. Kisi ek package ki full detail dekhna
# pip show numpy
# pip show pandas


# # 2. Saare installed packages ki list
# pip list


# # 3. Kaunse packages outdated hain
# pip list --outdated


# # 4. Saare packages + version (requirements format)
# pip freeze


# # 5. Pip ke saare commands dekhna
# pip help


# # 6. (Optional) Package search (kabhi work nahi karta new version me)
# pip search numpy

print("\n\n\n\n\n")  # thoda space dene ke liye
# =============================== Reading from URL ======================================


# By now you are familiar with how to read or write on a file located on you local machine. Sometimes,
# we would like to read from a website using url or from an API. API stands for Application Program 
# Interface. It is a means to exchange structured data between servers primarily as json data. To open 
# a network connection, we need a package called requests - it allows to open a network connection and 
# to implement CRUD(create, read, update and delete) operations. In this section, we will cover only 
# reading ore getting part of a CRUD.

# We will see get, status_code, headers, text and json methods in requests module:

# get(): to open a network and fetch data from url - it returns a response object
# status_code: After we fetched data, we can check the status of the operation (success, error, etc)
# headers: To check the header types
# text: to extract the text from the fetched response object
# json: to extract json data Let's read a txt file from this website, https://www.w3.org/TR/PNG/iso_8859-1.txt.

# import requests  # requests library import kar rahe hain

# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url)  # url se data fetch kar rahe hain
# print(response.status_code)  # status code print karega (200 means success)
# print(response.headers)  # headers print karega
# print(response.text)  # text content print karega
# print(response.json())  # json data print karega
# print(type(response.text))  # text ka type (string)
# print(type(response.json()))  # json ka type (dict)
# print("\n\n")  # thoda space dene ke liye


# # 1 more example

# import requests
# url = 'https://restcountries.eu/rest/v2/all'  # countries api
# response = requests.get(url)  # opening a network and fetching a data
# print(response) # response object
# print(response.status_code)  # status code, success:200
# countries = response.json()
# print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries


# =================================== Creating a Package ==============================================

# We organize a large number of files in different folders and sub-folders based on some criteria, 
# so that we can find and manage them easily. As you know, a module can contain multiple objects, 
# such as classes, functions, etc. A package can contain one or more relevant modules. A package 
# is actually a folder containing one or more module files. Let us create a package named mypackage, 
# using the following steps:

# Create a new folder named mypackage inside 30DaysOfPython folder Create an empty init.py file in the 
# mypackage folder. Create modules arithmetic.py and greet.py with following code:
print("\n\n\n\n\n")  # thoda space dene ke liye

from mypackage.arithmetics import add_numbers as add
from mypackage.greet import greet_person

print(add(10, 5))
print(greet_person("Aman", "Kumar"))