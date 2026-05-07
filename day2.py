#===================================== Day 2 - ASSIGNMENT ==============================================================================
#Problem 1 - String Length ===========>
name = input("enter your name: ")
print(len(name))

#Problem 2 - Slicing ========================>
word = "aribah"
print(word[0:3]) #print's first three letters
print(word[3:6]) #print's last three letters

#Problem 3 - String Functions ======================>
name = input("enter your name: ")
print(name.upper()) 
print(name.lower()) 
print(name.capitalize())
print(name.count("a"))

#Problem 4 - Odd or Even ==================================>
num = int(input("enter number: "))
rem = num % 2
if(rem == 0):
    print("EVEN")
else:
    print("ODD")

#Problem 5 - Grading System ================================>
marks = int(input("enter marks: "))
if(marks >= 90):
    print("A grade")
elif(marks >= 80):
    print("B grade")
elif(marks >= 70):
    print("C grade")
elif(marks >= 60):
    print("D grade")
else:
    print("fail")

#Problem 6 - Greatest Number ==========================================================>
a = int(input("enter first number: "))
b= int(input("enter second number: "))
c= int(input("enter third number: "))
if(a >=b and a>=c):
    print ("a is greatest number ")
elif(b >=a and b>=c):
    print("b is greatest number")
else:
    print("c is greatest number")

