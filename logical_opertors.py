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
