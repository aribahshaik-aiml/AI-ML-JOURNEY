# =============== FOR LOOP =============================
# for i in range (1, 6):
#     print(i)

# ================== WHILE LOOP =========================
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

#===================== BREAK =================
# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)

# ============= CONTINUE ===========================
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)
        
# =========== PASS ==============================
# for i in range (1, 6):
#     if i == 3:
#         pass
#     print(i)

# ====================== Day 5 - ASSIGNMENT ============================
# Print numbers 1 - 10 using while loops
# i = 1
# while i <= 11:
#     print(i)
#     i +=1

#Print even numbers 1 - 20 using for loop with break when you reach 12
# for i in range (1, 21):
#     if(i % 2 == 0):
#         print(i)
#         if i == 12:
#             break

#Print 1-10 using for loop but skip 5 using continue
for i in range (1, 11):
    if (i == 5):
        continue
    print(i)

#Print numbers 1 -20 using for loop
for i in range(1, 21):
    print(i)

#Print numbers 20 t0 1 (countdown)
for i in range(20, 0, -1):
    print(i)

#Multiplication table of 7
n = 7
for i in range(1, 11):
    print(n*i)

#Multiples of 3 from 1 to 50
n = 3
for i in range(1, 51):
    print(n*i)

#Sum of numbers from 1 to 50
total = 0
for i in range(1, 51):
    total = total + i
print("sum:", total)
