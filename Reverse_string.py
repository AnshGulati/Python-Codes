#Print a string in reverse.
str = input("Please enter the string: ")
reversed = ""
for i in str:
	reversed = i + reversed
print("\nThe reversed string is:", reversed)