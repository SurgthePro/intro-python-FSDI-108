# Tuples are just like lists -- they can store multpile items.
# But!!! They are IMMUTABLE (you can't change them after creation). This means you can't add, remove, or change items in tuples.

my_tuple = ("apple","banana", "cherry")
print(my_tuple)

# Accessing items:
print(my_tuple[0])
print(my_tuple[2])

# Check if item exists:
if "apple" in my_tuple:
    print("Yes, apple is in the tuple.")

# Length of a tuple:
print(len(my_tuple))

# Single item tuple:
# You MUST add a comma at the end or python won't recognize it as a tuple--it will only be recognized as a string.
single = ("grape")
print(type(single)) #This is a string.
tuple = ("water",)
print(type(tuple)) # This is a tuple.

# Nested tuples -- sort of (This is the only way to modify tuples in some way.):
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combine = (tuple1, tuple2)
print(combine) # Note: These two tuples are not fully combined, but this is as close as you get.

"""
MINI CHALLENGE: Travel Bag

1. Create a tuple called "travel_bag" with at least 5 items.
2. Print the SECOND and FORTH items in your bag.
3. Check if "shoes" is in your travel bag -- if it is, print "You're read to walk."
   Otherwise print "You forgot your shoes."
4. Make a new tuple called "essentials" with 3 must-have items.
5. Combine both tuples into one called "final_bag."
6. Print how many total items you now have.
7. Print the last item in your "final_bag."
"""
travel_bag = ("earphones", "toiletries", "underwear", "passport", "book")
print(travel_bag) # Here, I printed the entire tuple: travel_bag.

print(travel_bag[1]) # Here, I printed/accessed the second item of travel_bag.
print(travel_bag[3]) # Here, I printed/accessed the fourth item fo travel_bag.
print(travel_bag[1], travel_bag[3]) # This is a way of printing both with one line of code.
# Here, I'm checking to see if shoes is in travel_bag tuple:
if "shoes" in travel_bag: 
    print("Yes, shoes is in the travel_bag tuple.")
else:
    print("No, shoes is not in my travel_bag tuple.")

essentials = ("passport", "flight-ticket", "phone-and-charger")
print(essentials)
final_bag = (travel_bag, essentials) # This combines both tuples into one single tuple.
print(final_bag) # This prints both tuples as an overall tuple with two smaller tuples inside of it.
final_bag = travel_bag + essentials # This is a different way of combining the two tuples, but here they are displayed as one tuple.
print(final_bag)
print(len(final_bag)) # This counts all items of both tuples
print(len(travel_bag + essentials)) # This also counts all items in both tuples.
print(final_bag[1])
print(final_bag[7])

# Note: At this moment in time, I do not find tuples very useful or practical.



