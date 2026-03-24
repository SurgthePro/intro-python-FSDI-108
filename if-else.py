# if: checks a condition (to see if it's true)
# elif: -> (else if) checks another condition, if the first condition is false.
# else -> runs if all other conditions are False.

# if file or variable is mostly types out hit TAB  to automatically
x = 10

if x > 0: 
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Short hand IF Statements
if x > 5:print("x is greater than 5")

# Short-Hand if...else
print("Even") if x % 2 == 0 else print("odd") 

# Nested if statements
if x >0:
    if x < 20:
        print("x is a positive number less than 20")

# Combining Conditions
age = 18

if age >= 18 and age <= 21:
    print("You are between 18 and 21 years old!")
"""
MINI CHALLENGE
1. Ask user to enter today's temp in Fahrenheit and store it in a variable called temp
2. Use if-elif-else statements to classify the temp:
If temp >= 86, print "It's hot outside."
If temp >= 68, print "It's a bit chilly."
If temp >= 50 and temp < 68, print "It's Cold!" (else)
3. Create a variable called jacket:
   Set it to True if temp < 59, otherwise, False.
4. Bonus: If jacket is True, print "Better wear a jacket!", otherwise print "No jacket needed."
"""

temp = input("Enter temp in F units.")
if temp >= 86:
    print("It's hot outside!")
elif temp >= 68:
    print("It's a bit chilly.")
else:
    print("It's cold!")
jacket = True
if temp < 59:
    jacket = true
    print("Better wear a jacket.")
else:
    print("No jacket needed.")

# Python Collections:
