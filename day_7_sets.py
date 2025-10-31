'''
Sets


Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. 
The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and
un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find 
the union, intersection, difference, symmetric difference, subset, super set and disjoint set among 
sets.

'''

st = set() # creating empty set()
st = {'apple', 'orange', 'mango', 'banana'}  # creating set() with item {}
len(st) # knowing the the length of the set

for item in st:
    print(item)

st.add('watermelon') # add 1 item front of the set
print(st)
st.update(['pine', 'cherry', 'grapes']) # add multiple item in set
print(st)

for item in st:
    print(item)

vegetable = {'potato', 'tomato', 'lady finger'}
st.update(vegetable) # add merge/add another  set to one set
print(st)

st.pop() # using pop to remove add item
print(st)

st.remove('lady finger') # using remove to delete paticulat index item
print(st)

vegetable.clear()
print(vegetable) # clear the all data inside the set

del vegetable # delete the vegetable set
#print(vegetable)


fruit_lst = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
print(fruit_lst) # list print all duplicate data
fruit_set = set(fruit_lst)
print(fruit_set) # set remove duplicate data of list and print different data

join_fruit = {'banana', 'orange', 'mango', 'lemon','orange', 'banana'}
join_veg = {'potato', 'tomato', 'lady finger'}
print(len(join_fruit.union(join_veg))) # join the two set using union method

'''
* union() → Returns a new set
* It joins two or more sets
* But does NOT change the original set
* You get a new combined set as the result
'''

A = {1, 2, 3}
B = {3, 4, 5}

result = A.union(B)

print("A:", A)
print("B:", B)
print("Result of union:", result)


'''
* update() → Modifies the original set
* It also joins two or more sets
* But it adds all elements from another set into the first one
* It changes the original set permanently
'''

A = {1, 2, 3}
B = {3, 4, 5}

A.update(B)

print("A after update:", A)
print("B:", B)


# ------ # Intersection returns a set of items which are in both the sets.

num1 = {'item1', 'item2', 'item3', 'item4'}
num2 = {'item2', 'item4'}
print(num1.intersection(num2)) # Intersection returns a set of items which are in both the sets.

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print("Number match in two sets : ",whole_numbers.intersection(even_numbers)) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print("alphabet match in two sets : ",python.intersection(dragon))    # {'o', 'n'}


# -------- # A set can be a subset or super set of other sets:

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}

print("Whole number not a subset of even number : ",whole_numbers.issubset(even_numbers))
print("Whole number is the super subset of even number : ", whole_numbers.issuperset(even_numbers))
print("Even number is sebset of whole Number : ", even_numbers.issubset(whole_numbers))

python = {'p', 'y', 't', 'h', 'o','n'} 
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.issubset(dragon) ) # only two item in python set of dragon set. if all item of python set in drgon then asnwer will show true


# -------- # Checking the Difference Between Two Sets

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print("differnce of python and dragon sets : ",python.difference(dragon))
print("difference of dragon and python sets : ",dragon.difference(python))

# ------- # Finding Symmetric Difference Between Two Sets ------- mathematically: (A\B) ∪ (B\A)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.symmetric_difference(dragon))

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers))

# --------------------
'''
Joining Sets
If two sets do not have a common item or items 
we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.
'''

even_num = {0, 2, 4, 6, 8}
odd_num = {1, 3, 5, 7, 9}
print(even_num.isdisjoint(odd_num)) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon)) # False, because two common item




# --------------------- Exerciese -------------------------------------

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# ----------------------------- Level 1 -----------------------

# 1. Find the length of the set it_companies
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
print(it_companies.add('Tcs'))

# 3. Insert multiple IT companies at once to the set it_companies
print(it_companies.update(['dotplus', 'gei it', 'info era']))

# 4. Remove one of the companies from the set it_companies
print(it_companies.pop())

# 5. What is the difference between remove and discard

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print("After remove:", fruits) # if the element not exist then raise the error
fruits.discard("cherry")
print("After discard:", fruits) # using discard if the element not exist in set then no error throw


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Join A and B

# update() modifies A directly and returns None, so printing it will show None.
A.update(B)
print("Join using update() method :", A)

# union() returns a new set without modifying A or B.
print("Join using union() method :", A.union(B))

# 2. Find A intersection B
print("Intersection of A and B :", A.intersection(B))

# 3. Is A subset of B
print("Is A subset of B :", A.issubset(B))  # not B.issubset(A)

# 4. Are A and B disjoint sets
print("Are A and B disjoint :", A.isdisjoint(B))

# 5. Join A with B and B with A
print("Join A with B :", A.union(B))
print("Join B with A :", B.union(A))

# 6. What is the symmetric difference between A and B
print("Symmetric difference between A and B :", A.symmetric_difference(B))

# 7. Delete the sets completely



# --------------------- Exercises: Level 3 -------------------------------

age = [22, 19, 24, 25, 26, 24, 25, 24]  # list


# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?

ages_set = set(age)

print("List age : ", age)
print("Set age : ", ages_set)

print("length of list age :", len(age))
print("Length of set age : ", len(ages_set))

if len(age) > len(ages_set):
    print("list is bigger , because it allow duplicate value.")
else:
    print("set is bigger or equal")


# 2. I am a teacher and I love to inspire and teach people. 
#    How many unique words have been used in the sentence? Use the split methods and 
#    set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people."
word = sentence.split()
unique_word = set(word)

print("Total words : ", word)
print("Unique Words : ", unique_word)
print("Total length of Unique words : ", len(unique_word))









