#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

# For Converting the temperature to degree Fahrenheit .

celsius_1 = float(input("Temperature value in degree Celsius: " ))  
Fahrenheit_1 = (celsius_1 * 1.8) + 32  
      
print('The %.2f degree Celsius is equal to: %.2f Fahrenheit'  
      %(celsius_1, Fahrenheit_1))  

Fahrenheit_1 = float( input("Temperature value in degree Fahrenheit: " ))  
  
# For Converting the temperature from degree Fahrenheit to degree Celsius   
 
celsius_1 = (Fahrenheit_1 - 32)  / 1.8  
 
print ('The %.2f degree Fahrenheit is equal to: %.2f Celsius'  
      %(Fahrenheit_1, celsius_1)) 

       