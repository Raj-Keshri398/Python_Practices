#=============================== Class and Object ===============================

# Python is an object oriented programming language. Everything in Python is an object, with its properties 
# and methods. A number, string, list, dictionary, tuple, set etc. used in a program is an object of a 
# corresponding built-in class. We create class to create an object. A class is like an object constructor,
# or a "blueprint" for creating objects. We instantiate a class to create an object. The class defines 
# attributes and the behavior of the object, while the object, on the other hand, represents the class.


# Example

num = 10
print(type(num)) # <class 'int'>

name = "Raj"
print(type(name)) # <class 'str'>

boolean = True
print(type(boolean)) # <class 'bool'>

lst = [1, 2, 3]
print(type(lst)) # <class 'list'>

tpl = (1, 2, 3)
print(type(tpl)) # <class 'tuple'>

dict1 = {
    "name" : "Raj",
    "age" : 25
}
print(type(dict1)) # <class 'dict'>

set1 = {1, 2, 3}
print(type(set1)) # <class 'set'>

# ===========================  Creating a Class ====================================

# To create a class, we use the keyword 'class' followed by the name of the class and a colon. 
# The body of the class is indented and contains the attributes and methods of the class. 
# The convention for naming a class is to use CamelCase.

# Example

class Person:
    pass
print(Person) # <class '__main__.Person'>

# ========================== Creating an object ====================================

# To create an object, we instantiate the class by calling the class name followed by parentheses. 

# Example

person1 = Person()
print(person1) # <__main__.Person object at 0x7f8c8c8c8c8c>

# =========================== Class constructor =========================================

# In the examples above, we have created an object from the Person class. However, a class without a 
# constructor is not really useful in real applications. Let us use constructor function to make our 
# class more useful. Like the constructor function in Java or JavaScript, Python has also a built-in init() 
# constructor function. The init constructor function has self parameter which is a reference to the 
# current instance of the class 


# Examples:

class Person:
    def __init__(self, name, age):
        # self allow to attach parameter to the class
        self.name = name
        self.age = age

p = Person("Raj", 25)
print(p.name) # Raj
print(p.age) # 25
print(p) # <__main__.Person object at 0x7f8c8c8c8c8c>

# ===================== Object Methods =====================

# Object methods are functions that are defined inside a class and can be called on an object of that 
# class. They are used to define the behavior of the object. Object methods can access and modify the 
# attributes of the object.

# Example

class Person:
    def __init__(self, firstname, lastname, age, country):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country

    def full_name(self):
        return f"{self.firstname} {self.lastname}"
    
    def person_info(self):
        return f"{self.full_name()} is {self.age} years old. He lives in {self.country}."
    
p = Person("Shivam", "Sinha", 25, "India")
print(p.full_name()) # Shivam Sinha
print(p.person_info()) # Shivam Sinha is 25 years old. He lives in India.


# other example

class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())

# ============================ Method to Modify Class Default Values ==============================

# In the example below, the person class, all the constructor parameters have default values. In addition
# to that, we have skills parameter, which we can access using a method. Let us create add_skill method
# to add skills to the skills list.

class Person: 
    def __init__(self, firstname='kumar', lastname='sinha', age=25, country='India', city='Delhi'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}. his skills are {", ".join(self.skills)}.'
    
    def add_skill(self, skill):
        self.skills.append(skill)
p1 = Person()
print(p1.person_info()) # kumar sinha is 25 years old. He lives in Delhi, India.
print(p1.skills) # []
p1.add_skill('Python')
print(p1.skills) # ['Python']
p1.add_skill('JavaScript')
print(p1.skills) # ['Python', 'JavaScript']
p1.add_skill('Java')
print(p1.skills) # ['Python', 'JavaScript', 'Java']
print(p1.person_info()) # kumar sinha is 25 years old. He lives in Delhi, India. his skills are Python, JavaScript, Java.


# ============================= Inheritance ===============================

# Using inheritance we can reuse parent class code. Inheritance allows us to define a class that inherits all the 
# methods and properties from parent class. The parent class or super or base class is the class which gives all 
# the methods and properties. Child class is the class that inherits from another or parent class. Let us create a 
# student class by inheriting from person class.
print('\n\n')
print('Inheritance Example')
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}. his skills are {", ".join(self.skills)}.'
    
    def add_skill(self, skill):
        self.skills.append(skill)
    
class Student(Person):
    def __init__(self, firstname, lastname, age, country, city, gender, student_id): # constructor of the child class
        super().__init__(firstname, lastname, age, country, city) # super() is used to call the constructor of the parent class

        self.gender = gender # gender is a new attribute that is not in the parent class
        self.student_id = student_id # student_id is a new attribute that is not in the parent class

s = Student('Shivam', 'Sinha', 25, 'India', 'Delhi', 'Male', '12345')
s.add_skill('Python')
s.add_skill('JavaScript')
print(s.person_info()) # Shivam Sinha is 25 years old. He lives in Delhi, India. his skills are Python, JavaScript.
print(s.gender) # Male
print(s.student_id) # 12345   


# ========================= Overriding Parent Method =====================================================

# When we inherit from a parent class, we can override its methods in the child class. Let's see an example:
import random

class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        self.skills = []

    def info(self):
        return f"{self.name} is {self.age} years old> He lives in {self.country}. His skills are {', '.join(self.skills)}."
    
    def add_skill(self, skill):
        self.skills.append(skill)
    
class Student(Person):
    def __init__(self, name, age, country, gender):
        super().__init__(name, age, country)
        self.gender = gender
        self.student_id = self.generate_id()

    def generate_id(self):
        return random.randint(10000, 99999)

    def info(self): # overriding the info method of the parent class
        return f"{self.name} is a {self.gender} student. His Student ID is {self.student_id}. He is {self.age} years old. He lives in {self.country}. His skills are {', '.join(self.skills)}."
    
s = Student('Shivam Sinha', 25, 'India', 'Male')
s.add_skill('Python')
s.add_skill('JavaScript')
print(s.info()) # Shivam is a Male student. His Student ID is 12345. He is 25 years old. He lives in India. His skills are Python, JavaScript.


# ==================================== Exercise =====================================

# Q 1. Python has the module called statistics and we can use this module to do all the statistical calculations. 
# However, to learn how to make function and reuse function let us try to develop a program, which calculates the 
# measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). 
# In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. 
# You can create a class called Statistics and create all the functions that do statistical calculations as methods 
# for the Statistics class. Check the output below.


class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        count = len(self.data)
        return count
    
    def sum(self):
        sum = 0
        for i in self.data:
            sum += i
        return sum
    
    def min(self):
        min = sorted(self.data)[0]
        return min
    
    def max(self):
        return sorted(self.data)[-1]
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()

        if n % 2 == 0:
            median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            median = sorted_data[n//2]
        return median
    
    def mode(self):
        freq = {}
        for x in self.data:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        mode = max(freq, key=freq.get)
        return mode
    
    def variance(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / self.count()
        return variance
    
    def std_dev(self):
        return round(self.variance() ** 0.5, 1)

    def freq_dist(self):
        freq = {}
        for num in self.data:
            freq[num] = freq.get(num, 0) + 1
        total = self.count()
        return sorted([(round((v/total)*100,1), k) for k,v in freq.items()], reverse=True)

    def describe(self):
        print('Count:', self.count())
        print('Sum:', self.sum())
        print('Min:', self.min())
        print('Max:', self.max())
        print('Range:', self.range())
        print('Mean:', self.mean())
        print('Median:', self.median())
        print('Mode:', self.mode())
        print('Variance:', self.variance())
        print('Standard Deviation:', self.std_dev())
        print('Frequency Distribution:', self.freq_dist())

ages = [31,26,34,37,27,26,32,32,26,27,27,24,32,33,27,25,26,38,37,31,34,24,33,29,26]

data = Statistics(ages)
data.describe()    


# Q 2. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has
#  total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a
#  set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description):
        self.incomes.append((amount, description))

    def add_expense(self, amount, description):
        self.expenses.append((amount, description))

    def total_income(self):
        return sum(amount for amount, _ in self.incomes)
    
    def total_expense(self):
        return sum(amount for amount, _ in self.expenses)
    
    def account_balance(self):
        return self.total_income() - self.total_expense()
    
    def account_info(self):
        return (
            f"Account Holder Name : {self.firstname} {self.lastname}\n"
            f"Total Income : {self.total_income()}\n"
            f"Total Expenses : {self.total_expense()}\n"
            f"Account Balance : {self.account_balance()}"
        )
    
p = PersonAccount("Saurabh", "Keshri")

p.add_income(50000, "Salary")
p.add_income(5000, "Freelance")

p.add_expense(10000, "Rent")
p.add_expense(2000, "Food")

print(p.account_info())