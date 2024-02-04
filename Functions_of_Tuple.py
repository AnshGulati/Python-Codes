#Print the number of items in the tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Lists Concatenation(+)
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)

# Repetition(*)
tuple=("Hi", 'Hello')
print(tuple[0]*4)

# Membership(in)
nos=(1,2,3,4,5)
print(3 in nos)

# Iteration
fruit=("Banana", "Apple" , "Grapes")
for x in fruit:
    print(x)

#count() method returns the number of times a specified value appears in the tuple.
numbers = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = numbers.count(5)
print(x)

# The index() method finds the first occurrence of the specified value.(raises an exception if the value is not found.)
x = numbers.index(7)
print(x)