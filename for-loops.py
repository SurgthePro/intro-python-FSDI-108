"""
A for-loop in python is a control structure that lets you repeat a block of code for
each item in a sequence (such as, list, string, tuple, range of numbers, etc...)
Example of a for-loop:
for variable in sequence/list/set/dictionary/tuple: (Note: The only two keywords here are: for & in.
# Code block runs for each item in the sequence
"""
# Basic Example (using a list):
fruits = ["apple", "banana", "cherry"]

for fruit in fruits: # This means that for every item in our sequence of items, do the following:
    print(fruit)

for letter in "Sergio": # Here, we are looping through one string.
    print(letter)

print("______________") # This prints a line on the terminal to make it easier to visually separate things.
# range() generates a sequence of numbers.
for x in range(5): # Index by 0 (This applies to integers starting at zero. The argument means you want that quantity of integers.)
    print(x)

# Start and End a Range:
for x in range(2, 6): # This will start on the first integer argument, and will end on the last argument minus one.
    print(x)


 # Step:
for x in range(0, 10, 2): # Here, this looping process starts on the first integer argument, it ends at nine, but skips by 2 (so it begins on 0, then 2, 4, 6, 8, and it stops there because it can on longer skip by 2, or else, it will go past 9).
    print(x)

"""
MINI-CHALLENGE: 
1. Ask the user to enter a number and store it in a variable called "num".
2. Use a for-loop with range(1, 11) to repeat 10 times (from 1 to 10).
3. Inside the loop, multiple num by the current loop value (i). Don't forget to print all this process.
"""

num = int(input("Enter a number: ")) # Step 1
for i in range(1, 11): # Step 2: Since it needs to stop at 10, we need to set it at 11.
    print(f"{num} X {i} = {num * i}") # Step 3: Here, we are doing two things--printing what is happening and doing the math operation.
   