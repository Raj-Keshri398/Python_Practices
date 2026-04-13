# # ================================== File Handling ==================================

# '''
# File handling is a crucial aspect of programming that allows us to read from and write to files on our 
# computer. In Python, we can use built-in functions to work with files. Here are some common operations 
# for file handling:   

# So far we have seen different Python data types. We usually store our data in different file formats. 
# In addition to handling files, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, 
# .excel) in this section. First, let us get familiar with handling files with common file format(.txt).

# File handling is an import part of programming which allows us to create, read, update and delete files.
# In Python to handle data we use open() built-in function. 
# The open() function takes two parameters: the name of the file and the mode in which we want to open the 
# file. The mode can be:'''

# # Syntax
# # open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

# '''
# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
# '''


# # --------------------------------- Opening Files for Reading ---------------------------------
# import os

# # folder create (agar nahi hai)
# os.makedirs('files', exist_ok=True)

# # file create + write use encoding to support emojis
# f = open('./files/reading_file_example.txt', 'w', encoding='utf-8')
# f.write("Hello bhai 👋\nThis is second line")

# f.close()

# # Read the file
# f = open('./files/reading_file_example.txt', 'r', encoding='utf-8')
# line = f.readline()
# print(type(line))
# print(line)
# f.close()

# f = open('./files/reading_file_example.txt', 'r', encoding='utf-8')
# txt = f.read()
# print(type(txt))
# print(txt)
# f.close()

# # Step 1: Read old data
# with open('./files/reading_file_example.txt', 'r', encoding='utf-8') as f:
#     txt = f.read().splitlines()
#     print("Before Append:", txt)

# # Step 2: Append new data
# with open('./files/reading_file_example.txt', 'a', encoding='utf-8') as f:
#     f.write('\nThis text has to be appended at the end') 
#     print('Text appended successfully')

# # Step 3: Read updated data
# with open('./files/reading_file_example.txt', 'r', encoding='utf-8') as f:
#     updated_txt = f.read().splitlines()
#     print("After Append:", updated_txt)


# # ---------------------------------- deleting a file ----------------------------------
# # os.remove('./files/reading_file_example.txt'

# import os
# if os.path.exists('./files/example.txt'):
#     os.remove('./files/example.txt')
# else:
#     print("The file does not exist")

# # ---------------------------- File Type ----------------------------------------


# # File with txt Extension
# # File with txt extension is a very common form of data and we have covered it in the previous section.
# # Let us move to the JSON file

# # File with json Extension
# # JSON stands for JavaScript Object Notation. Actually, it is a stringified JavaScript object or Python 
# # dictionary.

# # Example:

# # dictionary
# person_dct= {
#     "name": "kumar",
#     "age": 25,
#     "country": "India",
#     "skills": ["Python", "JavaScript", "SQL"]
# }


# print('------------------------------- Json -------------------------------')


# # JSON: A string form a dictionary

# person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"


# # we use three quotes and make it multiple line to make it more readable

# person_json = '''{
#     "name": "shrikant",
#     "age": 35,
#     "country": "India",
#     "skills": ["Python", "JavaScript", "SQL"]
# }'''

# # Changing JSON to Dictionary
# # To change a JSON to a dictionary, first we import the json module and then we use loads method.


# print('------------------------------- Json to Dictionary -------------------------------')


# import json

# person_json = '''{
#     "name": "shrikant",
#     "age": 35,
#     "country": "India",
#     "skills": ["Python", "JavaScript", "SQL"]
# }'''

# person_dict = json.loads(person_json) # use json.loads() to convert JSON string to a Python dictionary
# print(type(person_dict))
# print(person_dict)
# print(person_dict['name'])
# print(person_dict['skills'][1])


# # Changing Dictionary to JSON
# # To change a dictionary to a JSON we use dumps method from the json module.
# print('------------------------------- Dictionary to Json -------------------------------')

# import json

# person = {
#     "name": "kumar",
#     "age": 25,
#     "country": "India",
#     "skills": ["Python", "JavaScript", "SQL"]
# }

# person_json = json.dumps(person) # use json.dumps() to convert a Python dictionary to a JSON string
# print(type(person_json))
# print(person_json)


# # Saving as Json file
# # We can also save our data as a json file. Let us save it as a json file using the following steps. 
# # For writing a json file, we use the json.dump() method, it can take dictionary, output file, 
# # ensure_ascii and indent.

# import json
# person = {
#     "name": "keshav",
#     "age": 25,
#     "country": "India",
#     "skills": ["Python", "JavaScript", "SQL"]
# }

# with open('./files/person.json', 'w', encoding='utf-8') as f:
#     json.dump(person, f, ensure_ascii=False, indent=4) # use json.dump() to write a Python dictionary to a JSON file
#     print('Json file created successfully')


# # ---------------------------- File with csv Extension ----------------------------
# # CSV stands for comma separated values. CSV is a simple file format used to store tabular data, 
# # such as a spreadsheet or database. CSV is a very common data format in data science.

# print('------------------------------- CSV -------------------------------')

# import csv
# with open('./files/csv_example.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Name', 'Age', 'Country'])
#     writer.writerow(['kumar', 25, 'India'])
#     writer.writerow(['shrikant', 35, 'India'])
#     print('CSV file created successfully')

# with open('./files/csv_example.csv', 'r') as f:
#     csv_reader = csv.reader(f, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} is {row[1]} years old and lives in {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count - 1} lines.')


# print('------------------------------- File with xlsx Extension -------------------------------')

# # ------------------------------------- File with xlsx Extension -------------------------------------

# # ---------------------- Excel File Create (Write Data) ----------------------

# from openpyxl import Workbook   # Excel file create karne ke liye module

# # Workbook object create kiya (ye ek Excel file hoti hai)
# wb = Workbook()

# # Active sheet (default sheet jo open hoti hai)
# ws = wb.active

# # Header row add kiya
# ws.append(['Name', 'Age', 'Country'])

# # Data rows add kiya
# ws.append(['kumar', 25, 'India'])
# ws.append(['shrikant', 35, 'India'])

# # File ko save kiya given path par
# wb.save('./files/excel_example.xlsx')

# print("File created successfully")


# # ---------------------- Excel File Read (Sheet Info) ----------------------

# from openpyxl import load_workbook   # read Excel files

# # Load excel file
# excel_book = load_workbook('./files/excel_example.xlsx')

# # Count number of sheets
# print(len(excel_book.sheetnames))

# # print sheet names
# print(excel_book.sheetnames)


# # ---------------------- Excel File Read (Data Print) ----------------------

# # Select active sheet
# sheet = excel_book.active

# # print each row data
# for row in sheet.iter_rows(values_only=True):
#     print(row)



# # ------------------------------------- File with xml Extension -------------------------------------

# # File with xml Extension
# # XML is another structured data format which looks like HTML. In XML the tags are not predefined. 
# # The first line is an XML declaration. The person tag is the root of the XML. The person has a gender 
# # attribute. 

# # Example:XML

# # ---------------------- XML Example ----------------------

# # XML data (string format me)
# person_xml = '''<?xml version="1.0" encoding="UTF-8"?>
# <person gender="male">
#     <name>kumar</name>
#     <age>25</age>
#     <country>India</country>
#     <skills>
#         <skill>Python</skill>
#         <skill>JavaScript</skill>
#         <skill>SQL</skill>
#     </skills>
# </person>'''

# import xml.etree.ElementTree as ET

# # ---------------------- Step 1: XML file created ----------------------

# with open('./files/xml_example.xml', 'w', encoding='utf-8') as f:
#     f.write(person_xml)   # save sting data as XML file

# print("XML file created successfully")


# # ---------------------- Step 2: XML file parse ----------------------

# tree = ET.parse('./files/xml_example.xml')  # file read 
# root = tree.getroot()  # Get root element 

# # ---------------------- Step 3: Data print ----------------------

# # root tag print
# print('Root tag:', root.tag)

# # root attributes print
# print('Attribute:', root.attrib)

# # child elements print
# for child in root:
#     print('field:', child.tag)



# # =============================== Questions ===============================
# print('------------------------------- Questions -------------------------------')

# # 1. Write a function which count number of lines and number of words in a text. 
# # All the files are in the data the folder:

#         # i. Read obama_speech.txt file and count number of lines and words
#         # ii. Read michelle_obama_speech.txt file and count number of lines and words
#         # iii. Read donald_speech.txt file and count number of lines and words
#         # iv. Read melina_trump_speech.txt file and count number of lines and words


# import os

# # Create folder if it doesn't exist
# os.makedirs('questions', exist_ok=True)

# # file create + write use encoding to support emojis
# f = open('./questions/obama_speech.txt', 'w', encoding='utf-8')
# f.write("Hello obama 👋\nThis is second line \n its third")
# f = open('./questions/michelle_obama_speech.txt', 'w', encoding='utf-8')
# f.write("Hello michelle 👋\nThis is second line \n its third")
# f = open('./questions/donald_speech.txt', 'w', encoding='utf-8')
# f.write("Hello donald 👋\nThis is second line \n its third")
# f = open('./questions/melina_trump_speech.txt', 'w', encoding='utf-8')
# f.write("Hello melina 👋\nThis is second line \n its third")


# f.close()

# # i. Read obama_speech.txt file and count number of lines and words

# with open('./questions/obama_speech.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     num_lines = len(lines)
#     num_words = sum(len(line.split()) for line in lines)
#     print(lines)

# print(f"Obama speech - Lines: {num_lines}, Words: {num_words}")

# # ii. Read michelle_obama_speech.txt file and count number of lines and words

# with open('./questions/michelle_obama_speech.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     num_lines = len(lines)
#     num_words = sum(len(line.split()) for line in lines)
#     print(lines)

# print(f"Michelle Obama speech - Lines: {num_lines}, Words: {num_words}")

# # iii. Read donald_speech.txt file and count number of lines and words

# with open('./questions/donald_speech.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     num_lines = len(lines)
#     num_words = sum(len(line.split()) for line in lines)
#     print(lines)
# print(f"Donald speech - Lines: {num_lines}, Words: {num_words}")

# # iv. Read melina_trump_speech.txt file and count number of lines and words
# with open('./questions/melina_trump_speech.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     num_lines = len(lines)
#     num_words = sum(len(line.split()) for line in lines)
#     print(lines)
# print(f"Melina Trump speech - Lines: {num_lines}, Words: {num_words}")


# # 2. Read the countries_data.json data file in data directory, create a function that finds the ten most 
# # spoken languages

# import json

# # step 1: read the countries_data.json file
# with open('./questions/countries_data.json', 'r', encoding='utf-8') as f:
#     countries_data = json.load(f)

# # step 2: create a function that finds the ten most spoken languages 
# def most_spoken_Language(counties_data, top_n):
        
#     # Count the number of countries that speak each language
#     lang_count = {}

#     # step 3 : loop through the countries data and count the languages
#     for country in countries_data:

#         # step 4: loop through the languages of each country and count the languages
#         for language in country['languages']:

#             # step 5: if the language is already in the lang_count dictionary, increment its count, 
#             # otherwise add it to the dictionary with a count of 1
#             if language in lang_count:
#                 lang_count[language] += 1
#             else:
#                 lang_count[language] = 1

#     # step 6: sort the languages by count in descending order and return the top n languages
#     sorted_lang = sorted(lang_count.items(), key=lambda x: x[1], reverse=True)

#     # step 7: return the top n languages
#     return sorted_lang[:top_n]


# # step 8: call the function and print the result
# top_languages = most_spoken_Language(countries_data, 10)

# # step 9: print the top 10 most spoken languages
# print("Top 10 most spoken languages:")
# for language, count in top_languages:
#     print(f"{language}: {count} countries")


# # 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

# import json

# # step 1: read the countries_data.json file
# with open('./questions/countries_data.json', 'r', encoding='utf-8') as f:
#     countries_data = json.load(f)

# # step 2: create a function that creates a list of the ten most populated countries
# def most_populated_countries_with_country_name(counties_data, top_n):
        
#     # step 3: sort the countries by population in descending order and return the top n countries
#     sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)

#     # step 4: return the top n countries
#     return sorted_countries[:top_n]

# # step 5: call the function and print the result
# top_countries = most_populated_countries_with_country_name(countries_data, 10)

# # step 6: print the top 10 most populated countries with their population
# print("Top 10 most populated countries:")

# for country in top_countries:
#     print(f"{country['name']}: {country['population']}")
    


# # Q3. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
# import re

# incoming_emails = []

# with open('./questions/email_exchanges_big.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         if line.startswith('From:'):
#             email = re.findall(r'\S+@\S+', line)
#             if email:
#                 incoming_emails.append(email[0])

# print(incoming_emails)


# # Q4. Find the most common words in the English language. Call the name of your function 
# # find_most_common_words, it will take two parameters - a string or a file and a positive integer, 
# # indicating the number of words. Your function will return an array of tuples in descending order. 

import string
from collections import Counter

# def find_most_common_words(text, n):
#     # Remove punctuation and convert to lowercase
#     translator = str.maketrans('', '', string.punctuation)
#     cleaned_text = text.translate(translator).lower()

#     # Split the text into words
#     words = cleaned_text.split()

#     # Count the frequency of each word
#     word_counts = Counter(words)

#     # Get the most common words
#     most_common = word_counts.most_common(n)

#     return most_common

# # Example usage
# text = "Hello world! Hello everyone. Welcome to the world of Python programming."
# n = 3
# most_common_words = find_most_common_words(text, n)
# print(most_common_words)

# Q5. Use the function, find_most_frequent_words to find:
        # i. The ten most frequent words used in Obama's speech
        # ii. The ten most frequent words used in Michelle's speech
        # iii. The ten most frequent words used in Trump's speech
        # iv. The ten most frequent words used in Melina's speech

# Q6. Write a python application that checks similarity between two texts. It takes a file or a string 
# as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity 
# between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function 
# to clean the text(clean_text), function to remove support words(remove_support_words) and finally to 
# check the similarity(check_text_similarity). List of stop words are in the data directory.



import string
from questions.stop_words import stop_words

def clean_text(text_or_file):
    try:
        with open(text_ot_file, 'r', encoding='utf-8') as f:
            text = f=read()
    except:
        text = text_or_file

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    return text.split()

def remove_stop_words(words):
    return [word for word in words if word not in stop_words]

def check_text_similarity(text1, text2):
    words1 = remove_stop_words(clean_text(text1))
    words2 = remove_stop_words(clean_text(text2))

    set1 = set(words1)
    set2 = set(words2)

    similarity = len(set1 & set2) / len(set1 | set2)

    return similarity


similarity = check_text_similarity(
    "./questions/michelle_obama_speech.txt",
    "./questions/melina_trump_speech.txt"
)

print("Similarity:", similarity)
    

