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


# Indexing and slicing of numpy array
# Indexing and slicing of numpy array is similar to python list. We can use the same

# Indexing
print(nums[0]) # first element
print(nums[1]) # second element
print(nums[-1]) # last element
print(nums[-2]) # second last element


# Mathematical Operation using numpy

'''
NumPy array is not like exactly like python list. To do mathematical operation in Python list we have to loop through the items but numpy can allow to do any mathematical operation without looping. Mathematical Operation:

Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Modules (%)
Floor Division(//)
Exponential(**)

'''

# Addition

arr1 = np.array([1, 2, 3, 4, 5])
print("Original Array for addition : ", arr1)
arr2 = np.array([6, 7, 8, 9, 10])
print("Second Array array for addition : ", arr2)

ten_plus_original = arr1 + 10
print("Ten plus original : ", ten_plus_original)
print("Addition : ", arr1 + arr2)

# Subtraction

arr1 = np.array([1, 2, 3, 4, 5])
print("Original Array for subtraction : ", arr1)
arr2 = np.array([6, 7, 8, 9, 10])
print("Second Array for subtraction : ", arr2)
ten_minus_original = arr1 - 10
print("Ten minus original : ", ten_minus_original)
print("Subtraction : ", arr1 - arr2)

# Multiplication

arr1 = np.array([1, 2, 3, 4, 5])
print("Original Array for multiplication : ", arr1)
arr2 = np.array([6, 7, 8, 9, 10])
print("Second Array for multiplication : ", arr2)
ten_times_original = arr1 * 10
print("Ten times original : ", ten_times_original)
print("Multiplication : ", arr1 * arr2)

# Division

arr1 = np.array([1, 2, 3, 4, 5])
print("Original Array for division : ", arr1)   
arr2 = np.array([6, 7, 8, 9, 10])
print("Second Array for division : ", arr2)
ten_division_original = arr1 / 10
print("Ten division original : ", ten_division_original)
print("Division : ", arr1 / arr2)


# Modulus : Find the remainder of the division

arr1 = np.array([12, 24, 35, 45, 56])
print("Original Array for modulus : ", arr1)
arr2 = np.array([6, 7, 8, 9, 10])
print("Second Array for modulus : ", arr2)
ten_modulus_original = arr1 % 10
print("Ten modulus original : ", ten_modulus_original)
print("Modulus : ", arr1 % arr2)

# Floor Division : Find the quotient of the division

arr1 = np.array([12, 24, 35, 45, 56])
print("Original Array for floor division : ", arr1)
arr2 = np.array([6, 7, 8, 9, 10])
print("Second Array for floor division : ", arr2)
ten_floor_division_original = arr1 // 10
print("Ten floor division original : ", ten_floor_division_original)
print("Floor Division : ", arr1 // arr2)

# Exponential : Find the power of the array

arr1 = np.array([1, 2, 4, 6, 7])
print("Original Array for exponential : ", arr1)
arr2 = np.array([5, 7, 8, 9, 10])
print("Second Array for exponential : ", arr2)
ten_exponential_original = arr1 ** 10
print("Ten exponential original : ", ten_exponential_original)
print("Exponential : ", arr1 ** arr2)

# Checking data types

# Int, Floor, Bool

arr_int = np.array([1, 2, 3, 4, 5])
arr_floor = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
arr_bool = np.array([-1, -3, 0, 1, 4], dtype=bool)

print("Integer Array : ", arr_int.dtype)
print("Floor Array : ", arr_floor.dtype)
print("Boolean Array : ", arr_bool.dtype)

# Converting types

# int to float
arr_int = np.array([1, 2, 3, 4, 5], dtype='float')
print("Integer Array : ", arr_int)

# float to int
arr_float = np.array([1.1, 2.2, 3.3, 4.4, 5.5], dtype='int')
print("Float Array : ", arr_float)

# int to bool
arr_int = np.array([1, 2, 0, 4, 5], dtype='bool')
print("Integer Array to boolean : ", arr_int)

# int to str 
arr_int = np.array([1, 2, 3, 4, 5])
arr_int.astype('int').astype('str')
print("Integer Array to string : ", arr_int)

# Multi-dimensional Arrays

two_dimensional_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Two dimensional array : ", two_dimensional_array)
print("Shape of two dimensional array : ", two_dimensional_array.shape)
print("Data type of two dimensional array : ", two_dimensional_array.dtype)
print("Size of two dimensional array : ", two_dimensional_array.size)
print("First row of two dimensional array : ", two_dimensional_array[0])
print("Second row of two dimensional array : ", two_dimensional_array[1])
print("Third row of two dimensional array : ", two_dimensional_array[2])
print("First column of two dimensional array : ", two_dimensional_array[:, 0])
print("Second column of two dimensional array : ", two_dimensional_array[:, 1])
print("Third column of two dimensional array : ", two_dimensional_array[:, 2])
print(two_dimensional_array)

# Slicing Numpy array
# Slicing in numpy is similar to slicing in python list

two_dimensional_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Two dimensional array : ", two_dimensional_array)
first_two_rows_and_columns = two_dimensional_array[:2, :2]
print("First two rows and columns : ", first_two_rows_and_columns)
last_two_rows_and_columns = two_dimensional_array[1:, 1:]
print("Last two rows and columns : ", last_two_rows_and_columns)
first_row_and_last_column = two_dimensional_array[0, -1]
print("First row and last column : ", first_row_and_last_column)
last_row_and_first_column = two_dimensional_array[-1, 0]
print("Last row and first column : ", last_row_and_first_column)

# Reverse the row and column positions

two_dimensional_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Two dimensional array : ", two_dimensional_array)
reverse_row_and_column = two_dimensional_array[::-1, ::-1]
print("Reverse row and column : ", reverse_row_and_column)

# How to represent missing values ? or NaN values in numpy array or replace missing values with mean or median ?

two_dimensional_array = np.array([[1, 2, 3], [4, np.nan, 6], [7, 8, 9]])
print("Two dimensional array with NaN value : ", two_dimensional_array)
two_dimensional_array[1, 1] = 55
print("Two dimensional array after replacing NaN value with 55 : ", two_dimensional_array)

# numpy Zeros and Ones
zeros_array = np.zeros((3, 3), dtype=int, order='C')
print("Zeros array : ", zeros_array)
ones_array = np.ones((3, 3), dtype=int, order='C')
print("Ones array : ", ones_array)
twos_array = ones_array * 2
print("Twos array : ", twos_array)

# reshape of numpy array
# Reshape is used to change the shape of the array without changing the data. The new shape should be 
# compatible with the original shape. The total number of elements should be the same.

# reshape()
# flatten()

reshape_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("Original array : ", reshape_array)
reshaped_array = reshape_array.reshape(3, 4)
print("Reshaped array : ", reshaped_array)

flattened_array = reshape_array.flatten()
print("Flattened array : ", flattened_array)

# Horizontal and vertical stacking of numpy array

np_list_one = np.array([1, 2, 3])
np_list_two = np.array([4, 5, 6])
print("First array : ", np_list_one)
print("Second array : ", np_list_two)
print(np_list_one + np_list_two) # element wise addition
print("horizontal Append : ", np.hstack((np_list_one, np_list_two)))
print("Vertical Append : ", np.vstack((np_list_one, np_list_two)))







# What is jupyter notebook ?

# In jupyter notebook we can write the code and get the output too fast. we can add the explaination 
# between the code



