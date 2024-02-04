#Demonstrate the concept of closure function
def greet(name):
    def display_name():
        print("hi",name)
    display_name()
greet("john")