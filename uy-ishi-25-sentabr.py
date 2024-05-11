
# N1) for i in range (1, 101) :
#     print(i)

# N2)for i in range (101, 0, -1):
    
#     print(i)
 
# N3)for i in range(1, 101) :
#     if i % 2 == 1:
#         print(i)

# N4for i in range (1, 101):
#    if i % 2 == 0:
#      print(i)

# N5)for i in range (100, 1000):
#     if i % 50 == 0 :
#         print(i)

# N6)for i in range (1, 500):
    
#     if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
#       continue
#     print(i)

# N7)while True:
#     print("RAMAZON MUBORAk")

# N8)a = int (input("a="))
# k = a
# for i in range (a, 1 , -1):
#     print("*"*i, end="")
#     print(" "*(a-i), end="")
#     print(" "
#     (a-i), end="")
#     print("*"*i)

# N9)butun_son = int (input("butun son kiriting: "))
# daraja = butun_son ** 15
# print(f"{butun_son} ning ketma ket 15-darajasi: {daraja}")
   
#N10) temp = float (input("haroratingizni kiriting: "))
# if temp > 36.6 or temp < 36.6:
#     print("tana haroratingiz normal emas ")
# else :
#     print("tana haroratingiz normal")    

# N11)son = int  (input("son kiriting "))
# while son > 0:
#     son = int (input("son kiriting "))
# print("tugadi")  

# N12)son = int (input("son kiriting: "))
# if son > 0 :
#     print("musbat  son")
# elif son < 0 :
#     print("manfiy son")    
# elif son == 0:
#     print("tamom")

# print("son kiriting ")
# son = int
# while son != -1:
#     son = int (input("istalgancha son kiriting:  "))
# print()



# N14) a = int (input ("a son kiriting: "))
# n = int (input ("n qiymat  kiriting: "))
# while n > 0 :
#     print(a)
#     n -= 1
    
# N15)butun_son = int (input ("butun son kiriting: "))
# kv_yig = 0
# for i in range (1, butun_son+1):
#     k = i*i
#     kv_yig +=k
# print(butun_son, "gacha bo'lgan sonlarning kvadratlari yig'indisi", kv_yig, "ga teng")   

    
#N 16) butun_son = int (input ("butun son kiriting: "))
# kv_yig = 0
# for i in range (1, butun_son+1):
#   if butun_son % 2 == 1:
#     k = i*i
#     kv_yig +=k
# print(butun_son, "gacha bo'lgan sonlarning kvadratlari yig'indisi", kv_yig, "ga teng")   


# N17)ikki_n = int (input ("butun son kiriting: "))
# kv_yig = 0
# n = int (input("n son kiriting: "))
# for i in range (n, ikki_n*2+1):
#     k = i*i
#     kv_yig +=k
# print(ikki_n, "gacha bo'lgan sonlarning kvadratlari yig'indisi", kv_yig, "ga teng")   

# N 18) password = "qwerty111"
# count = 0 
# while count < 5: 
#    kod = str (input("parolni kiriting "))
#    if kod != password:
#     print("kod xato")
#     count +=1
#    elif password == kod:
#     print("ZEd maxfiy")
#    elif count == 5:
#      print("bloklandi")

# N19) son = int (input("Musbat son kiriting: "))
# if son % son == 0 and son % 1 == 0:
#     print("tub son")
# else :
#     print("murakkab son")

# N20)on, two = 0,1
# for _ in range(20):
#     print(on+two, end=" ")
#     temp = on +two
#     on = two
#     tw = temp

# N13)n = int (input("istalgancha son kiriting"))
# mx,mn,oa,s,cnt, = n, n, 0, n, 0
# while n != -1:
#     SON = int (input("istalgancha son kiriting"))
#     if n > mx:
#         mx = n
#     if n < mn:
#         mn = n
#     s += n
#     cnt +=1
# print(f"""
# kiritilganlar soni {cnt}
# sonlar yig;indisi {s}
# orta arifmetigi {s/cnt}
# max {mx}
# min {mn}
#       """)    