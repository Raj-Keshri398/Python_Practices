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


from xml.etree.ElementTree import ElementTree

import numpy
import pip  # numpy library import kar rahe hain

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

# import pandas as pd  # pandas library import kar rahe hain, aur uska short name pd rakh rahe hain

# # pandas ka version print karega
# print(pd.__version__)

# # ek simple data frame banayenge, jisme 3 columns aur 5 rows hain
# data = {
#     'Name': ['Shivam', 'Amit', 'Priya', 'Rohit', 'Sneha'],
#     'Age': [25, 30, 22, 28, 24],
#     'City': ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata']
# }

# df = pd.DataFrame(data)  # data frame banayenge
# print(df)  # data frame print karega


# print("\n\n")  # thoda space dene ke liye

# import pandas as pd

# # Series banana
# data = [10, 20, 30, 40]
# s = pd.Series(data)
# print(s)

# print("\n\n")  # thoda space dene ke liye

# # Top rows dekhna
# print(df.head())

# # Column select karna
# print(df["Name"])

# # Ek row select karna
# print(df.iloc[0])

# # Shape (rows, columns)
# print(df.shape)

# # Info (data type etc.)
# print(df.info())

# print("\n\n")  # thoda space dene ke liye

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
print("\n\n")  # thoda space dene ke liye

# Further Information About Packages

# 1. Database

    # SQLAlchemy or SQLObject - Object oriented access to several different database systems
    #       pip install SQLAlchemy
    # PyMySQL - MySQL database connector
    #       pip install PyMySQL
    # psycopg2 - PostgreSQL database adapter
    #       pip install psycopg2


# 2. Web Development

        # Django - High-level web framework.
        #   pip install django
        # Flask - micro framework for Python based on Werkzeug, Jinja 2. (It's BSD licensed)
        #   pip install flask
        # Pyramid - A small, fast, down-to-earth Python web framework.
        #   pip install pyramid

# 3. HTML Parser

        # Beautiful Soup - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.
        #   pip install beautifulsoup4
        # PyQuery - implements jQuery in Python; faster than BeautifulSoup, apparently.
        #   pip install pyquery
        # html5lib - A pure-python library for parsing HTML. It parses the same way as a web browser does.
        # pip install html5lib

# 4. Data Visualization

    # Matplotlib - 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.   
    #   pip install matplotlib
    # Seaborn - Statistical data visualization based on matplotlib.
    #   pip install seaborn
    # Bokeh - Interactive Web Plotting for Python.
    #   pip install bokeh
       

# 5. XML Processing

    # ElementTree - The Element type is a simple but flexible container object, designed to store 
    # hierarchical data structures, such as simplified XML infosets, in memory. --Note: Python 2.5 
    # and up has ElementTree in the Standard Library

# 6. Natural Language Processing

    # NLTK - Natural Language Toolkit, a suite of libraries and programs for symbolic and statistical natural language processing for English written in the Python programming language.
    #   pip install nltk
    # spaCy - Industrial-strength Natural Language Processing (NLP) with Python and Cython.
    #   pip install spacy
    # TextBlob - Simplified Text Processing. TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.
    #   pip install textblob

# 7. Machine Learning
    
    # Scikit-learn - A set of python modules for machine learning and data mining.
    #   pip install scikit-learn
    # TensorFlow - An open-source software library for Machine Intelligence.
    #   pip install tensorflow
    # Keras - Deep Learning for humans.
    #   pip install keras

# 8. Computer Vision

    # OpenCV - Open Source Computer Vision Library.
    #   pip install opencv-python
    # Pillow - The friendly PIL fork (Python Imaging Library).
    #   pip install Pillow

# 9. GUI

    # PyQt - Bindings for the cross-platform Qt framework.
    # TkInter - The traditional Python user interface toolkit.
    # wxPython - A blending of the wxWidgets C++ class library with the Python.

# 10. Data Analysis, Data Science and Machine learning

    # Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.

    # Pandas: is a data analysis, data science and a machine learning library in Python that provides data
    # structures of high-level and a wide variety of tools for analysis.

    # SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library 
    # contains modules for optimization, linear algebra, integration, image processing, and statistics.
    
    # Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.

    # TensorFlow: is a machine learning library built by Google.

    # Keras: is considered as one of the coolest machine learning libraries in Python. It provides an 
    # easier mechanism to express neural networks. Keras also provides some of the best utilities for 
    # compiling models, processing data-sets, visualization of graphs, and much more.

# 11. Network:

    # requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)
    # pip install requests



# ================================ Excersies Questions ======================================

# 1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

# import requests
# from collections import Counter
# import re

# romeo_and_juliet = 'https://www.gutenberg.org/files/1112/1112.txt'
# response = requests.get(romeo_and_juliet, timeout=10)
# text = response.text

# # clean words
# words = re.findall(r'\b\w+\b', text.lower())
# word_counts = Counter(words)
# most_common_words = word_counts.most_common(10)
# print("Top 10 words:", most_common_words)

# 2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
        # i.   the min, max, mean, median, standard deviation of cats' weight in metric units.
        # ii.  the min, max, mean, median, standard deviation of cats' lifespan in years.
        # iii. Create a frequency table of country and breed of cats


import requests
import statistics

cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
cats_data = response.json()

weights = []  # ye list rahegi

for cat in cats_data:
    weight_range = cat['weight']['metric'] 
    
    try:
        low, high = weight_range.split(' - ')
        low = float(low)
        high = float(high)
        
        avg_weight = (low + high) / 2
        weights.append(avg_weight)
        
    except:
        continue

print("Weight stats in KG:")
print("Min:", min(weights))
print("Max:", max(weights))
print("Mean:", statistics.mean(weights))
print("Median:", statistics.median(weights))
print("Standard Deviation:", statistics.stdev(weights))    

# -------------------------------
# Lifespan starts
# -------------------------------

lifespans = []

for cat in cats_data:
    lifespan_range = cat['life_span']
    
    try:
        low, high = lifespan_range.split(' - ')
        low = float(low)
        high = float(high)
        
        avg_lifespan = (low + high) / 2
        lifespans.append(avg_lifespan)
        
    except:
        continue

print("Lifespan stats in years:")
print("Min:", min(lifespans))
print("Max:", max(lifespans))
print("Mean:", statistics.mean(lifespans))
print("Median:", statistics.median(lifespans))
print("Standard Deviation:", statistics.stdev(lifespans))   


# -------------------------------
# Breed frequency table
# -------------------------------

from collections import Counter
countries = []
for cat in cats_data:
    country = cat['origin']
    countries.append(country)
    breed_name = cat['name']
    print(f"Country: {country}, Breed: {breed_name}")


country_counts = Counter(countries)
print("\nCountry Frequency Table:")
for country, count in country_counts.items():
    print(f"{country}: {count}")

print("\n\n")  # thoda space dene ke liye

import requests


countries_api = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'

response = requests.get(countries_api, timeout=10)

if response.status_code == 200:
    print("Countries data fetched successfully!")
    countries_data = response.json()
else:
    print("Failed:", response.status_code)
    exit()

# i. 10 largest countries
countries_data.sort(key=lambda x: x.get('area', 0), reverse=True)

print("\nTop 10 Largest Countries:")
for country in countries_data[:10]:
    name = country.get("name", {}).get("common", "Unknown")
    area = country.get("area", 0)
    print(f"{name}: {area} sq km")

# ii. 10 most spoken languages

from collections import Counter

languages = []

for country in countries_data:
    langs = country.get("languages", {})
    
    for lang in langs.values():
        languages.append(lang)

# count karna
lang_count = Counter(languages)

print("\nTop 10 Most Spoken Languages:")

for lang, count in lang_count.most_common(10):
    print(f"{lang}: {count}")

# iii. Hindi speaking countries

hindi_countries = []
count = 0

for country in countries_data:
    langs = country.get("languages", {})

    if "Hindi" in langs.values():
        name = country.get("name", {}).get("common", "Unknown")
        hindi_countries.append(name)
        count += 1
print(f"\nHindi Speaking Countries ({count}):")

for name in hindi_countries:
    print(name)


total_population = 0

for country in countries_data:
    langs = country.get("languages", {})
    
    if "Hindi" in langs.values():
        population = country.get("population", 0)
        total_population += population

print("Total population in Hindi-speaking countries:", total_population)
# iv. 10 most populated countries

import requests

countries_api = 'https://restcountries.com/v2/all'

response = requests.get(countries_api, timeout=10)

# check status
if response.status_code != 200:
    print("API failed:", response.status_code)
    exit()

countries_data = response.json()

# ensure correct type
if not isinstance(countries_data, list):
    print("Invalid data format ❌")
    exit()

populated_countries = []

for country in countries_data:
    population = country.get("population", 0)
    name = country.get("name", "Unknown")
    
    populated_countries.append((name, population))

populated_countries.sort(key=lambda x: x[1], reverse=True)

print("\nTop 10 Most Populated Countries:")
for name, population in populated_countries[:10]:
    print(f"{name}: {population} people")


# 4. UCI is one of the most common places to get data sets for data science and machine learning. 
# Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries 
# it will be difficult, so you may try it with BeautifulSoup4

import requests
from bs4 import BeautifulSoup

UCL = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(UCL)

soup = BeautifulSoup(response.text, 'html.parser')
dataset_links = soup.find_all('a', href=True)
print("Datasets available at UCI:")
for link in dataset_links:
    print(link['href'], link.text)
    