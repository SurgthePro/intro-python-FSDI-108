# Lists are used to store MULTIPLE items in a singular variable.
# Think of a container that can hold many items.
# Lists are written within square brackets. []

my_list = [10, 20, 30, 40, 50]
print(my_list)

# A list can contain different data types.
mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

# You can access list items by their index number.
# (Indexing starts at 0.)

fruits = ["apple", "banana", "cherry"]
print(fruits[0]) # First item: apple.
print(fruits[2]) #last item: cherry.

# You can also use a NEGATIVE index to count from the end.
print(fruits[-1])

# Modifying List Items:
fruits[1] = "mango" # We changed banana to mango.
print(fruits)

# Adding items:
fruits.append("orange") # This adds an item to the end of the list.
print(fruits)

fruits.insert(1, "kiwi") # This adds an item at index 1.
print(fruits)

# Removing items:
fruits.remove("apple") # Removes last item--by value.
print(fruits)

fruits.pop() # Removes only the last item.
print(fruits)

# Looping through a list:
for fruit in fruits:
    print(fruit) # This prints out each and all items in the list named "fruits."

# Check if item exists:
if "mango" in fruits:
    print("yes, mango is in the list.")
else:
    print("No, mango is not in the list.")
# List Length:
print(len(fruits)) # Number of items in list.

# The following code is for assignment 2
# Creating a list (assignment 2a):
activities = ["Introduce Unit", "Teach the Strategies", "Teach the Skills"]
print(activities) # Here, we are printing the list.
# Accessing items by index:
print(activities[0]) # This accesses the first list item.
print(activities[2]) # This accesses the last list item.
print(activities[-1]) # This accesses the last list item.
# Replacing values:
activities[1] = "Teach the vocabulary"
print(activities)
# Removing items (by value or by index)
activities.pop() # Removing an item by index (last item).
print(activities)
# Adding items:
activities.append("Teach the Skill") # Add item at the end of the list.
# Printing the list and its length.
print(f"The Activities list: {activities} has a length of {len(activities)} items.")

#Note: I personally found lists to be more practical/useful.





