#1. and 2.
class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def display(self):
        print("Complex number: ",self.real,"+",self.imag,"i")

# Get the real and imaginary parts of the first complex number from the user
real1=float(input("Enter the real part of the first complex number: "))
imag1=float(input("Enter the imaginary part of the first complex number: "))

# Create the first complex number object
c1=Complex(real1, imag1)

# Create the second complex number object with real part 2 and imaginary part 3
c2=Complex(2, 3)

# Display the two complex numbers
c1.display()
c2.display()


#3.
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)
print("Sum:", c1.real, "+", c1.imag, "i")
print("Difference:", c1.real, "+", c1.imag, "i")
print("Multiplication:", c1.real, "+", c1.imag, "i")
