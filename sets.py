# Sets are used to store multiple items in a single variable.
# Sets can also be used to perform math set operations like union, intersection, symmetric difference, etc.
# Sets are UNORDERED (and therefore, UNINDEXED), UNCHANGEABLE, and don't allow duplicates.

# Sets are written with curly brackets {}.
fruits = {"apple", "banana", "cherry"}
print (fruits)

# No duplicates are allowed:
fruits = {"apple", "banana", "apple"} # It ignores the duplicates.
print(fruits)

# Check if an item exists:
print("banana"in fruits) #Note: "In" is a keyword. Note: We can't access by index number--only by typing the specific string value in quotes.

# Adding Items:
fruits.add("orange") # We can only add one item at a time--it can add it anywhere on the set.
print(fruits)

# Adding multiple items:
fruits.update(["kiwi", "mango"])
print(fruits)

# Removing items: Note: If item we want to remove is not in the set, this will cause an error, which will break our program--causing it to stop (it will not continue after that--so you want to avoid this.)
fruits.remove("banana")
print(fruits)

# If you aren't sure the item exists, use discard()
fruits.discard("water")
print(fruits)

# Set operations (similar to math).
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2)) # Here, we are combining two sets. (no duplicates will result.) If there are duplicates, they will only be ignored, and no error messages will result.
print(set1.intersection(set2)) # Common elements are only displayed.
print(set1.difference(set2)) # Here, we get only what's different among both.
# Note: You can add additional sets, as such: print(set1.union(set2, set3 ))
"""
MINI CHALLENGE: Party Guest
1. Create two sets:
    - invited_friends = {"Alex", "Sam", "Leo", "Nina}
    - rsvped = {"Nina", "Sam", "Jordan"}
2. Print:
    - Everyone who was invited (union)
    - Everyone who said they're coming (rsvped)
    - Who hasn't replied yet (difference)
3. Add two new names to invited_friends
4. One of the people canceled - remove from rsvped
5. Print how many total confirmed guests are attending.
6. Check if "Leo" is still coming= print a message depending on result.
"""
invited_friends = {"Alex", "Sam", "Leo", "Nina"} # Step 1a
rsvped = {"Nina", "Sam", "Jordan"} # Step 1b
print(invited_friends.union(rsvped)) # Step 2a
print(rsvped) # Step 2b
print(invited_friends.difference(rsvped)) # Step 2c
invited_friends.update(["Sergio", "Lucy"]) # Step 3
print(invited_friends)
rsvped.remove("Nina") # Step 4
print(rsvped) # Step 5
if "Leo" in rsvped: # Step 6
    print("Leo is coming.")
else:
    print("Leo is not coming.")

# Note: Because of the limitations of sets as specified on line 3, I personally don't find "sets" to be of much use/practicality.                 
                   