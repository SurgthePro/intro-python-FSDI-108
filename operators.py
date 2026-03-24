# 1. Arithmetic Operators:

x = 1
y = 2
res = 0

res = x + y
print(res)

res = x + y
print(res)

res = x - y
print(res)

res = x / y
print(res)

res = x * y
print(res)

#2. Assignment Operators - used to assign values to variables.
# = means "put this value inside the (variable)."

x = 5
x += 5
print(x)
x -= 3
x *= 3
x /= 3
print(x)
# 3. Comparison Operator
# Used to campare two values.
# same as if-else

# == (equal to), != (not equal), < > (less/greater than), <= >=

#4. Logical Operator: Used to combine conditional statements.
# Used with booleans True/False

x = 3
y = 10
z = 3
print (x == y and y ==z) # False, becaue both conditions must be true.
print(x == y or y == z) # False, because at least one must be true.
print(not x == y) # not: -> flips True to False (vice-versa)

#5. Identity Operators: Used to compare the objects, not if they're equal.
# But, if they're actually the same object
# is -> checks if two things are the exact same
# is not -> checks if they are NOT the same
x = 3
y = 4
print(x is y)
print(x is not y)

#6. Membership Operator: Used to test if a sequence is presented in an object.
# in -> checks if something exists in a sequence (list)
# not in -> checks if something does NOT exist inside.

x = [1, 2, 3, 4, 5] # This is a list.

print(4 in x)
print(90 in x)
print(9 not in x)


