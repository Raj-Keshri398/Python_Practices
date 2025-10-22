# 1. Declare an empty list
lst = list()
lst = []


# 2. Declare a list with more than 5 items
fruits = ['Orange', 'Banana', 'Mango', 'Grapes', 'Watermelon']


# 3. Find the length of your list
print(len(fruits))


# 4. Get the first item, the middle item and the last item of the list
print("First Index Item of the list : ", fruits[0])
m = len(fruits) // 2
print("Middle Index item of the list : ", fruits[m])
print("Last Index Item of the list : ",fruits[len(fruits) - 1])


# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
lst_mixed_datatype = ['Shivam', 25, "5'7", 'Single', 'Bangalore']


# 6. Declare a list variable named it_companies and assign initial values
#     Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']


# 7. Print the list using print()
print(lst_mixed_datatype)
print(it_companies)


# 8. Print the number of companies in the list
print("Number of companies in it_companies list : ", len(it_companies))


# 9. Print the first, middle and last company
print("First Index value : ", it_companies[0])
m = len(it_companies) // 2
print("Middle Index Value : ", it_companies[m])
print("Last Index Value : ", it_companies[-1])


# 10. Print the list after modifying one of the companies

print(it_companies)
it_companies[4] = 'infosys'
print(it_companies)

#11. Add an IT company to it_companies

it_companies.append('Tcs') # adding the item using append()
print(it_companies)

it_companies.extend(['Dotplus', 'Zoho']) # adding the more item using extend()
print(it_companies)

#12 Insert an IT company in the middle of the companies list


it_companie = ['Facebook', 'google', 'IBM', 'Oracle', 'Amazon']

it_companie.insert(3, 'CodeBucket')  # add the item using insert()
print(it_companie)

it_companie[3:3] = ['Microsoft', 'Apple'] # add the item using slicing
print(it_companie)

it_companie.extend(['abs', 'bcd']) # add the item using extend 
print(it_companie)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)

index = it_companie.index('google')
print(index)
it_companie[index] = it_companie[index].upper() # first know the index of the item then change the upper case
print(it_companie)

# 14. Join the it_companies with a string '#;  '

joined_companie = '# '.join(it_companie)
print(joined_companie)

# 15. Check if a certain company exists in the it_companies list.

company = 'Facebooks'

if company in it_companie:
    print(f"{company} exist in the list")
else:
    print(f"{company} doest exist in the list")

# 16. Sort the list using sort() method

it_companie.sort()
print(it_companie)

# 17. Reverse the list in descending order using reverse() method
it_companie.sort(reverse=it_companie)
print(it_companie)

# 18. Slice out the first 3 companies from the list
it_company = ['Facebook', 'google', 'IBM', 'Oracle', 'Amazon']

first_three = it_company[0:3]
print("First Three companies : ", first_three)

# 19. Slice out the last 3 companies from the list
last_three = it_company[-3:]
print("Last Three companies : ", last_three)


# 20. Slice out the middle IT company or companies from the list
n = len(it_company)
middle2 = n // 2
middle_comapines = it_company[middle2]
print(middle_comapines)


# 21. Remove the first IT company from the list
del it_company[0]
print(it_company)


# 22. Remove the middle IT company or companies from the list
del it_company[middle2]
print(it_company)


# 23. Remove the last IT company from the list
it_company.pop()
print(it_company)


# 24. Remove all IT companies from the list
it_company.clear()
print(it_company)


# 25. Destroy the IT companies list
#del it_company
#print(it_company)

# 26. Join the following lists:

    # * front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    # * back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)


# -------------------------------------- Exercises level 2 ----------------------------------------

# The following is a list of 10 students ages:
        #  * ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Sort the list and find the min and max age

ages.sort()
m = max(ages)
n = min(ages)
print("Sorted ages : ", ages)
print("max Value : ", m)
print("min value : ", n)

# 2. Add the min age and the max age again to the list

ages.append(m)
ages.append(n)
print(ages)

# 3. Find the median age (one middle item or two middle items divided by two)
ages.sort()
length = len(ages)
m1 = length // 2 - 1
m2 = length // 2
medium = (ages[m1] + ages[m2]) / 2
print("medium/ Average Age : ", medium)

# 4. Find the average age (sum of all items divided by their number )

ages.sort()
s = len(ages)

total = sum(ages)
print("Sum of age : ", total)

average = total / s
print("Average age : ", average)

tot = 0
for age in ages:
    tot += age
print(tot)

# 5. Find the range of the ages (max minus min)
range = (m - n) // 2
print("Range : ", range)


# 6. Compare the value of (min - average) and (max - average), use abs() method

ages = [22, 23, 24, 25, 15, 17, 19, 28, 30, 26, 25]

n = len(ages)
total = sum(ages)
minimum = min(ages)
maximum = max(ages)
average = total / n

min_diff = abs(minimum - average)
max_diff = abs(maximum - average)

print("Average : ", average)
print("Minimum diffrence using abs() method : ", min_diff)
print("Maximum difference using abse() method : ", max_diff)



# --------------------------------------- level 3 -------------------------------------------

# 1. Find the middle country(ies) in the countries list


# import the countries list
from countries import countries

# total number of countries
n = len(countries)

# find the middle country from the countries list
if n % 2 != 0:
    # odd number countries
    middle_country = countries[n // 2]
    print("Middle Country: ", middle_country)
else:
    # even number countries
    middle_countries = countries[n // 2 - 1 : n // 2 + 1]
    print("Middle Countries : ", middle_countries)


# loop through list with index
for index, country in enumerate(countries):
    if "India" in country:   # search dynamically
        print(f"Country: {country}, Index: {index}")
        break  # stop after first match





# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.


n = len(countries)
mid = (n + 1) // 2

first_half = countries[:mid]
second_half = countries[mid:]

print("First half:", first_half)
print(" ")
print("Second half:", second_half)



# 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

country_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

#unpack 

country1, country2, country3, *scandic_countries = country_list

print("country1 :", country1)
print("country2 :", country2)
print("country3 :", country3)
print("Scandic Countries :", scandic_countries)