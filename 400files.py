#Variables are names given to values in programming language
#They typically allow you to store and manipulate data in a program.
#Think of variables like labeled containers where you can store a value.
#You can use the variable name to refer to the value stored in a container.
# Examples
#           name = ("Michael") #str 
#           fruits = ("apples", "banana", "water-melon") #str
#           odd_numbers = (1, 3, 5, 7, 9) #int
#           even_numbers = (2, 4, 6, 8) #int
#           rate = (2.24, 0.44) #float
#           pass_rate = (97.8, 79.3, 88.7) #float
#           is_adult = True #bool
#           is_absent = False #bool
#           names = ["Mike", "Arnold", "Andrew"] #list
#           numbers = {1, 2, 3, 4, 5, 6} #set

# In Python, data types are a category of data that can be stored and manipulated.
# Examples of data types
# whole_numbers = ( 1, 2, 3) # (int) data stored are integers
# decimal_numbers = (3.14, -0.5) # (float) data stored are floats popularly known as decimal numbers
# sequence_of_characters = ("Hello") #(str) str short for string, displays a sequence of characters like name etc
# ordered_collection_of_items = ["a", "b", "c", "d", "e"] #(list) a list simply displays a collection of different items
# tuples = (1, 2, 3, "Mike", 4.5) #(tuples) tuples are a data type which are immutable
# dictionary = {"name": "John", "age": 27} #unordered collections of key-value pairs
# sets = {1, 2, 3}, {"a", "b", "c"}
# is_developer = True #Boolean data type and it prints either a true or a false value
# (None) #none data type represents the absence of a value

# integers include all whole numbers, both positive and negative, as well as zero   
# Examples of integers
# 5
# -3
# 0
# 12
# -45
# 98
# -100
# 22
# -7
# 42


# A string is a sequence of characters enclosed within quotes 
# Strings include letters, numbers, symbols and even spaces
# Examples of strings
# "Hello"
# "12345"
# "Python is awesome"
# "Amateur"
# "True"
# "apple"
# "Welcome to the world"
# "abc123"
# "12.34"
# "  "


# Floats are numbers that contain a decimal point or are expressed in scientific notation.
# Examples of floats
# 3.14
# -2.5
# 0.0
# 7.89
# -10.25
# 1.5
# 99.99
# -4.56
# 2.718
# 100.0


# Tuples are ordered collection of elements, and they can contain different types of data e.g integers, strings e.t.c
# Tuples are immutable, meaning their values cannot be changed after they are created
# Examples of tuples
# (1,2,3)
# ('apple', 'banana', 'cherry')
# (5, 'hello', True)
# (100, 200, 300, 400)
# ('cat', 7, 'dog')
# (3.14, 2.71, 1.61)
# ('a', 'b', 'c', 'd')
# (True, False)
# ('red', 42, 'blue')
# (0, 1, 2, 3, 4, 5, 6 )


# Lists can contain different types of elements, such as integers, stings, booleans, floating-point numbers, even other lists as well
# Lists are ordered and mutable, meaning you can change their elements after creation
# Examples of lists
# [1,2,3,4,5]
# ['apple', 'banana']
# [True, False]
# [1.5, 2.3, 3.7]
# ['a', 1, True, 3.5]
# [10, 20, 30, 40, 50]
# [None, 'hello', 42]
# ['dog', 'cat', 'rabbit']
# [3,5,7,9]
# [['apple', 'orange'], [1, 2, 3]]


# A set is an unordered collection of unique elements
# It does'nt allow duplicates, and the order of elements is not preserved
# Sets can obtain different types of elements (integers, strings, booleans e.t.c)
# Union symbol [|] and intersection symbol [&]
# When calling out a set one uses curly braces {} or set constructor ([])
# Examples of sets
# {1,2,3,4,5}
# {10,20,30,40}
# {'apple', 'banana', 'avocado'}
# {3.14, 2.71, 1.61}
# {True, False}
# {1,2,2,3,3,3,3}
# {'a', 'b', 'c', 'd'}
# {0, 5, -1, 2, -3}
# {1, 'hello', 3.14}
# {} #an empty set creates an empty dictionary


# A boolean can only have one of two possible values. True or False
# They are often used in conditional statements and logical operators
# Examples of boolean values
# True
# False
# True and False
# 5 > 3
# 2 == 2
# 3 != 3
# not True
# False or True
# 10 <= 5
# True and True


# A dictionary in python is a collection of key value pairs.
# Each key is unique, and it maps to a value. The keys can be strings, numbers, or other immutable types, while values are str, numbers, lists
# Examples of dictionaries
# person = {"name":"John", "age":20, "city":"harare"}
# student = {"name":"alice", "grade":"a"}
# car = {"brand":"toyota", "model":"corolla"}
# book = {"title":"the genesis of zimbabwe", "author":"dennis richards"}
# fruit_prices = {"apple":2.5, "banana":3.0}
# coordinates = {"x":10, "y":20}
# employee = {"name":"Mike", "position":"manager"}
# organization = {"name":"uncommon", "location":"harare"}
# animal = {"species":"cat", "color":"black"}


# None is a special null like value used to indicate the absence of a value or a null object
# It is often used to represent missing values, default function arguments, or a placeholder
# Examples of the none data type
# None
# x = None
# def my_function(): return None
# y = None
# result = None
# my_list = [1,2,None,4]
# my_dict = {"key_1":None}
# class MyClass: def_init__(self):self.value = None
# print(None) 

# A function is a block of reusable code that is designed to perform a specific task
# Functions help to make a code more organized, modular, and easier to manage
# Think of a function like a machine. You give it input(known as parameters), and it processes it, then gives you an output (return value)
# Examples of functions

# simply function
# def say_hello():
    # print("Hello there")
# say_hello()

# functions with parameters
# def greet_user(name):
    # print(f"Hello,{name}! Nice to meet you.")
# greet_user("Mike")

# functions with parameters and a return value
# def add_numbers(num1,num2):
    # total = num1 + num2
    # return total
# result = add_numbers(5,7)
# print(f"The sum is:{result}")

# functions with a default parameter value
# def greet_default(name = "User"):
    # print(f"Welcome, {name}!")
# greet_default()
# greet_default("Bob")

# functions using keyword arguments
# def describe_pet(animal_type, pet_name):
    # print(f"I have a {animal_type}.")
    # print(f"My {animal_type}'s name is {pet_name.capitalize()}.")
# describe_pet(pet_name="Alice", animal_type="cat")

# function returning a boolean
# def is_even(number):
    # return number % 2==0
# print(f"Is 10 even? {is_even (10)}")
# print(f"Is 7 even? {is_even (7)}")

course='Damn python is hard'
# print(len(course))
# print(course.upper())
# print(course.find("p"))
# print(course.replace('hard', 'Super cool'))
# print('damn' in course)


name=input("What is your name? ")
#print("Hi "+ name)

#name=input("What is your name? ")
#favorite_color=input("What is your favorite color? ")
#print(name + " likes " + favorite_color)

#birth_year=input("Birth year: ")
#age=2025-int(birth_year)
#print(age)

#birth_year=(2004)
#print(type(birth_year))

# name = input("What is your name? ")
# color = input("What is your favorite color? ")
# print(name + " likes " + color)

# birth_year = input("Birth year: ")
# age = 2025 - int(birth_year)
# print(age)

# age = 20
# print(type(age))

# weight_in_lbs = input("What is your body weight in lbs? ")
# weight_in_kgs = int(weight_in_lbs) * 0.45
# print(weight_in_kgs) 

# course = 'Python for Beginners'
# print(course[0:6])

# course = 'Python fo Beginners'
# another = course[:]
# print(another)    #this is how you make a clone

# name = 'Jennifer'
# print(name[1:-1])

##formatted strings 
#first = 'John'
#last = 'Smith'
## message = first + ' [' + last + '] is a coder'
#msg = f'{first} [{last}] is a coder'
#print(msg)

# course = 'Python for Beginners'
# print(course.lower())

# course = 'Python for Beginners'
# print(len(course))

# course = 'Python for Beginners'
# print(course.find('o'))

# course = 'Python for Beginners'
# print(course.upper())

# course = 'Python for Beginners'
# print(course.replace('Beginners', 'Amateurs'))

# course = 'Python for Beginners'
# print('Python' in course)

##Arithmetic operations
# print(10 ** 3) #power
# print(10 % 3) #returns the remainder
# print(10 // 3) #integer
# print(10 / 3) #division
# print(10 + 3) #add
# print(10 - 3) #subtract
# print(10 * 3) #multiply

# x = 10
# x = x + 3
# x += 3 #augmented assignment operator
# print(x)

#x = 10 + 2 * 2 ** 2
#print(x)
#Operator president
#Parenthesis always overrides the order x = (2 + 3) * 10 - 3
# exponentiation 2 ** 3
# multiply or division
# addition or subtraction

#Math functions
# x = 2.9
# print(round(x)) #rounding the number to the nearest whole number
# print(abs(-2.9)) #absolute function converts all numbers to positive ones

# import math #this is how all the math module are imported ...visit your browser ---python 3 math module
# print(math.ceil(2.9))
# print(math.floor(2.9))

#If statements: conditional
#Statement: if it's a hot day (drink plenty of water), otherwise if it's a cold day (wear warm clothes), otherwise (it's a lovely day)
# is_hot = False
# is_cold = False
# 
# if is_hot:
    # print("It's a hot day")
    # print("Drink plenty of water")
# elif is_cold:
    # print("It's a cold day")
    # print("Wear warm clothes")
# else:
    # print("It's a lovely day")
# print("Enjoy your day")

# good_credit = False
# if good_credit:
    # print("Pay $900.000")
# else:
    # print("Pay $950.000")

# price = 1000000
# has_good_credit = True
# 
# if has_good_credit:
    # down_payment = 0.1 * price
# else:
    # down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")

#logical operators
#And Operator
#Used when both conditions must be true.

#age = 25
# Check if age is between 18 and 65
#if age >= 18 and age < 65:
    #print("Eligible for standard work.")
#else:
    #print("Not eligible for standard work based on age range.")


#Or Operator
#Used when at least one condition needs to be true.

#day = "Sunday"
# Check if it's the weekend
# if day.lower() == "saturday" or day.lower() == "sunday":
    # print("It's the weekend!")
# else:
    # print("It's a weekday.")
# Output: It's the weekend!


# Not Operator
# Used to reverse the boolean value of a condition.

# is_raining = False
# Check if it's NOT raining
# if not is_raining:
    # print("Good weather to go outside.")
# else:
    # print("Better take an umbrella.")
# Output: Good weather to go outside.


# Combining and

# has_ticket = True
# is_on_time = True
# Check if allowed to board the train
# if has_ticket and is_on_time:
    # print("Allowed to board.")
# else:
    # print("Cannot board.")
# Output: Allowed to board.


# Combining or

# is_senior = False
# is_student = True
# has_coupon = False
# Check if eligible for a discount
# if is_senior or is_student or has_coupon:
    # print("Eligible for a discount.")
# else:
    # print("No discount applicable.")
# Output: Eligible for a discount.

# Combining and & or (with Parentheses)

# is_admin = False
# is_editor = True
# is_active = True
# Check access rights
# if is_admin or (is_editor and is_active):
    # print("Access granted.")
# else:
    # print("Access denied.")
# Output: Access granted.


# Using not with Comparisons

# status = "completed"
# Check if the task is NOT pending
# if not (status == "pending"):
    # print("Task is no longer pending.")
# else:
    # print("Task is still pending.")



# and with

# items = ["apple", "banana"]
# Check if list exists and is not empty
# if items and len(items) > 0:
    # print(f"The first item is: {items[0]}")
# else:
    # print("The list is empty or does not exist.")
# Output: The first item is: apple


# or with

# user_input_name = "" # User didn't enter anything
# default_name = "Guest"
# Use user_input_name if it's truthy, otherwise use default_name
# username = user_input_name or default_name
# print(f"Welcome, {username}!")
# Output: Welcome, Guest!


# not, and, or

# is_raining = False
# is_warm = False
# has_jacket = True

# if not is_raining and (is_warm or has_jacket):
    # print("Let's go for a walk!")
# else:
    # print("Maybe stay inside.")
# Output: Let's go for a walk!


# name = "Charlie"
# age = 28
# profession = "developer"

# print(f"My name is {name}. I am {age} years old and work as a {profession}.")
# Output: My name is Charlie. I am 28 years old and work as a developer.


# num1 = 15
# num2 = 7

# print(f"The sum of {num1} and {num2} is {num1 + num2}.")
# print(f"The product is {num1 * num2}.")
# print(f"My name in uppercase is {'Alice'.upper()}.")
# Output:
# The sum of 15 and 7 is 22.
# The product is 105.
# My name in uppercase is ALICE.


# pi_value = 3.2
# price = 19.99

# print(f"Pi rounded to 2 decimal places: {pi_value:.2f}")
# print(f"The price is ${price:.2f}")
# Output:
# Pi rounded to 2 decimal places: 3.14
# The price is $19.99


# item = "Apples"
# quantity = 5
# cost = 2.50

# print(f"{'Item':<10} | {'Qty':>5} | {'Cost':>7}") # Header
# print(f"{item:<10} | {quantity:>5} | {cost:>7.2f}")


# large_number = 1234567890
# balance = 5250.75

# print(f"Population estimate: {large_number:,}")
# print(f"Your account balance: ${balance:,.2f}")


# ratio = 0.5
# discount = 0.10

# print(f"Completion rate: {ratio:.1%}") 
# print(f"Discount applied: {discount:%}")
