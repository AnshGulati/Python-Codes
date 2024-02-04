# Passing parameters into the function

def name(fname):
    print(fname + "Ref")
name("Emil")
name("Tobias")
name("Linus")


def my_function(*kids):
    '''Here * is used so we dont have to define every element'''
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

# Here * is not used so we have to define and initialise every element.
def my_function2(kid1,kid2,kid3):
    print("The youngest child is " + kid2)
my_function2(kid1="Emil" , kid2="Tobias" , kid3="Linus")