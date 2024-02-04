pan=input("Enter your pan number: ")
start=pan[0:5]
last=pan[9:10]
mid=pan[5:9]
if len(pan)==10:
    if pan.isupper()==True and last.isalpha()==True and start.isalpha()==True and mid.isdigit()==True:
        print("Valid pan card")
    else:
        print("Invalid pan card")
else :
    print("Invalid pan card")