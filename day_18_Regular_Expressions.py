# ==================================  Regular Expressions  ==================================

# Regular expressions are a powerful tool for searching and manipulating strings based on specific patterns. 
# They allow you to define complex search patterns using a combination of characters and special symbols.
# A regular expression or RegEx is a special text string that helps to find patterns in data. 
# A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python 
# first we should import the RegEx module which is called re.

# ========================= The re Module ======================

import re
import string

'''
Methods in re Module

To find a pattern we use different set of re character sets that allows to search for a match in a string.

re.match(): searches only in the beginning of the first line of the string and returns matched objects 
            if found, else returns None.           
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string
re.compile: Compiles a regular expression pattern into a regular expression object, which can be used 
for matching using its match(), search() and other methods.

'''

# ---------------------------- Match Method ----------------------------

# syntax

#re.match(substring, string, re.I)
# re.I is used to ignore the case sensitivity of the string. It is an optional parameter.


import re

txt = 'I love to learn python , AI, ML, DL, NLP, CV, Data Science and many more.'
match = re.match('I love to learn', txt, re.I)
print(match)
# Output: <re.Match object; span=(0, 19), match='I love to learn'>

span = match.span()
print(span)
# Output: (0, 19)

start, end = span
print(start, end)
# Output: 0 19

substring = txt[start:end]
print(substring)
# Output: I love to learn


import re

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None

# If the pattern is not found, re.match() returns None. In this case, since the pattern 'I like to teach' 
# does not match the beginning of the string 'I love to teach python and javaScript', the output will be 
# None.

# ---------------------------- Search Method ----------------------------

# syntax
# re.search(substring, string, re.I)
# substring is a pattern, string is the text we look for a pattern , re.I is case ignore flag

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>

# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)

# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105

substring = txt[start:end]
print(substring)       # first


# --------------------- findall Method ---------------------
# syntax
# re.findall(substring, string, re.I)

# re.findall() returns a list of all matches found in the string. If no matches are found, 
# it returns an empty list.

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']


# If we want to find both 'Python' and 'python' we can use the following pattern
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

# We can also use character sets to find both 'Python' and 'python' using a single pattern.
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

# ---------------------- Replacing a Substring ----------------------

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
#I recommend python for a first programming language

match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language


txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)

#I am teacher and I love teaching.
#There is nothing as rewarding as educating and empowering people.
#I found teaching more interesting than any other jobs.
#Does this motivate you to be a teacher?

# ---------------------------------  Splitting Text Using RegEx Split ---------------------------------

txt = '''I love to teach python and javaScript. I also love to teach AI, ML, DL, NLP, CV, Data Science and many more.'''
# re.split() takes a string, splits it at the match points, and returns a list of substrings.
# We can split the text using space as a separator
split = re.split(' ', txt)
print(split)
# ['I', 'love', 'to', 'teach', 'python', 'and', 'javaScript.', 'I', 'also', 'love', 'to', 'teach', 'AI,', 'ML,', 'DL,', 'NLP,', 'CV,', 'Data',
# 'Science', 'and', 'many', 'more.']


txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol



# Writing RegEx Patterns

# To declare a string variable we use a single or double quote. To declare RegEx variable 
# r''. The following pattern only identifies apple with lowercase, to make it case insensitive either
# we should rewrite our pattern or we should add a flag.

print("--------------------------------------------------------------------")

import re

regex_pattern = r'apple'
txt = 'Apple and apple are fruits'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

print("--------------------------------------------------------------------")


# Square Bracket
# Let us use square bracket to include lower and upper case letters in our pattern.
#  We can also use a flag to ignore the case sensitivity of the pattern.

regex_pattern = r'[Aa]pple'
txt = 'Apple and apple are fruits'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

print("--------------------------------------------------------------------")

# Escape character(\) in RegEx

regex_pattern = r'\d'  # \d is used to find digits in a string
txt = 'This regular expression example was made in january 2020.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2', '0', '2', '0']


print("--------------------------------------------------------------------")

# One or more times(+)
regex_pattern = r'\d+'  # \d+ is used to find digits in a string
txt = 'This regular expression example was made in 1 january 2020.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2020']

print("--------------------------------------------------------------------")

# Period(.)

regex_pattren = r'he..'  # . is used to find any character except new line
txt = 'hello world, hey you, helo, heo'
matches = re.findall(regex_pattren, txt)
print(matches)  # ['hello', 'hey', 'helo']

print("--------------------------------------------------------------------")

# Zero or more times(*)

regex_pattern = r'[a].*'  # . any character, * any character zero or more times Apple and banana are fruits In this pattern we are looking for a string that starts with a and followed by any character zero or more times
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']


print("--------------------------------------------------------------------")

# Zero or one time(?)

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''

regex_pattern = r'[Ee]-?mail'  # -? is used to find - zero or one time
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

print("--------------------------------------------------------------------")

# Quantifier in RegEx
# We can specify the length of the substring we are looking for in a text, using a curly bracket. 
# Let us imagine, we are interested in a substring with a length of 4 characters:

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}' # \d{4} is used to find digits with a length of 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,4}' # \d{1,4} is used to find digits with a length of 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']

print("--------------------------------------------------------------------")

# Cart ^

# start

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ is used to find a string that starts with This
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

# Negation

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']

# ---------------------------------------  Questions ---------------------------------------

# 1. What is the most frequent word in the following paragraph?


import re
from collections import Counter

paragraph = '''I love teaching. If you do not love teaching what else can you love.
I love Python if you do not love something which can give you all the capabilities 
to develop an application what else can you love.'''

words = re.findall(r'\w+', paragraph.lower())
freq = Counter(words)

print(freq.most_common(1))

for word, count in freq.items():
    print(f'{word}: {count}')

for word, count in freq.most_common():
    print({word: count})


# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative 
# direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole
#  text and find the distance between the two furthest particles.


print("----------------------------Question 2 ----------------------------------------")

import re
txt = '''The position of some particles on the horizontal x-axis are -4, -12, -3 and -1 
in the negative direction, 0 at origin, 4 and 8 in the positive direction.'''

numbers = re.findall(r'-?\d+', txt)

points = [int(num) for num in numbers]
sorted_points = sorted(points)
distance = sorted_points[-1] - sorted_points[0]

print(f'Points : {points}')
print(f'Sorted Points : {sorted_points}')
print(f'Distance : {distance}')


print("----------------------------Question 3 ----------------------------------------")

# 3. Write a pattern which identifies if a string is a valid python variable

import re

def is_valid_variable(s):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'

    if re.fullmatch(pattern, s):
        return True
    else:
        return False

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname1')) # True


print("----------------------------Question 4 ----------------------------------------")

# 4. Clean the following text. After cleaning, count three most frequent words in the string.

import re

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding 
as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs.
%Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

matches = re.sub(r'[^a-zA-Z\s.]', '', sentence)
print(matches)


