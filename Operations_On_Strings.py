a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Press number which operation you want to perform:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)