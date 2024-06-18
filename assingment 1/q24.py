#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.

a = int(input('enter first number :'))
b = input("operator sign: ")
c = int(input('enter second number :'))
if b == "+":
    print(a+c)
elif b == "-":
    print(a-c)
elif b == "*":
    print(a*c)
elif b == "/":
    print(a/c)
else :
    print("enter a vaild operator")