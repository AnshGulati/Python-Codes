'''
Python has a set of built-in math functions, including an extensive math 
module, that allows you to perform mathematical tasks on numbers.
'''

import math

# sqrt gives square root of a number.
x= math.sqrt(64)
print(x)

#pow is an exponential function.
y=math.pow(x,2)
print(y)

# ceil() method rounds a number upwards to its nearest integer.
p=math.ceil(1.7)
print(p)
# floor() method rounds a number downwards to its nearest integer.
q=math.floor(1.7)
print(q)

# pi constant, returns the value of PI (3.14...).
import math
pie = math.pi
print(pie)

# degrees to radians conversion.

angle=math.radians(30)
print(angle)
# sin , cos, tan ratios for the angle of 30 degrees (0.5235987755982988 radians).
'''
These take values in radians.
'''
print(math.sin(angle))
print(math.cos(angle))
print(math.tan(angle))

# log10() method returns the base-10 logarithm of the given number. We can also use log2 with 2 as a base.

number=math.log10(2)
print(number)