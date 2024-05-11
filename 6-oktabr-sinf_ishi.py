# import random
# num1 = int (input("birinchi sonni kiriting: "))
# num2 = int (input("ikkinchi sonni kiriting: "))
# son = random.randint(num1, num2)
# print(son)


# import random

# tanga = random.randint(0,1)
# if tanga == 0:
#     print("chikka!")
# elif tanga == 1:
#     print("pukka")


# import random

# def generate_password(length):
#     password = ''
#     characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
#     for _ in range(length):
#         password += random.choice(characters)
#     return password
# length = int(input("Parol uzunligini kiriting: "))
# password = generate_password(length)
# print("Generatsiya qilingan parol:", password)


# birinchi = int (input ("birinchi toshni tashlang: "))
# ikkinchi = int (input ("ikkinchi toshni tashlang: "))
# import random
# bir = random.randint(1, 6)
# ikki = random.randint(1, 6)
# print(bir)
# print(ikki)

# import random
# rand_num = random.randint(1, 15)
# while True:
#     num = int (input ("taxminiy sonni topish uchun son kiriting: "))
#     if num < rand_num:
#         print("kiritgan soningiz random sondan kichik")
#     elif num > rand_num:
#         print("kiritgan soningiz random sondan katta")
#     else:
#         print("to'gri toptingiz!!!")
#         break


# import math
# num = int (input("son kiriting: "))
# print(math.sqrt(num))

# radius = float(input("Doira radiusini kiriting: "))
# area = math.pi * math.pow(radius, 2)
# print("Doira yuzasi:", area)









# import math
# angle = float(input("Burchakni kiriting: "))
# sin = math.sin(math.radians(angle))
# cos = math.cos(math.radians(angle))
# print("Sinus:", sin)
# print("Kosinus:", cos)




# import math
# angle = float(input("Burchakni kiriting: "))
# sin = math.sin(math.radians(angle))
# cos = math.cos(math.radians(angle))
# hypotenuse = math.sqrt(sin**2 + cos**2)
# print("Gipotenuza:", hypotenuse)




import os
for i in range(1, 31):
    papka = "papka" + str(i)
    os.mkdir(papka)
    os.rmdir(f"directory{i}")