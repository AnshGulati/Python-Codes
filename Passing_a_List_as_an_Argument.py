# Passing a List as an Argument

def function(food):
    for x in food:
        print(x)
        print(type(food))

fruits=[ "apple" , "Banana" , "Cherry"]
function(fruits)