# List items can be accessed by indices which starts from zero 0 for the first element and then continues incrementally.

Values = [ 1, 2, 3, 4, 5, 6]

# Accessing element by index
print(Values[3])

# Negative Indexing
print(Values[-4])

#Replacing using index
Values[0] = 9
print(Values)

# Slicing Operator(:) used to get a subset list or a particular item.

list= [5,10,15,20,25]
print(list[:3])
print(list[::-1])
print(list[1:3])
print(list[:4])
print(list[2:])