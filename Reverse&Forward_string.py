str = "Python"
reversed = ""
forward= ""
for c in str:
	reversed = c + reversed

print(reversed)

for x in str:
	forward=forward + x

print(forward)