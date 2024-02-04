# The format() method is the most flexible and useful method in formatting strings.

# Using Curly braces
print("{} and {} both are my best friend".format("Devansh","Abhishek"))
a="{} and {} both are my best friend"
print(a.format("Devansh","Abhishek"))

#Positional Argument
print("{1} and {0} best players ".format("Virat","Rohit"))

#Keyword Argument
print("{a},{b},{c}".format(a = "James", b = "Peter", c = "Ricky"))

# % Modulus in Strings
Integer = 10
Float = 1.290
String = "Devansh"
print("Hi I am Integer ... My value is %d\nHi I am float ... My value is %f\nHi I am string ... My value is %s"%(Integer,Float,String))

# Faster Way of Formatting (Another way without using .format method ).
name="Ansh"
college="UPES"
print(f"{name} study in {college}")