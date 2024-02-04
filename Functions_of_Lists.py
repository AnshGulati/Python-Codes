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

# Count Method
NewList = [123, 'xyz', 'zara', 'abc', 'xyz']
print(NewList.count("xyz"))

# Sort Method
print(list_1.sort)

#Max & Min Method
list1=[1997,2000]
print(max(list1),min(list1))