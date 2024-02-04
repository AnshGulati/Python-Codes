# Here Double quotes is present inside external double quotes Hence it is a syntax error.

''' str = "They said, "Hello what's going on?""
print(str)'''

# The solution to this is backslash(\) which denotes escape sequence.

str1= 'They said, "What\'s going on ?"'
print(str1)

str2= "They said, \"What's going on?\""
print(str2)