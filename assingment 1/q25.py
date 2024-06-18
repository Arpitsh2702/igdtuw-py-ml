#Write a program that copies the contents of one text file to another.

with open("string1.txt",'r')as firstfile , open("string.txt",'a')as secondfile :
    for line in firstfile:
        secondfile.write(line)
