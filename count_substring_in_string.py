string="ABCDCCDC"
substring="CDC"

count=0

for i in range(len(string)):
    if string[i:i+len(substring)] == substring:
        count+=1

print(count)

'''
    In each iteration of the loop, we use the string slicing notation string[i:i+len(substring)]
    to extract a substring of length equal to the length of the given substring, starting from 
    the current position i. We then compare this substring with the given substring using the 
    equality operator ==. If the two substrings are equal, we increment the count variable. 
'''