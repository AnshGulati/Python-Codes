# If the number of keyword arguments is unknown, add a double ** before the parameter name

def child(**kid):
    print("His name is " + kid["fname"])
child(fname = "T" , lname= 'R')

