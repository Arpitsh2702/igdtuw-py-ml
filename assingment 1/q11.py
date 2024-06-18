#Write a python program that generates the first n numbers in the Fibonacci sequence.

n = int(input("enter number "))
a = 0 
b = 1
for i in range(1,n):
    print(a, end="")
    c = a+b 
    a=b
    b=c
