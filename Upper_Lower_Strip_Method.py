a = "Hello, World!"
b = "    Hello, World!    "

#The upper() method returns the string in upper case:
print(a.upper())

#The lower() method returns the string in lower case:
print(a.lower())

#The strip() method removes any whitespace from the beginning or the end:
print(b.strip())

#The replace() method replaces a string with another string:
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
print(a.split(","))
print(a.split("o"))
