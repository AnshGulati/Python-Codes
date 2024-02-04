#1.
n=int(input("enter a number:"))
if n%2==1:
    print("Weird")
elif n%2==0 and 2<=n<=5:
    print("Not Weird")
elif n%2==0 and 6<=n<=20:
    print("Weird")
else:
    print("Not Weird")

#2.
n=int(input("enter the number:"))
for i in range(n):
    print(i**2)

#3.
n=int(input("enter a number:"))
i=1
while i<=n:
    print(i,end="")
    i=i+1
