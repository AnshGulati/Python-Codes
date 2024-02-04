#Using functions,re-write and execute Python program to:
#1.Add natural numbers upto n where n is taken as an input from user.
#2.Print Fibonacci series till nth term (Take input from user).
def sum_natural_numbers(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum

def fibonacci_series(n):
    if n<=0:
        print("Invalid input! Please enter a positive integer.")
    elif n==1:
        print("Fibonacci series up to",n,"term:")
        print(0)
    else:
        print("Fibonacci series up to",n,"terms:")
        a,b=0,1
        print(a,b,end=" ")
        for i in range(2,n):
            c=a+b
            print(c,end=" ")
            a,b=b,c
        print()

n=int(input("Enter a positive integer: "))
print("Sum of natural numbers up to", n,"is",sum_natural_numbers(n))
fibonacci_series(n)


#2.
def check_baggage(baggage_weight):
    if baggage_weight>=0 and baggage_weight<=40:
        return True
    else:
        return False
def check_immigration(expiry_year):
    if expiry_year>=2030 and expiry_year<=2050:
        return True
    else:
        return False
def check_security(noc_status):
    if noc_status=='valid' or noc_status=='VALID':
        return True
    else:
        return False
def traveler(traveler_id,traveler_name,baggage_weight,expiry_year,noc_status):
    if check_baggage(baggage_weight) and check_immigration(expiry_year) and check_security(noc_status):
        print("Traveler with ID",traveler_id,"and name",traveler_name,"is allowed to enter the flight.")
    else:
        print("Traveler with ID",traveler_id,"and name",traveler_name,"is not allowed to enter the flight.")
#Sample input values
traveler_id=1001
traveler_name="Jim"
baggage_weight=35
expiry_year=2019
noc_status="valid"
#Invoke the traveler function with sample input values
traveler(traveler_id,traveler_name,baggage_weight,expiry_year,noc_status)


#3.
lst=[('V',62),('VI',68),('VII',72),('VIII',70),('IX',74),('X',65)]
max_val=max(lst,key=lambda x:x[1])[1]
min_val=min(lst,key=lambda x:x[1])[1]
print("Maximum and minimum values of the said list of tuples:({},{})".format(max_val,min_val))
