# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

# set() Constructor
'''
    It is also possible to use the set() constructor to make a set
'''
thisset = set(("apple", "banana", "cherry"))
print(thisset)

# Add Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add Sets
'''
    To add items from another set into the current set, use the update() method
'''
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)