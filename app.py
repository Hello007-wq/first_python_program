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

print("Hello World")