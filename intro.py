print("Hello World from Python!") # No semicolons needed.
print(2)
print(5 + 3)
print(True)

# COMMENTS:
# Shortcuts:
# Save File: ctrl + s
# Run last command in terminal: up arrow
""" 

This is a comment.

This is also a comment.
"""

# Variables and Concatenation:
name = "Sergio"
age = 46
print(name)
# Concatenation (joining strings with + symbol):
print("My name is " + name + " and I am " + str(age) +" years old.")

name = "Lucy"
age = 22
middle_name = "Thomas"
found = False # Boolean variable

print(name)
print("My name is  " + name + " and I am " + str(age) +" years old.")
print("Did he show up to class? " + str(found))

# Mini Challenge:
"""
Write a short story using variables.
Steps:
1. Declare and initialize variables (strings and numbers).
2. Use print() and concatenation to tell the story.
3. Run the program in the terminal.
"""
name = "Alberto"
middle_name = "Luis"
last_name = "Ramirez"
money = 100

print("There once was a man named " + name + "and he had " + str(money) + "that he spent on a very expensive hamburger.")

# F-String:
# A Cleaner way to format strings.
work = "sdgku"
job = "" \
"" \
"professor"
print(f"I work at {work} and my job is {job}!")

# Multi-line f-string:
print(f"""My name is {name} {middle_name} {last_name})
      I like python!
      Type indentations
      """)
# Type Function:
print(type(name))
print(type(age))
print(type(found))

# casting ( changing data types):
print(20 + int("20"))
print(20 + age)
print(20 + 2.98)

# User input
# input() let the user type values into the terminal.
user_name = input("Enter your name:")


print(f"Hello, {user_name}!")
print(input("Enter your age: "))
 
# input() always returns a string--even numbers--it reads them as strings.
# Example: converting input to int:
# new_age = int(input("Enter your age: "))
 # print(age + new_age)

#Mini Challenge:
"""
Pizza Calculator
    - Ask how many slices of pizza and how many people
    - Use math operators to calculate slices per person
    -Show to result with an f-string.
"""

user_slice_numbers = int(input("How many slices of pizza do you want?"))
user_person_numbers = int(input("How many people are there?"))
slices_per_person = user_slice_numbers / user_person_numbers
print(slices_per_person)

