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



