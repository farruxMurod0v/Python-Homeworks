

# def toq_juft():
#     """bu funksiya sonning toq yoki juft ekanligini aniqlaydi"""
#     son = int (input("son kiriting: "))
#     if son % 2 == 0:
#         print("juft son! ")
#     else:
#         print("toq son! ")

# toq_juft()




# def factorial(n):
#     """bu funksiya sonning faktariyalini hisoblaydi """
#     nat = 1
#     for i in range (1, n+1):
#         nat *= i
#     return(nat)
# print(factorial(5))


# def daraja(num_1, num_2):
#     """bu funksiya sonning darajasini hisoblaydi"""
#     return num_1**num_2
# print(daraja(3,3))



def tub(num):
    while  num % 1 and num % num:
        if num % num != 1 and num % 1:
            print("tub son")