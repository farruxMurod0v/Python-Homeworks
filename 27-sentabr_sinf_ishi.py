# import random
# for i in range (50):

#     a = random.randint(0,154)
#     print(a, end="\n")
# for i in range(1,len(a), 2):
#      print(a[i])

# import calendar
# y = 2023 #year
# m = 9 #month
# print(calendar.month(y,m))

# N1)a = int (input("son kiriting: "))
# for i in range (a):
#     if i % 15 == 0:
#         print("fizzbuzz", end=" ")
#     elif i % 5 == 0:
#         print("buzz", end=" ")
#     elif i % 3 == 0:
#         print("fizz", end=" ") 
#     else:       
#         print(i, end=" ")        

# N2)yig = 0
# son = int (input("son kiriting: "))
# for i in range(1, son+1):
#     yig += i
# print(yig)
 
# N3) yig=0
# a = int (input("a son kiriting: "))
# b = int (input("b son kiriting: "))
# for i in range(a, b+1):
#     yig += a
#     a +=1
# print(yig)



# N4) kop=1
# a = int (input("a son kiriting: "))
# b = int (input("b son kiriting: "))
# for i in range(a, b+1):
#     kop *= a
#     a += 1
# print(kop)

# N5) count=0
# k = int (input (" son kiriting: "))
# n = int (input("n marta ekranga chiqarish uchun son kiriting: "))
# for i in range (1, n+1):
#     print(k)



# N6)i = 2
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(i, end=" ")
#         j += 1
#     print()
#     i += 1


# i = 2
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(j, end=" ")
#         j += 1
#     print()
#     i += 1


# N7)revs_num =[15,12,15,13]
# print(revs_num)
# revs_num.reverse()
# print(revs_num)


# N8) facto = 1
# n= int (input("faktarialini topuvchi sonni kiriting: "))
# for i in range (1, n+1):
#     i+1
#     facto *= i
# print(facto)

# N9) son=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
# print(son)

#N10) n = int(input("n fibanochchi son kiriting: "))
# one, two= 0,1
# for i in range (n):
#     print(one+two, end=" ")
#     tmp = one+ two
#     one = two
#     two = tmp
