a,b,c=(float(input("Enter a:")),float(input("Enter b:")),float(input("Enter c:")))
print(a,",",b,",",c)
if a<b:
    if a<c:
        print("a is the smallest number")
    else:
        print("c is the smallest number")
if b<a:
    if b<c:
        print("b is the smallest number")
    else:
        print("c is the smallest number")