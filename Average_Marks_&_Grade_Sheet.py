maths=int(input("Enter your marks in Mathematics:"))
physics=int(input("Enter your marks in Physics:"))
ppl=int(input("Enter your marks in PPL:"))
wwd=int(input("Enter your marks in WWD:"))
lc=int(input("Enter your marks in LC:"))
average=(maths+physics+ppl+wwd+lc)/5
print("Your average marks are:",average)
if average>=91 and average<=100:
    print("You got O grade")
if average>=81 and average<91:
    print("You got A+ grade")
if average>=71 and average<81:
    print("You got A grade")
if average>=61 and average<71:
    print("You got B+ grade")
if average>=51 and average<61:
    print("You got B grade")
if average>=41 and average<51:
    print("You got C+ grade")
if average>=35 and average<41:
    print("You got C grade")
if average<35:
    print("You failed the semester!")