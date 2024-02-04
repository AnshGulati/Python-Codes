# Here , we have defined the __del__ method to act as a destructor.

class example:
    def __init__(self):
        print("Object Created!!")

    # Destructor
    def __del__(self):
        print("Object Destroyed!!")

# Creating an object
myObj = example()

# To delete the object explicitly
del myObj