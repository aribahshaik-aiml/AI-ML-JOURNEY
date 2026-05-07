# Problem 1 - Simple Calculator
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
print("Sum:", num1+num2)
print("Difference:", num1-num2)
print("Multiply:", num1*num2)
print("Division:", num1/num2)

# Problem 2 - Area of Square
side = int(input("side of square: "))
area = side*side
print("Area of square: ", area)

# Problem 3 - AVERAGE
num1 = float(input("enter first number : "))
num2 = float(input("enter second number : "))
average = (num1 + num2)/2
print("The average is : ", average)

# Problem 4 - Simple Interest
P = int(input("enter principle number: "))
R= int(input("enter rate: "))
T = int(input("enter time: "))
SI = (P * R * T)/100
print("The result is: ", SI)

# Problem - 5 Temperature Converter
C = int(input("enter temperature in celsius : "))
F = (C * 9/5) + 32
print("The result is : ", F)

# Problem 6 - My Introduction
Name = input("enter your name : ")
Age = input("enter your age : ")# City = input("enter your city : ")
City = input("enter your city : ")
Dreamjob = input("enter your Dream job : ")
print("This is my introduction : ", Name , Age, City, Dreamjob)
