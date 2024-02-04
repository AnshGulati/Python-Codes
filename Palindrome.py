# Write a program to check if a string entered is symmetric, palindrome or both

def palindrome(string):
    length = len(string)
    mid = (length-1)//2
    start = 0
    end = length-1
    while(start <= mid):
        if string[start] == string[end]:
            start+=1
            end-=1
            ans = 1
        else:
            ans = 0
            break
    if ans == 1:
        print("The given string is a palindrome")
    else:
        print("The given string is not a palindrome")

def symmetric(string):
    length = len(string)
    if length % 2:
        mid = length//2+1
    else:
        mid= length//2
    start = 0
    end = mid
    while(start < mid and end < length):
        if (string[start] == string[end]):
            start = start+1
            end = end+1
            ans = 1
        else:
            ans = 0
            break
    if ans == 1:
        print("The given string is symmetrical")
    else:
        print("The given string is not symmetrical")

string = input("Enter a string: ")
palindrome(string)
symmetric(string)