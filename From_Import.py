'''
    Instead of importing the whole module into the namespace,
    python provides the flexibility to import only the specific
    attributes of a module.This can be done by using from import statement.
'''

from calculation import summation
a=int(input("Enter The First Number"))
b=int(input("Enter The Second Number"))
c=print("Sum" + "=" ,summation(a,b))

# We can import all the modules using * as follows : from calculation import* .

from calculation import *
print(summation(12,23))
print(multiplication(2,3))