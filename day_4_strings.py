# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

con_String = 'Thirty', 'Days', 'Of', 'Python'
print(' '.join(con_String))

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

con_string2 = 'Coding', 'For', 'All'
print(' '.join(con_string2))

# 3. Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

# 4. Print the variable company using print().

print(company)

# 5. Print the length of the company string using len() method and print().

print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize()) # it make the first letter of the sentence capital.
print(company.title()) # it make the first letter of the word capital.
print(company.swapcase()) # it make the first letter of the word small and rest are capital.

# 9. Cut(slice) out the first word of Coding For All string.

first_word = company[:6]
print(first_word)

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.

# 1st
if "Coding" in company:
    print("Yes, Coding is Found")
else:
    print("No, Coding is not Found")

#2nd
index = company.find("Coding")
if index != -1:
    print(f"'Coding' found at index {index}")
else:
    print("'coding' not found")

#3rd
try:
    index = company.index("Coding")
    print(f"'Coding' found at index {index}")
except ValueError:
    print("'Coding' not found")


# 11. Replace the word coding in the string 'Coding For All' to Python.

print(company.replace('Coding', 'Python'))

# 12. Change Python for Everyone to Python for All using the replace method or other methods.

text = "Pyhton for Everyone"
print(text)
print(text.replace('Everyone', 'All'))

# 13. Split the string 'Coding For All' using space as the separator (split()) .

print(company.split(' '))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies_list = companies.split(", ")
print(companies_list)

# 15. What is the character at index 0 in the string Coding For All.

print(company[0])


