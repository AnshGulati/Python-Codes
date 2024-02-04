#if we put 0 , nothing or white space then it will be FALSE
print(bool())
print(bool(0))
print(bool(  ))

#anything else will be TRUE and white space in double quotes is also TRUE
print(bool("Hello"))
print(bool(1))
print(bool("  "))

#depends whether TRUE or FALSE
print(bool(10<9))
print(bool(5>2))
print(bool(9>=8))