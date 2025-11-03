'''
Dictionaries


    * A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
'''

# for example 

# Creating a Dictionary
# To create a dictionary we use curly brackets, {} or the dict() built-in function.

person = {
    'First_Name' : 'Raj',
    'Last_Name'  : 'Keshri',
    'Age'        : 25,      
    'Country'    : 'India',
    'is_married' : False,
    'Skills'     : ['python', 'javascript', 'css', 'html', 'php'],
    'Address'    :  {
        'Street'         : 'Marufgang',
        'Zipcode'        : '800008'
    } 
}

print(person)

# length of the dictionary

print("Length of the Dictonary : ", len(person))

# We can access Dictionary items by referring to its key name.

print(person['Age']) # 25
print(person['First_Name']) # Raj
print(person['Country'])    # India
print(person['Skills'])     # ['python', 'javascript', 'css', 'html', 'php']
print(person['Skills'][0])  # python
print(person['Address']['Street']) # Space street
#print(person['City'])       # Error


'''
Accessing an item by key name raises an error if the key does not exist. 
To avoid this error first we have to check if a key exist or we can use the get method. 
The get method returns None, which is a NoneType object data type, if the key does not exist.

'''

print(person.get('City')) # None when we use get method it will not throw the error. it show None instead of error
print(person.get('Last_Name')) # Keshri

# Adding Items to a Dictionary
#  * We can add new key and value pairs to a dictionary

person = {
    'First_Name' : 'Raj',
    'Last_Name'  : 'Keshri',
    'Age'        : 25,      
    'Country'    : 'India',
    'is_married' : False,
    'Skills'     : ['python', 'javascript', 'css', 'html', 'php'],
    'Address'    :  {
        'Street'         : 'Marufgang',
        'Zipcode'        : '800008'
    } 
}

person['Job_Title'] = 'Developer'
person['Skills'].append('Mysql')
person['Address']['Locality'] = 'DeviAsthan'
print(person)


person = {
    'First_Name' : 'Raj',
    'Last_Name'  : 'Keshri',
    'Age'        : 25,      
    'Country'    : 'India',
    'is_married' : False,
    'Skills'     : ['python', 'javascript', 'css', 'html', 'php'],
    'Address'    :  {
        'Street'         : 'Marufgang',
        'Zipcode'        : '800008'
    } 
}

# make a new dictonary to add role after the country
new_persons = {}
for key, value in person.items():
    new_persons[key] = value
    if key == 'Country':
        new_persons['Role'] = 'Software Developer'

person = new_persons
print(person)

# Modifying Items in a Dictionary

person['First_Name'] = 'Nisha'
person['Age'] = 23
person['Role'] = 'Executive'
print(person)

# Checking Keys in a Dictionary

print('Last_Name' in person) # True
print('key' in person) # False

# Removing Key and Value Pairs from a Dictionary

#   * pop(key): removes the item with the specified key name:
#   * popitem(): removes the last item
#   * del: removes an item with specified key name

person.pop('Role')
person.popitem()
del person['Age']
print(person)


# Changing Dictionary to a List of Items
#   * The items() method changes dictionary to a list of tuples.

print(person.items())

# Clearing a Dictionary
#   * If we don't want the items in a dictionary we can clear them using clear() method

person.clear()
print(person)

# Copy a Dictionary
# * We can copy a dictionary using a copy() method. 
#   Using copy we can avoid mutation of the original dictionary.


person = {
    'First_Name' : 'Raj',
    'Last_Name'  : 'Keshri',
    'Age'        : 25,      
    'Country'    : 'India',
    'is_married' : False,
    'Skills'     : ['python', 'javascript', 'css', 'html', 'php'],
    'Address'    :  {
        'Street'         : 'Marufgang',
        'Zipcode'        : '800008'
    } 
}

person_cpy = person.copy()
print(person_cpy)

# Getting Dictionary Keys as a List
#   * The keys() method gives us all the keys of a a dictionary as a list.
#   * The values method gives us all the values of a a dictionary as a list. 


keys = person.keys()
print(keys)
values = person.values()
print(values)

# ---------------------------------- Exercises: Day 8 ----------------------------------------------


# * 1. Create an empty dictionary called dog

dog = {}

# * 2. Add name, color, breed, legs, age to the dog dictionary

dog['name'] = 'Laddu'
dog['color'] = 'White'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 8
print("Dog Dictonary : ", dog)

# * 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, 
#   country, city and address as keys for the dictionary

student = {
    'first_name' : 'nisha',
    'last_name'  : 'gupta',
    'gender'     : 'female',
    'age'        : 24,
    'is_married' : False,
    'skills'     : ['Canva', 'Mysql', 'Designar', 'Data Handling'],
    'country'    : 'India',
    'city'       : 'Patna',
    'address'    : 'dujra'
}

print(student)

# * 4. Get the length of the student dictionary

print("Length of the Student Dictonary : " ,len(student))

# * 5. Get the value of skills and check the data type, it should be a list

value = student['skills']
print(value)
print(type(value))


# * 6. Modify the skills values by adding one or two skills

student['skills'].append('python')
student['skills'].append('html')
print(student)

# * 7. Get the dictionary keys as a list

keys = student.keys()
print(keys)

# * 8. Get the dictionary values as a list

values = student.values()
print(values)

# * 9. Change the dictionary to a list of tuples using items() method

person = {
    'First_Name' : 'Raj',
    'Last_Name'  : 'Keshri',
    'Age'        : 25,      
    'Country'    : 'India',
    'is_married' : False,
    'Skills'     : ['python', 'javascript', 'css', 'html', 'php'],
    'Address'    :  {
        'Street'         : 'Marufgang',
        'Zipcode'        : '800008'
    } 
}


student_list = list(student.items())
print(student_list)
print(type(student_list))


# * 10. Delete one of the items in the dictionary

person = {
    'First_Name' : 'Raj',
    'Last_Name'  : 'Keshri',
    'Age'        : 25,      
    'Country'    : 'India',
    'is_married' : False,
    'Skills'     : ['python', 'javascript', 'css', 'html', 'php'],
    'Address'    :  {
        'Street'         : 'Marufgang',
        'Zipcode'        : '800008'
    } 
}

person.popitem()
print(person)






