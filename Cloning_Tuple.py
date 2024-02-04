a=(1, 2, 3, 4, 5)
b=a #Cloning a tuple
print(b)

a=(2,9,4,5)
b=(3,5,7,2)
print("The common elements between the two tuples are: ")
for i in b:
    if i in a:
        print(i, end=" ")