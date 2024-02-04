#Create a dictionary having name and age, first ask from user how many pairs of name andage user wants to add, then get many number of pairs from user one by one using loop
dict1={}
n=int(input("enter the number of pairs you want: "))
for i in range(n):
    key=input("enter the name:")
    value=int(input("enter the age:"))
    dict1[key]=value

#Now display the pair one by one through loop.
list1=dict1.keys()
for i in list1:
    print("The age of ",i,"is: ",dict1[i])

#Add new pair of name and age through function.
def add(dict):
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    dict1[name] = age

print("\nAdding a new pair: ")
add(dict1)
print("Updated dictionary is: ", dict1)

#Delete pair of name and age through function.
def delete(dict):
    name = input("Enter the name to be deleted: ")
    del dict1[name]

print("\nDeleting a pair: ")
delete(dict1)
print("Updated dictionary is: ", dict1)

#Update age corresponding to a name.
name = input("\nEnter the name to be updated: ")
age = int(input("Enter the new age: "))
dict1[name] = age
print("Updated dictionary is: ", dict1)
