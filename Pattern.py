num = 1
for i in range (1, 11):
    for j in range(1, i+1):
        print(i*num, end=" ")
        num+=1
    num=1
    print()