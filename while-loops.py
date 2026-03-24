"""
A while loop repeats a block of code as long as a condition is TRUE.
Be careful - if the condition never becomes FALSE, you'll get an INFINITE loop.
 
while condition:
    # cod block runs as long as the condition is True
"""

count = 1

while count <= 5:
    print("Count is: ", count) # This creates an infinite loop.
    count += 1 # Assignment operator which adds 1 and loop stops at =5.

# Using BREAK to stop the loop:
number = 0

while True: # infinite loop
    print(number)
    number += 1
    if number == 3:
        break # stops the loop when it reaches 3.


# Using CONTINUE to SKIP an iteration:
count = 0

while count < 5:
    count += 1
    if count == 3:
        continue   # SKIP (continue just skips the specific condition you give)
    print(count)

print("__________________")
# else with while-loop:
# The else block runs when the loop condition becomes False (not by break).

count = 1
while count < 3:
    print(count)
    count += 1
else:
    print("Loop is finished.")


"""
MINI CHALLENGE: PASSWORD CHECKER
1. Ask the user to enter a password.
2. Check if it's correct (password: "secret123").
3. If it's wrong, print "Wrong! Try again." and ask again.
4. When they enter the correct password, print: "Access granted!"
"""
# password = input("Enter you password: ")
# if password == "secret123":
#     print("Access granted!")
# else:
#     while password != "secret123":
#         print("Wrong! Try again.")
#         break
# password = input("Enter your password: ")

# solution:
password = "" # empty string
while password != "secret123":  # Keeps looping while password is wrong.
    password = input("Enter the password: ")
    if password != "secrtet123": # If wrong
        print("Wrong! Try again.")

# Once they enter the correct password, while-condition becomes flase, so loop stops.
print("Access granted!")

 