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

# 16. What is the last index of the string Coding For All.

print(len(company) -1)

# 17. What character is at index 10 in "Coding For All" string. 

print(company[10]) #output is space

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.

Phrase = "Python For Everyone"

acronym = ''.join(word[0].upper() for word in Phrase.split()) # acronym pick the fir letter of the word
abbreviation = acronym[0].capitalize() + '4' + acronym[-1].upper() # it make the word easy to understand

print(acronym)
print(abbreviation)


# 19. Create an acronym or an abbreviation for the name 'Coding For All'.

acronym2 = ''.join(words[0].upper() for words in company.split())
abbreviation2 = acronym2[0] + 'f4r' + acronym2[-1]

print(acronym2)
print(abbreviation2)

# 20. Use index to determine the position of the first occurrence of C in Coding For All.

position = company.index('C')
print("Position for C in coding for all : ", position)

# 21. Use index to determine the position of the first occurrence of F in Coding For All

position = company.index('F')
print("Position for F in Coding for all : ", position)

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.

text = "Coding For All People."
position = text.rfind('l')
print("Position for l from all index occerences in Coding for all people : ", position)


# 23. Use index or find to find the position of the first occurrence of the word 'because' 
#     in the following sentence: 'You cannot end a sentence with because because because is a conjunction'


sentence = 'You cannot end a sentence with because because because is a conjunction'
position = sentence.index('because')
print("Position of 'because' of the first occurrence using 'index' : ", position)

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 
#     'You cannot end a sentence with because because because is a conjunction'

sentence = 'You cannot end a sentence with because because because is a conjunction'
position = sentence.rindex('because')
print("Position of 'because' of the last occurrence using 'rindex' : ", position)

# 25. Slice out the phrase 'because because because' in the following sentence: 
#     'You cannot end a sentence with because because because is a conjunction'


sentence = 'You cannot end a sentence with because because because is a conjunction.'

start = sentence.index('because')
end = start + len('because because because')

s = slice(start, end)
Phrase = sentence[s]

print(f"Slice out the phrase 'because because because' starting position {start} and ending position {end} is : {Phrase}")


# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 
#     'You cannot end a sentence with because because because is a conjunction'

position = sentence.index('because')
print(f"Position of 'because' first occurrence is at index : {position}")

# 27. Does ''Coding For All' start with a substring Coding?

text = "Coding For All"

result = text.startswith('Coding')
print(result)

# 28. Does 'Coding For All' end with a substring coding?

result = text.endswith('Coding')
print(result)

# 29. '   Coding For All      '  , remove the left and right trailing spaces in the given string.

text = '   Coding For All      '
clean_text = text.strip()
leading_space_removed = text.lstrip()
Trailing_space_removed = text.rstrip()
print("Original : ", repr(text))
print("After : ", repr(clean_text))
print("Leading Space Removed : ", repr(leading_space_removed))
print("Trailing Space Removed : ", repr(Trailing_space_removed))

# 30. Which one of the following variables return True when we use the method isidentifier():
        # * 30DaysOfPython
        # * thirty_days_of_python

var_1 = "30DaysOfPython"
print("'30DaysOfPython' Return False due to start with number : ", var_1.isidentifier())
var_2 = "thirty_days_of_python"
print("'thirty_days_of_python' It Return True : ", var_2.isidentifier())


# 31. The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

labraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join_labraries = '# '.join(labraries)
print(join_labraries)

# 32. Use the new line escape sequence to separate the following sentences.
    # * I am enjoying this challenge.
    # * I just wonder what is next.

sentence = "I am enjoying this challenge. \nI just wonder what is next."
print(sentence)

# 33. Use a tab escape sequence to write the following lines.
    # * Name      Age     Country   City
    # * Asabeneh  250     Finland   Helsinki

heading = 'Name\tAge\tCountry\tCity'
print(heading.expandtabs(12))
data = 'Asabeneh\t250\tFinland\tHelsinki'
print(data)


# 34. Use the string formatting method to display the following:
    # * radius = 10
    # * area = 3.14 * radius ** 2
    # * The area of a circle with radius 10 is 314 meters square.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result)


# 35. Make the following using string formatting methods:
    # * 8 + 6 = 14
    # * 8 - 6 = 2
    # * 8 * 6 = 48
    # * 8 / 6 = 1.33
    # * 8 % 6 = 2
    # * 8 // 6 = 1
    # * 8 ** 6 = 262144

a = 8
b = 6 

print('{} + {} = {}'.format(str(a), str(b), str(a + b)))
print('{} - {} = {}'.format(str(a), str(b), str(a - b)))
print('{} * {} = {}'.format(str(8), str(6), str(8 * 6)))
print('{} / {} = {}'.format(str(8), str(6), str(8 / 6)))
print('{} % {} = {}'.format(str(8), str(6), str(8 % 6)))
print('{} // {} = {}'.format(str(8), str(6), str(8 // 6)))
print('{} ** {} = {}'.format(str(8), str(6), str(8 ** 6)))

