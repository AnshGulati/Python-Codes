#Membership Operator - (in) compares the given two strings

str1=input('Enter the First String: ')
str2=input('Enter the Second String: ')
if str2 in str1:
    print(str2+'Found in the First String.')
else:
    print(str2+'Not found in the First string.')