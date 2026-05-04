# ======================== Python for Statistical Analysis =====================================

# Statistics

# Statistics is the discipline that studies the collection, organization, displaying, analysing, interpretation 
# and presentation of data. Statistics is a branch of Mathematics that is recommended to be a prerequisite 
# for data science and machine learning. Statistics is a very broad field but we will focus in this section 
# only on the most relevant part. After completing this challenge, you may go onto the web development, data 
# analysis, machine learning and data science path. Whatever path you may follow, at some point in your career 
# you will get data which you may work on. Having some statistical knowledge will help you to make decisions 
# based on data, data tells as they say.

# Statistics is the study of collecting, organizing, analyzing, and interpreting data to make meaningful 
# decisions. It is an important part of mathematics and is widely used in data science and machine learning.


# example :

Marks = [50, 60, 70, 80, 90]

# Data collect karte hain
# Usko arrange karte hain
# Analyze karte hain
# Result samajhte hain
# Aur present karte hain


# Statistics Module

# The Python statistics module provides functions for calculating mathematical statistics of numerical data. 
# The module is not intended to be a competitor to third-party libraries such as NumPy, SciPy, or proprietary 
# full-featured statistics packages aimed at professional statisticians such as Minitab, SAS and Matlab. 
# It is aimed at the level of graphing and scientific calculators.


# Statistics module is the in-build module. Basic calculation use for this module.

import statistics

# example

# Mean (average)
# Median
# Mode
# Standard deviation


# example :
import statistics

data = [10, 20, 30, 40, 50]

# Mean (average)
print(statistics.mean(data))

# Median
print(statistics.median(data))

# Mode
print(statistics.mode(data))


# NumPy = Numerical Python

# In the first section we defined Python as a great general-purpose programming language on its own, but 
# with the help of other popular libraries as(numpy, scipy, matplotlib, pandas etc) it becomes a powerful 
# environment for scientific computing.
# NumPy is the core library for scientific computing in Python. It provides a high-performance multidimensional 
# array object, and tools for working with arrays.
# So far, we have been using vscode but from now on I would recommend using Jupyter Notebook. To access 
# jupyter notebook let's install anaconda. If you are using anaconda most of the common packages are 
# included and you don't have install packages if you installed anaconda.

# simple example :


import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
print(np.mean(arr))
print(np.sum(arr))


# creating INT numpy

import numpy as np

python_list = [1, 2, 3, 4, 5]
print("Type :", type(python_list))
print(python_list)

Two_dimension_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Type of Two dimension Array : ", type(Two_dimension_array))
print(Two_dimension_array)

# Creating Numpy(Numerical Python) array from python list

numpy_array_from_list = np.array(python_list)
print("Type : ", type(numpy_array_from_list))
print(numpy_array_from_list)

# Creating a float numpy array from list with a float data type parameter

numpy_array_from_list2 = np.array(python_list, dtype=float)
print("Type : ", type(numpy_array_from_list2))
print(numpy_array_from_list2)

# Creating a boolean a numpy array from list

numpy_boolen_array = np.array([0, -1, 1, 0, 1], dtype=bool)
print("Type : ", type(numpy_boolen_array))
print(numpy_boolen_array)

# Creating multidimensional array using numpy

Two_dimensional_array = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
numpy_two_dimensional_array = np.array(Two_dimensional_array)
print("Type : ", type(numpy_two_dimensional_array))
print(numpy_two_dimensional_array)

# Converting numpy array to list We can always convert an array back to a python list using tolist().

numpy_to_list = numpy_array_from_list.tolist()
print("Type : ", type(numpy_to_list))
print("One dimensional Array : ", numpy_to_list)
print("Two dimensional Array : ", numpy_two_dimensional_array.tolist())

# Creating numpy array from tuple
# creating tuple

python_tuple = (1,2,3,4,5,6)
print("Type : ", type(python_tuple))
print(python_tuple)

numpy_array_from_tuple = np.array(python_tuple)
print("Type : ", type(numpy_array_from_tuple))
print(numpy_array_from_tuple)

# Shape of numpy array
# The shape method provide the shape of the array as a tuple. The first is the row and the second is the 
# column. If the array is just one dimensional it returns the size of the array.

nums = np.array([1,2,3,4,5])
print(nums)
print("Shape of nums : ", nums.shape)

numpy_two_dimensional_list = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(numpy_two_dimensional_list)
print("shape of two dimensianal : ", numpy_two_dimensional_list.shape)

numpy_three_by_four_array = np.array(
                                        [
                                            [1, 2, 3, 4],
                                            [5, 6, 7, 8],
                                            [0, 9, 10, 11]
                                        ]
                                    )

print(numpy_three_by_four_array)
print("Shape of three by four array: ", numpy_three_by_four_array.shape)

# Data type of numpy array
# Type of data types: str, int, float, complex, bool, list, None

int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
string_array = np.array(int_lists, dtype=str)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)
print(string_array)
print(string_array.dtype)







# What is jupyter notebook ?

# In jupyter notebook we can write the code and get the output too fast. we can add the explaination 
# between the code



