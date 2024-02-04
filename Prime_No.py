#Get a number from user and print number is even/odd and prime/non prime.
n=int(input("enter a number:"))
if n==1:
    print(n,"is not a prime number")
elif n>1:
    for i in range(2,n):
        if(n%i)==0:
            print(n,"is not a prime number")
            break
        else:
            print(n,"is a prime number")
            break
    else:
        print(n,"is not a prime number")
if(n%2==0):
    print(n,"is an even number")
else:
    print(n,"is an odd number")