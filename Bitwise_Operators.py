#Bitwise And (&) 1 if it exists in both operands
'''a= 1 0 1 whereas b= 1 1 1 , Hence a&b must be 1 0 1 answer should be 5'''
a=5
b=7
print(a&b)

#Bitwise Or (|) 1 if it exists in neither of operands
'''p= 1 0 0 1 whereas q=  1 1 0 0 , Hence a|b must be 1  1  0 1 answer should be 13 '''
p=9
q=12
print(p|q)

#Bitwise XOR (^) 1 if it is set in one operand but not both
'''x= 1 0 0 1 1 whereas y= 1 1 0 0 1 , Hence x^y must be 0 1 0 1 0 answer should be 10 '''
x=19
y=25
print(x^y)

#Bitwise Complement (~) has the ability of flipping digits
'''Formula = -(n+1) , Here -(8+1) = - 9(Answer) '''
n=8
print(~n)

#Bitwise Left Shift (<<)
''' 120 in bits is 1 1 1 1 0 0 0 , Hence 120<<3 is 1 1 1 1 0 0 0 0 0 0 answer should be 960 '''
num1=120
print(num1<<3)

#Bitwise Right Shift (>>)
''' 120 in bits is 1 1 1 1 0 0 0 , Hence 120>>2 is 0 0 1 1 1 1 0 answer should be 30 '''
print(num1>>2)
