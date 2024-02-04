#Create a file (your_name.text) and write about your-self in that file through file handling function. Save at least 10 lines
with open("your_name.txt", "w") as f:
    f.write("My name is ansh.\n")
    f.write("I am a student.\n")
    f.write("I live in karnal.\n")
    f.write("I love listening to music.\n")
    f.write("My favorite food is pizza.\n")
    f.write("I have 1 sibling.\n")
    f.write("I am currently studying in UPES.\n")
    f.write("I am interested in coding and maths.\n")
    f.write("My favorite artist is the weeknd.\n")
    f.write("I am excited to learn more about Python programming!\n")

#Display the content of file (your_name.text) line by line
with open("your_name.txt", "r") as f:
    for line in f:
        print(line)


#Display the number of lines in file (your_name.text) which are not starting with alphabet“A”
with open("your_name.txt","r")as f:
    count=0
    for line in f:
        if not line.startswith("A"):
            count+=1
print("Number of lines not starting with 'A':",count)


#Display the total number of words in file (your_name.text)
with open("your_name.txt", "r") as f:
    words=0
    for line in f:
        words += len(line.split())
print("Total number of words:", words)


#Display the count of those words whose length is less than 4 in file (your_name.text)
with open("your_name.txt","r")as f:
    count=0
    for line in f:
        words=line.split()
        for word in words:
            if len(word)<4:
                count+=1
print("Count of words with length less than 4:", count)