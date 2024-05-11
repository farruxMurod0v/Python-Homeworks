# N1) sonlar = [34,34,5,35,234,35,35,5,3,4234,5423,5,453,54,234,344,23]
# print(sonlar)
# sonlar.reverse()
# print(sonlar)


# N2) import random
# for i in range (50):

#     a = random.randint(0,154)
#     print(a, end="\n")
# for i in range(1,len(a), 2):
#      print(a[i])


# N3) sonlar = [34,34,5,35,234,35,35,5,3,4234,5423,5,453,54,234,344,23]
# print(sonlar)
# yigindi = sum(sonlar)
# print(yigindi)

# N4) sonlar = [34,34,5,35,234,35,35,5,3,4234,5423,5,453,54,234,344,23]
# print(sonlar)
# max_num = max(sonlar)
# print(max_num)


# N5) text = ["phython, java, php, html,  css, mysql,  javascript, kotlin, unreal"]
# print(text, end="\n\n")
# tartib = sorted(text[0]. split(", "))
# print(tartib)


# N6) text = ["phython, java, php, html,  css, mysql,  javascript, kotlin, unreal"]
# print(text, end="\n\n")
# tartib = sorted(text[0]. split(", "))
# print(tartib)
# tartib.reverse()
# print(tartib)


#N7)  fruits = ("olma", "nok", "behi", "olma", "anjir", "banan", "olma", "anor")
# print(fruits)


# N8) fruits = ("olma", "nok", "behi", "olma", "anjir", "banan", "olma", "anor")
# print(fruits)
# fruit = input("fruitdagi  biron so'zni kiriting: ")
# count = fruits.count(fruit)
# print(f" {fruit}' so'zi {count}  marta qatnashgan.") 


# N9) text = ["phython", "java", "php", "html",  "css", "mysql",  "javascript", "kotlin", "unreal"]
# print(text, end="\n\n")
# text.pop()
# text.pop(0)
# print(text)


# N10) ranglar = ("red", "green", "white", "black", "pink", "yellow")
# ranglar = ranglar + ("blue",)
# print(ranglar)


# N11) ismlar = ["nodir", "qodir", "sherali", "jasur", "javlon", "doniyor", "sarvar", "ali", "vali"]
# ismlar_kirit = input("ism kiriting: ")
# if ismlar_kirit in ismlar:
#         print("ism  ro'xatda  bor")
# elif ismlar_kirit != ismlar:
#         ismlar.append(ismlar_kirit)
#         print("ism ro'yxatga qo'shildi! ")
# print(ismlar)


# N12) import random
# count=0
# for i in range (50):
#     a = random.randint(0,154)
#     print(a, end=" ")
#     count += 1
# print(end="\n\n")
# print(count, " ta sonlar bor")

# N13) import random
# ls = list()
# for i in range (50):
#     a = random.randint(0,154)
#     print(a, end=" ")
#     ls.append(a)
# print()
# print(max(ls))


#N14) import random
# ls = list()
# sum_son=0
# for i in range (50):
#     a = random.randint(0,154)
#     print(a, end=" ")
#     ls.append(a)
# print(end="\n\n")
# print(sum(ls), "  sonlar yig'indisi")


# N15) def fibonacci(n):
#     fib_list = [0, 1]  
#     for i in range(2, n):
#         fib_list.append(fib_list[i-1] + fib_list[i-2]) 
#     return fib_list
# n = 50 
# fib_numbers = fibonacci(n)
# print(fib_numbers)

# n = int(input("n fibanochchi son kiriting: "))
# one, two= 0,1
# for i in range (n):
#     print(one+two, end=" ")
#     tmp = one+ two
#     one = two
#     two = tmp



# son_10 = int (input("10 ta son kiriting: "))
# teskari_sonlar = []
# teskari_sonlar.append(son_10)
# print(teskari_sonlar)
# print()
# teskari_sonlar.reverse()
# print(teskari_sonlar)


# N16) son_10 = []
# for i in range(10):
#     son = int(input(f"{i+1}-sonni kiriting: "))
#     son_10.append(son)
# son_10.reverse()
# print(son_10)


# N17) l = list()
# for i in range(1, 10+1):
#     print(i, "- son kiriting: ")
#     a = int(input())
#     l.insert(0, a)
# print(l)


# N18) a, b = input().split()
# a = int(a)
# b = int(b)
# ls = list()
# while a <= b:
#     ls.append(a)
#     a+=1
# print(ls)


# N19) a =[10, 11, 8, 5, 7 , 9]
# for i in a:
#     for j in range(1,10):
#         print(f"{i} * {j} = {i * j}")
#         print()
#         print()

# N20) ans = []
# ls = list(input().split())
# for i in range(len(ls)):
#     ans.append(int(ls[i]) ** 2)
# print(ans)

# N 21) sonlar = [494, 4 ,948,484,89489,7878,45,4,9549,4,9,94,9, 8,79,885,45,495,7,89,87,7,8]
# orta_arifmetik = sum(sonlar) / len(sonlar)
# print("Orta arifmetik:", orta_arifmetik)

    
