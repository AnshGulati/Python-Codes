dt={6:"Sahil",4:"Tarun",5:"Anurag",2:"Ankur",1:"Ravi",3:"Pankaj"}

c1=dict(sorted(dt.items(),key=lambda t:t[0]))
print(c1)

c2=dict(sorted(dt.items(),key=lambda t:t[1]))
print(c2)