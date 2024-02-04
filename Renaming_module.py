# The syntax to rename a module is: import <module-name> as <specific-name>

import calculation as cal
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("sum " + "=" , cal.summation(a,b))