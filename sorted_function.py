#Get the name and age of students from user in a dictionary and return two different dictionary where entry of dictionary are sorted by name and age respectively. Use customized sorted() function
dt={}
dt['23']='asmi'
dt['22']='adi'
dt['12']='nannu'
lst=dt.keys()
print("sorted by age:",sorted(lst))
lst1=dt.values()
print("sorted by name:",sorted(lst1))