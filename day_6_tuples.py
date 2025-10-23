'''
Tuples
A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

tuple(): to create an empty tuple
count(): to count the number of a specified item in a tuple
index(): to find the index of a specified item in a tuple
operator: to join two or more tuples and to create a new tuple

'''

# 1. Creating an empty tuple

# syntax
empty_tuple = ()

#  using the tuple constructor
empty_tuple = tuple()


# 2. tuples with initial values

fruits = ('Orange', 'Mango', 'Grapes', 'Banana', 'Pineapple')

# 3. We use the len() method to get the length of a tuple.

len(fruits)

# 4. accessing tuples using indexing

first_item = fruits[0]
second_item = fruits[1]
last_item = len(fruits) - 1
last_index = fruits[last_item]

# 5. Negative indexing Negative indexing means beginning from the end, -1 refers to the last item, 
#    -2 refers to the second last and the negative of the list/tuple length refers to the first item.

last_fruit = fruits[-1]
second_last_fruit = fruits[-2]


# 6. Slicing tuples
# We can slice out a sub-tuple by specifying a range of indexes where to 
# start and where to end in the tuple, the return value will be a new tuple with the specified items.

all_item = fruits[0:5] # print all item
all_item = fruits[0:]  # print all item
middle_item = fruits[1:3] # print doesn't added 3index

# 7. Slicing using Range of Negative Indexes

fruits = ('Orange', 'Mango', 'Grapes', 'Banana', 'Pineapple')
all_fruits = fruits[-5:]
mango_Grapes = fruits[-4:-2]
Grapes_to_rest = fruits[-3:]

# 8. We can change tuples to lists and lists to tuples.
#    Tuple is immutable if we want to modify a tuple we should change it to a list.

fruits = ('Orange', 'Mango', 'Grapes', 'Banana', 'Pineapple')
print("Original Tuple Value : ", fruits)
fruits = list(fruits)
fruits[0] = 'Apple'
print("List Value adding one item : ", fruits)
fruits = tuple(fruits)
print("After Changing list to tuple : ", fruits)


# 9. We can check if an item exists or not in a tuple using in, it returns a boolean.

fruits = ('Orange', 'Mango', 'Grapes', 'Banana', 'Pineapple')
print('Orange' in fruits)
print('Watermelon' in fruits)


# 10. We can join two or more tuples using + operator

fruits = ('Orange', 'Mango', 'Grapes', 'Banana', 'Pineapple')
vegetable = ('Ladyfinger', 'Potato', 'tomato', 'onion', 'Brigal')
fruits_vegetable = fruits + vegetable
print(fruits_vegetable)

# 11. It is not possible to remove a single item in a tuple but 
#      it is possible to delete the tuple itself using del.

fruit = ('orangle', 'mango')
print(fruit)
del fruit
#print(fruit)


# -------------------------------------------------Execrises level 1---------------------------------------


# 1. Create an empty tuple
empty_tuples = ()


# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Komal', 'Nandani', 'Simran', 'sunita', 'Vasanavi')
brothers = ('Vishal', 'Golu', 'Aaditya', 'Ashu', 'Aman')


# 3. Join brothers and sisters tuples and assign it to siblings
Siblings = brothers + sisters
print(Siblings)


# 4. How many siblings do you have?
print(f"Total Numbers of Sbiling is {len(Siblings)}")


# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Siblings = list(Siblings)
Siblings.append('Father')
Siblings.append('Maa')
Siblings = tuple(Siblings)
family_members = Siblings
print(f"Total family member is {len(family_members)} and Family member name is {family_members}")


# -----------------------------------Exercises level 2 ------------------------------------------------


# 1. Unpack siblings and parents from family_members

*siblings, father, mother = family_members
print("Sbilings : ", siblings)
print("Father : ", father)
print("Mother : ", mother)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('Orange', 'Mango', 'Grapes', 'Banana', 'Pineapple')
vegetable = ('Ladyfinger', 'Potato', 'tomato', 'onion', 'Brigal')
animal = ('Butter', 'Milk', 'Paneer')
food_stuff = fruits + vegetable + animal
print(food_stuff)
print(type(food_stuff))


# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff = list(food_stuff)
print(type(food_stuff))

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.


middle = len(food_stuff) // 2
food_stuff_tp = food_stuff[middle]
print("Middle index value of list food stuff : ", food_stuff_tp)

food_stuff = tuple(food_stuff)
mid = len(food_stuff) // 2
food_stuff_tp = food_stuff[mid]
print("Middle index value of tuples food stuff : ", food_stuff_tp)


# 5. Slice out the first three items and the last three items from food_staff_lt list

food_stuff = list(food_stuff)
food_stuff_ft = food_stuff[0:3]
print("first three item : ", food_stuff_ft)
food_stuff_lt = food_stuff[-3:]
print("Last three item from food stuff : ", food_stuff_lt)

# 6. Delete the food_staff_tp tuple completely

print("before deleing : ", food_stuff_tp)
del food_stuff_tp
#print("After deleting : ", food_stuff_tp)


# 7. Check if an item exists in tuple:

# Suppose you have a tuple
food_stuff = ('apple', 'banana', 'mango', 'milk', 'bread', 'egg')

# Check if an item exists
item_to_check = 'mangos'

if item_to_check in food_stuff:
    print(f"'{item_to_check}' exists in the tuple.")
else:
    print(f"'{item_to_check}' does not exist in the tuple.")



