# Accessing elements of Sets
'''
    Set items cannot be accessed by referring to an index, since sets are unordered the items has 
    no index. But you can loop through the set items using a for loop, or ask if a specified value is 
    present in a set, by using the in keyword.
'''
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
    print("banana" in thisset)