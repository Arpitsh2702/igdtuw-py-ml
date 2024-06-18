#Write a python program that calculates the sum of the digits of a given number .

num1 = int(input("enter  number"))
sum = 0
while num1 > 0:
    a = num1%10  
    sum = sum + a
    num1 = num1//10
print("\n sum of digit given num1 = %d" %sum)
 
