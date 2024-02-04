# class Animal:
#     def speak(self):
#         print("speaking")

# class Dog(Animal):
#     def speak(self):
#         print("Barking")

# d=Dog()
# d.speak()

class Bank:
    def getroi(self):
        return 10
    
class SBI(Bank):
    def getroi(self):
        return 6.5
    
class HDFC(Bank):
    def getroi(self):
        return 7.5
    
b1=Bank()
b2=SBI()
b3=HDFC()
print("Bank Rate of Interest: ",b1.getroi())
print("SBI Rate of Interest: ",b2.getroi())
print("HDFC Rate of Interest: ",b3.getroi())