# def salom():
#     """bu funksiya bolajaonlar bilan salomlashadi! """
#     print("salom bolajonlar! ")


# salom()



# def ismlar (**ism):
#     """bu funksiya eng uzun ismni qaytaradi """
#     input("ism kiriting:")
#     return max(ism)

# ismlar()

# def ismlar():
#     """bu funksiya eng uzun ismni qaytaradi """
#     n = int(input("Nechta ismni kiriting: "))
#     ismlar = []
#     for i in range(n):
#         ism = input(f"{i+1}-ismni kiriting: ")
#         ismlar.append(ism)
#     eng_uzun_ism = max(ismlar, key=len)
#     print(f"Eng uzun ism: {eng_uzun_ism}")
# ismlar()



# def baholar(*baho):
#     """bu funksiya baholarni o'rta qiymatini qaytaradi """
#     n = int(input("Nechta baholigini kiriting: "))
#     ballar = []
#     for i in range(n):
#         baho = int (input("baholarni kiriting: "))
#         ballar.append(baho)

#     ortacha_baho = sum(ballar) / n
#     print(f"o'rtacha baho: {ortacha_baho}")
# baholar()



# def ismlar():
#     """bu funksiya eng qisqasini ismni qaytaradi """
#     n = int(input("Nechta ismni kiriting: "))
#     ismlar = []
#     for i in range(n):
#         ism = input(f"{i+1}-ismni kiriting: ")
#         ismlar.append(ism)
#     eng_qisqa_ism = min(ismlar, key=len)
#     print(f"Eng qisqa ism: {eng_qisqa_ism}")
# ismlar()

# def reverse_text(text):
#     """bu funksiya matnni teskari tartibga o'girib beradi """
#     print(text[::-1])

# reverse_text("Parametr argument sifatida matn olib uni teskari tartibda chiqarib beradigan funksiya tuzing.")



# def max_num(num1, num2, num3):
#     """bu funksiya 3 ta sonning eng kattasini ekranga chiqardi """
#     if num1 > num2 and num3:
#         print(num1)
#     elif num2 > num1 and num3:
#         print(num2)
#     else:
#         print(num3)

# max_num(87, 584, 95)

# def uch(num):
#     """funkiyaning vazifasini sonning kubini topadi"""
#     print(num * num * num)
   
# uch(8)


# def toq_juft(son):
#     """funksiya berilgan sonning toq yoki juft ekanligini aniqlaydi"""
#     if son % 2 == 0:
#         print("juft son")
#     else:
#         print("toq son")

# toq_juft(84)


# def big(word):
#     """so'zning hamma harflarni katta harfga o'zgartirib beradi"""
#     print(word.upper())
# big ("nozanin")



def karra(num):
    """sonning karra jadvalini chiqaradi"""
    for i in range (1, num+1):
        for j in range(1, 10):
            print(i * j)

karra(7)
