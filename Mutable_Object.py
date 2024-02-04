# Mutable object can be changed after it is created, and an immutable object can’t.

''' Objects of built-in types like (int, float, bool, str, tuple, unicode) are immutable. 
    Objects of built-in types like (list, set, dict) are mutable.
    But in the newer version of python tuple is also mutable.
'''

# Here both variables are changed.
a = [1,2,3]
b = a
a.append(4)
print (b)
