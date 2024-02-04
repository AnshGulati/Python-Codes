'''
The dir() function returns a sorted list of names defined in the passed module.
This list contains all the sub-modules, variables and functions defined in this module.
'''

import datetime
List = dir(datetime) 
print(List)


import calculation
allfunctions= dir(calculation)
print(allfunctions)