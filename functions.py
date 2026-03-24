"""
A function is a block of code that only runs when it's called.
We can pass data to a functon using parameters/arguments, and they can return data.

def function_name(parameters):
    # Code block (indented)
    #Perform actions using parameters.
    return value # optional

"""
# Simple function without parameters:
def my_function():
    print("This is my function.") # This runs when the function is called.

my_function() # Here, I am calling the function.

def other_function():
    print("This is another function.")

other_function() # Here, I am calling the function. The same function can be called multiple times as needed.
# Function with Parameters:

def print_full_name(first_name, middle_initial, last_name):
    print(f"The name is: {first_name} {middle_initial} {last_name}")

print_full_name("Sergio", "J.", "Gonzalez") 
       

# Functions that return values:
# Instead of just printing, fucntions can send back (return) data.

def get_full_name(fname, lname):
    return f"{fname} {lname}" # Sends back the full name as text.

# Store the returned value in a variable:
full_name = get_full_name("Sergio", "Gonzalez")
print(full_name)

# Functions with Default Parameters:
# A default parameter means the function will use that argument value.
# If no arguemnt is provided when calling the function.

def greet(name="student"):
    print(f"Hello, {name}!  Welcome to class!")

# Calling with no argument -> use the default.
greet()

#Calling with an argument -> overrides the default.
greet("Sergio")



