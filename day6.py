#1. Simple function
# def say_hello():
#     print("Hello World!")
# say_hello()    

#2. Function with parameter
# def greet(name):
#     print("Hello", name)
# greet("Aribah") 

#3. Function with return
# def add(a,b):
#     return a + b  
# print(add(5,3))

#4. Default argument
# def introduce(name, city="Hyderabad"):
#     print("I am", name, "from", city)
# introduce("Aribah")
# introduce("Sara", "Hyderabad") 
  
#=================================== Day 6 - ASSIGNMENT ======================================================

#Problem 1 - Rectangle area function
# def calculate_area(length,breadth):
#     return length * breadth

# area = calculate_area(2,4)
# print(area)

#Problem 2 - Check Even number Using Function
# def is_even(number):
#     return number % 2 == 0
# print(is_even(4))
# print(is_even(7))

#Problem 3 - 
# def greet_student(subject = "Python"):
#     print("I am learning", subject)

# greet_student()   

#Problem 4 - Find the Largest of Three Numbers  
# def find_max(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
# print(find_max(10,25,15))    

#Problem 5 - Simple Function
# def function():
#     print("Welcome to Python!")
# function()    

#Problem 6 - Default Argument
# def student_info(name, grade = "A"):
#     print("Name:", name)
#     print("Grade:", grade)
# student_info("Aribah")   
# student_info("Aribah", "B") 

#Problem 7 -
def check_evenorodd():
    num = int(input("enter number : "))
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
print(check_evenorodd())







        
        
    





 
