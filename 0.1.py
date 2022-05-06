"""Changing type string to list,
thus being able to work character by character of a string"""

s = "Hello World"
l = list(s)
l[0] = "h"
print(l)

"""Changing back to sting, using (.join) method"""

l[0] = "H"
s = "".join(l)
print(s)