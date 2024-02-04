#Get the age of students in a list and display those students who are above 18, use lambda and filter function.
def checkage(age):
    if age>18:
        return True
    else:
        return False
age=[5,11,16,19,24,42]
adults=filter(checkage,age)
print(list(adults))