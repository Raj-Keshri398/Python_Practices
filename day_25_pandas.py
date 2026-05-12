# ============================== Pandas ==============================

'''
Pandas is an open source, high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Pandas adds data structures and tools designed to work with table-like data which is Series and Data Frames. Pandas provides tools for data manipulation:

reshaping
merging
sorting
slicing
aggregation
imputation. If you are using anaconda, you do not have install pandas.

For Windows:

pip install conda
pip install pandas

'''

'''
Pandas data structure is based on Series and DataFrames.

A series is a column and a DataFrame is a multidimensional table made up of collection of series. 
In order to create a pandas series we should use numpy to create a one dimensional arrays or a python 
list
'''

# =============================== Importing Pandas ===============================

import pandas as pd
import numpy as np

# =============================== Creating a Series ===============================

# Creating a series from a list
my_list = [1, 2, 3, 4, 5]
my_series = pd.Series(my_list)
print(my_series)

# =========================  Creating a series from a numpy array =========================
my_array = np.array([10, 202, 30, 40, 50])
my_series2 = pd.Series(my_array)
print(my_series2)

# =========================  Creating a series from a dictionary =========================
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
my_series3 = pd.Series(my_dict)
print(my_series3)

# =========================  Creating Pandas Series with custom index =========================
my_scalar = [10, 20, 30, 40, 50]
my_series4 = pd.Series(my_scalar, index=['a', 'b', 'c', 'd', 'e'])
print(my_series4)

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
my_series5 = pd.Series(fruits, index=['a', 'b', 'c', 'd', 'e'])
print(my_series5)


# =============================== Creating a Constant Pandas Series ===============================
my_constant_series = pd.Series(5, index=['a', 'b', 'c', 'd', 'e'])
print(my_constant_series)

# =============================== Creating a Pandas Series Using Linspace ===============================
my_linspace_series = pd.Series(np.linspace(5, 24, 15), index=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']) # linspace(starting, end, items)
print(my_linspace_series)


# =============================== Creating a Pandas Series Using Random Numbers ===============================
my_random_series = pd.Series(np.random.rand(5), index=['a', 'b', 'c', 'd', 'e'])
print(my_random_series)

# =============================== Creating a Pandas Series Using Random Integers ===============================
my_random_int_series = pd.Series(np.random.randint(1, 100, 5), index=['a', 'b', 'c', 'd', 'e'])
print(my_random_int_series)

# =============================== Creating a Pandas Series Using Random Normal Distribution ===============================
my_random_normal_series = pd.Series(np.random.normal(0, 1, 5), index=['a', 'b', 'c', 'd', 'e'])
print(my_random_normal_series)

# =============================== Creating a Pandas Series Using Random Choice ===============================
my_random_choice_series = pd.Series(np.random.choice(['apple', 'banana', 'cherry', 'date', 'elderberry'], 5), index=['a', 'b', 'c', 'd', 'e'])
print(my_random_choice_series)

# =============================== Creating a Pandas Series Using Random Permutation ===============================
my_random_permutation_series = pd.Series(np.random.permutation([1, 2, 3, 4, 5]), index=['a', 'b', 'c', 'd', 'e'])
print(my_random_permutation_series)

# =============================== Creating a Pandas Series Using Random Shuffle ===============================
my_random_shuffle_series = pd.Series(np.random.shuffle([1, 2, 3, 4, 5]), index=['a', 'b', 'c', 'd', 'e'])
print(my_random_shuffle_series)

# ============================== Creating DataFrames from List of Lists ==============================
data = [
    [1, 'Alice', 25],
    [2, 'Bob', 30],
    [3, 'Charlie', 35]
]

df = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])
print(df)

# ============================== Creating DataFrames from List of Dictionaries ==============================

data = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
}

df2= pd.DataFrame(data)
print(df2)


# ============================== Creating DataFrames from Dictionary of Lists ==============================
data = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
}
df3 = pd.DataFrame(data)
print(df3)

# ============================== Reading CSV File Using Pandas ==============================
print("\nReading CSV File Using Pandas")
df4 = pd.read_csv('files/csv_example.csv')
print(df4)

import pandas as pd

# CSV file read
df = pd.read_csv('files/weight-height.csv')

# Print full data
print(df)

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

# Height column
heights = df['Height']
print("\nHeights")
print(heights)

# Weight column
weights = df['Weight']
print("\nWeights")
print(weights)

# Describe
print("\nHeight Describe")
print(heights.describe())

print("\nWeight Describe")
print(weights.describe())

print("\nFull Data Describe")
print(df.describe())


# =================================== Modifying a DataFrame ===================================

'''
Modifying a DataFrame: * We can create a new DataFrame * We can create a new column and add it to the DataFrame, 
* we can remove an existing column from a DataFrame, * we can modify an existing column in a DataFrame, * we can 
change the data type of column values in the DataFrame

Creating a DataFrame

As always, first we import the necessary packages. Now, lets import pandas and numpy, 
'''

import pandas as pd
import numpy as np
 # Create a DataFrame
data = [
  {'ID': 1, 'Name': 'Alice', 'Age': 25},
  {'ID': 2, 'Name': 'Bob', 'Age': 30},
    {'ID': 3, 'Name': 'Charlie', 'Age': 35}
 ]


df9 = pd.DataFrame(data)
print(df9)


# ============================ Adding a New Column to a DataFrame ============================
df9['City'] = ['New York', 'Los Angeles', 'Chicago']
print(df9)

df9['Salary'] = [50000, 60000, 70000]
print(df9)

df9['Department'] = ['HR', 'Engineering', 'Marketing']
print(df9)

df9['Experience'] = [2, 5, 7]
print(df9)

df9['Education'] = ['Bachelor', 'Master', 'PhD']
print(df9)

df9['Height'] = [160, 170, 180]
print(df9)

df9['Weight'] = [60, 70, 80]
print(df9)

# ============================== Modifying column values in a DataFrame ==============================

df9['Salary'] = df9['Salary'] * 1.1
print(df9)

# Using functions makes our code clean, but you can calculate the bmi without one

def claculate_bmi():
    weights = df9['Weight']
    heights = df9['Height']
    bmi = []
    for w, h in zip(weights, heights):
        b = w / (h/100) ** 2
        bmi.append(b)
    return bmi
bmi = claculate_bmi()
df9['BMI'] = bmi
print(df9)


# ==================================== Formatting DataFrame columns ====================================
'''
The BMI column values of the DataFrame are float with many significant digits after decimal. Let's change it to one 
significant digit after point.

'''

df9['BMI'] = round(df9['BMI'], 1)
print(df9)

# ============================== Brith year and current year columns ==============================
df9['Birth Year'] = 2026 - df9['Age']
print(df9)
    

# ============================== Removing a Column from a DataFrame ==============================
df9.drop('Birth Year', axis=1, inplace=True)
print(df9)

# ============================== Changing the Data Type of Column Values in a DataFrame ==============================
df9['Age'] = df9['Age'].astype(float)
print(df9)

# =============================== Boolean Indexing in a DataFrame ===============================
adults = df9[df9['Age'] >= 30]
print(adults)

# =============================== Filtering DataFrame Using Multiple Conditions ===============================
engineering_adults = df9[(df9['Age'] >= 30) & (df9['Department'] == 'Engineering')]
print(engineering_adults)

# =============================== Sorting a DataFrame by Column Values ===============================
sorted_df = df9.sort_values(by='Salary', ascending=False)
print(sorted_df)

# =============================== Grouping Data in a DataFrame ===============================
grouped_df = df9.groupby('Department')['Salary'].mean()
print(grouped_df)

# =============================== Aggregating Data in a DataFrame ===============================
aggregated_df = df9.groupby('Department').agg({'Salary': 'mean', 'Age': 'max'})
print(aggregated_df)


# ============================== Saving a DataFrame to CSV File ==============================
df9.to_csv('files/modified_dataframe.csv', index=False)

# ============================== Saving a DataFrame to Excel File ==============================
df9.to_excel('files/modified_dataframe.xlsx', index=False)

# ============================== Saving a DataFrame to JSON File ==============================
df9.to_json('files/modified_dataframe.json', orient='records', lines=True)

# ============================== Saving a DataFrame to HTML File ==============================
df9.to_html('files/modified_dataframe.html', index=False)

# ============================== Saving a DataFrame to SQL Database ==============================
import sqlite3
conn = sqlite3.connect('files/modified_dataframe.db')
df9.to_sql('modified_dataframe', conn, if_exists='replace', index=False)
conn.close()


