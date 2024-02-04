#Generate the patterns given below:
rows=int(input("enter the number of rows:"))
for i in range(0,rows+1):
    for j in range(i):
        print("*",end='')
    print()

n=4
for r in range(1,n+1):
    p=r
    fl=0
    for s in range(1,n-r+1):
        print(" ",end='') 
    for c in range(1,(2*r)):
        print(p,end='')
        if p==1:
            fl=1
        if fl==1:
            p=p+1
        else:
            p=p-1
        
    print()

rows=5
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print("\r")