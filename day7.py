# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
#     print("end")

# show(3)    

# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n

# print(fact(6))

# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(10) 
# print(sum)   

# def print_list(items, idx=0):
#     if(idx == len(items)):
#         return
    
#     print(items[idx])
#     print_list(items, idx +1)

# fruits = ["mango", "litchi", "apple", "banana"]   

# print_list(fruits) 
 
#======================= Day 7 - ASSIGNMENT =======================================================
#Problem 1 - Countdown
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(10) 
# print("Blast off!")

#Problem 2 - Factorial
# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n

# print(fact(5))
# print(fact(6))

#Problem 3 - Sum of numbers
# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(5) 
# print(sum) 

#Problem 4 - Power
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2, 3))
print(power(3, 2))

 