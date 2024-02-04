def checkAge(age):
    if age > 18:
        return True
    else:
        return False
age = [5, 11, 16, 19, 24, 42]
adults = filter(checkAge, age)
print(list(adults))
