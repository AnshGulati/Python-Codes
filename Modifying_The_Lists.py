# To change the value of a specific item, refer to the index number
thislist=["apple","banana","cherry"]
thislist[1]="blackcurrant"
print(thislist)

''' If you insert more items than you replace, the new items will be 
    inserted where you specified, and the remaining items will move 
    accordingly:
'''
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Delete List Elements
list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)
del list1[2]
print(list1)

# Remove Method deletes the first matching element.
List = [123, 'xyz', 'zara', 'abc', 'xyz']
List.remove('xyz')
print(List)

# Append(Adds the list to last position) , insert(to add at a specific index) , extend(for extending the list rather than merging)
list_1=[1,2,3]
list_2=[1,2,3]
list_3=[1,2,3]
a=[2,3]
list_1.append(a)
list_2.insert(1,a)
list_3.extend(a)
print(list_1)
print(list_2)
print(list_3)
print(len(list_1))
print(len(list_2))
print(len(list_3))