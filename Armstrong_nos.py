#Print Armstrong numbers in the range 1 to 1000. An Armstrong number is anumber whose sum of the cubes of the digits is equal to the number itself.
for inputt in range(100,500):
    number=inputt
    sum=0
    while number>0:
        d=number%10
        sum=sum+(d**3)
        number=number//10
    if inputt==sum:
        print("Armstrong number: ",inputt)
    else:
        continue