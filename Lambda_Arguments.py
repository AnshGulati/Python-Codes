#Default argument
add = lambda x, y=3, z=4: x+y+z
print(add(2))

# Variable list of arguments (*args)
add = lambda *args: sum(args)
print(add(2,3,5,7))

#Variable list of keyword arguments (**args)
add = lambda **kwargs: sum(kwargs.values())
print(add(x=2, y=3,z=3,f=8))

